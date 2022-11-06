# -*- coding: utf-8 -*-
# file: notification_utils.py
# time: 05/11/2022 23:38
# author: yangheng <hy345@exeter.ac.uk>
# github: https://github.com/yangheng95
# GScholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# ResearchGate: https://www.researchgate.net/profile/Heng-Yang-17/research
# Copyright (C) 2022. All Rights Reserved.
import os

from pyabsa.framework.flag_class.flag_template import PyABSAMaterialHostAddress

import requests
from termcolor import colored

def check_emergency_notification():
    """
    Check if there is any emergency notification from PyABSA
    """

    url = PyABSAMaterialHostAddress + 'resolve/main/emergency_notification.txt'

    try:  # from Huggingface Space
        response = requests.get(url, stream=True)
        save_path = 'emergency_notification.txt'
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        with open(save_path, 'r') as f:
            print(colored('PyABSA: '+f.read(), 'red'))
        os.remove(save_path)
    except Exception as e:
        pass