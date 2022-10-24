# -*- coding: utf-8 -*-
# file: apc_config_manager.py
# time: 2021/5/26 0026
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

import copy

# if you find the optimal param set of some situation, e.g., some model on some datasets
# please share the main use template main
from pyabsa.functional.config.config_manager import ConfigManager
from pyabsa.core.tc.classic.__bert__.models import BERT
from pyabsa.core.tc.classic.__glove__.models import LSTM

_tc_config_template = {'model': BERT,
                       'optimizer': "adamw",
                       'learning_rate': 0.00002,
                       'patience': 99999,
                       'pretrained_bert': "microsoft/mdeberta-v3-base",
                       'cache_dataset': True,
                       'warmup_step': -1,
                       'show_metric': False,
                       'max_seq_len': 80,
                       'dropout': 0,
                       'l2reg': 0.000001,
                       'num_epoch': 10,
                       'batch_size': 16,
                       'initializer': 'xavier_uniform_',
                       'seed': 52,
                       'polarities_dim': 3,
                       'log_step': 10,
                       'evaluate_begin': 0,
                       'cross_validate_fold': -1,
                       'use_amp': False,
                       # split train and test datasets into 5 folds and repeat 3 training
                       }

_tc_config_base = {'model': BERT,
                   'optimizer': "adamw",
                   'learning_rate': 0.00002,
                   'pretrained_bert': "https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1",
                   'cache_dataset': True,
                   'warmup_step': -1,
                   'show_metric': False,
                   'max_seq_len': 80,
                   'patience': 99999,
                   'dropout': 0,
                   'l2reg': 0.000001,
                   'num_epoch': 10,
                   'batch_size': 16,
                   'initializer': 'xavier_uniform_',
                   'seed': 52,
                   'polarities_dim': 3,
                   'log_step': 10,
                   'evaluate_begin': 0,
                   'cross_validate_fold': -1
                   # split train and test datasets into 5 folds and repeat 3 training
                   }

_tc_config_english = {'model': BERT,
                      'optimizer': "adamw",
                      'learning_rate': 0.00002,
                      'patience': 99999,
                      'pretrained_bert': "https://huggingface.co/yangheng/deberta-v3-base-absa-v1.1",
                      'cache_dataset': True,
                      'warmup_step': -1,
                      'show_metric': False,
                      'max_seq_len': 80,
                      'dropout': 0,
                      'l2reg': 0.000001,
                      'num_epoch': 10,
                      'batch_size': 16,
                      'initializer': 'xavier_uniform_',
                      'seed': 52,
                      'polarities_dim': 3,
                      'log_step': 10,
                      'evaluate_begin': 0,
                      'cross_validate_fold': -1
                      # split train and test datasets into 5 folds and repeat 3 training
                      }

_tc_config_multilingual = {'model': BERT,
                           'optimizer': "adamw",
                           'learning_rate': 0.00002,
                           'patience': 99999,
                           'pretrained_bert': "microsoft/mdeberta-v3-base",
                           'cache_dataset': True,
                           'warmup_step': -1,
                           'show_metric': False,
                           'max_seq_len': 80,
                           'dropout': 0,
                           'l2reg': 0.000001,
                           'num_epoch': 10,
                           'batch_size': 16,
                           'initializer': 'xavier_uniform_',
                           'seed': 52,
                           'polarities_dim': 3,
                           'log_step': 10,
                           'evaluate_begin': 0,
                           'cross_validate_fold': -1
                           # split train and test datasets into 5 folds and repeat 3 training
                           }

_tc_config_chinese = {'model': BERT,
                      'optimizer': "adamw",
                      'learning_rate': 0.00002,
                      'patience': 99999,
                      'cache_dataset': True,
                      'warmup_step': -1,
                      'show_metric': False,
                      'pretrained_bert': "bert-base-chinese",
                      'max_seq_len': 80,
                      'dropout': 0,
                      'l2reg': 0.000001,
                      'num_epoch': 10,
                      'batch_size': 16,
                      'initializer': 'xavier_uniform_',
                      'seed': 52,
                      'polarities_dim': 3,
                      'log_step': 10,
                      'evaluate_begin': 0,
                      'cross_validate_fold': -1
                      # split train and test datasets into 5 folds and repeat 3 training
                      }

