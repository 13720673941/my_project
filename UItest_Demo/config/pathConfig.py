# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 14:43

import os

"""
    数据以及文件夹路径配置文件
"""

# 获取 UItest_Demo 文件夹的相对路径
PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# chrome驱动存放路径
CHROME_DRIVER_PATH = os.path.join(PARENT_PATH,"config","driver","chromedriver.exe")
# 输出日志的文件夹路径
LOG_SAVE_PATH = os.path.join(PARENT_PATH,"result","log")+"\\"
# 配置文件路径
CONFIG_DATA_PATH = os.path.join(PARENT_PATH,"config","configData.ini")
# 测试数据excel文件路径
TEST_DATA_PATH = os.path.join(PARENT_PATH,"data","UItest_case.xls")
# 错误截图保存文件夹路径
ERROR_IMG_PATH = os.path.join(PARENT_PATH,"result","Img")+"\\"
# 测试用例存放文件夹路径
TEST_SCRIPT_PATH = os.path.join(PARENT_PATH,"script")+"\\"
# 测试报告存放路径
REPORT_SAVE_PATH = os.path.join(PARENT_PATH,"result","report")+"\\"