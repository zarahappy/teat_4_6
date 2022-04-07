# -*- coding: utf-8 -*-
# Time : 2022/4/3 22:14
# Author : shelly
# File : run_pytest.py
# Desc :

import pytest
import subprocess

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)