_tc_config_glove = {'model': LSTM,
                    'optimizer': "adamw",
                    'learning_rate': 0.001,
                    'cache_dataset': True,
                    'warmup_step': -1,
                    'show_metric': False,
                    'max_seq_len': 100,
                    'patience': 20,
                    'dropout': 0.1,
                    'l2reg': 0.000001,
                    'num_epoch': 100,
                    'batch_size': 64,
                    'initializer': 'xavier_uniform_',
                    'seed': 52,
                    'embed_dim': 300,
                    'hidden_dim': 300,
                    'polarities_dim': 3,
                    'log_step': 5,
                    'warm_step': -1,
                    'hops': 3,  # valid in MemNet and RAM only
                    'evaluate_begin': 0,
                    'cross_validate_fold': -1
                    }


class TCConfigManager(ConfigManager):
    def __init__(self, args, **kwargs):
        """
        Available Params:  {'model': BERT,
                            'optimizer': "adamw",
                            'learning_rate': 0.00002,
                            'pretrained_bert': "roberta-base",
                            'cache_dataset': True,
                            'warmup_step': -1,
                            'show_metric': False,
                            'max_seq_len': 80,
                            'patience': 99999,
                            'dropout': 0,
                            'l2reg': 0.000001,
                            'num_epoch': 10,
                            'batch_size': 16,
                            'initializer': 'xavier_uniform_',
                            'seed': {52, 25}
                            'embed_dim': 768,
                            'hidden_dim': 768,
                            'polarities_dim': 3,
                            'log_step': 10,
                            'evaluate_begin': 0,
                            'cross_validate_fold': -1 # split train and test datasets into 5 folds and repeat 3 training
                            }
        :param args:
        :param kwargs:
        """
        super().__init__(args, **kwargs)

    @staticmethod
    def set_tc_config(configType: str, newitem: dict):
        if isinstance(newitem, dict):
            if configType == 'template':
                _tc_config_template.update(newitem)
            elif configType == 'base':
                _tc_config_base.update(newitem)
            elif configType == 'english':
                _tc_config_english.update(newitem)
            elif configType == 'chinese':
                _tc_config_chinese.update(newitem)
            elif configType == 'multilingual':
                _tc_config_multilingual.update(newitem)
            elif configType == 'glove':
                _tc_config_glove.update(newitem)
            else:
                raise ValueError(
                    "Wrong value of config type supplied, please use one from following type: template, base, english, chinese, multilingual, glove")
        else:
            raise TypeError("Wrong type of new config item supplied, please use dict e.g.{'NewConfig': NewValue}")

    @staticmethod
    def set_tc_config_template(newitem):
        TCConfigManager.set_tc_config('template', newitem)

    @staticmethod
    def set_tc_config_base(newitem):
        TCConfigManager.set_tc_config('base', newitem)

    @staticmethod
    def set_tc_config_english(newitem):
        TCConfigManager.set_tc_config('english', newitem)

    @staticmethod
    def set_tc_config_chinese(newitem):
        TCConfigManager.set_tc_config('chinese', newitem)

    @staticmethod
    def set_tc_config_multilingual(newitem):
        TCConfigManager.set_tc_config('multilingual', newitem)

    @staticmethod
    def set_tc_config_glove(newitem):
        TCConfigManager.set_tc_config('glove', newitem)

    @staticmethod
    def get_tc_config_template() -> ConfigManager:
        _tc_config_template.update(_tc_config_template)
        return TCConfigManager(copy.deepcopy(_tc_config_template))

    @staticmethod
    def get_tc_config_base() -> ConfigManager:
        _tc_config_template.update(_tc_config_base)
        return TCConfigManager(copy.deepcopy(_tc_config_template))

    @staticmethod
    def get_tc_config_english() -> ConfigManager:
        _tc_config_template.update(_tc_config_english)
        return TCConfigManager(copy.deepcopy(_tc_config_template))

    @staticmethod
    def get_tc_config_chinese() -> ConfigManager:
        _tc_config_template.update(_tc_config_chinese)
        return TCConfigManager(copy.deepcopy(_tc_config_template))

    @staticmethod
    def get_tc_config_multilingual() -> ConfigManager:
        _tc_config_template.update(_tc_config_multilingual)
        return TCConfigManager(copy.deepcopy(_tc_config_template))

    @staticmethod
    def get_tc_config_glove() -> ConfigManager:
        _tc_config_template.update(_tc_config_glove)
        return TCConfigManager(copy.deepcopy(_tc_config_template))
