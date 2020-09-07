# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/14 15:13

"""
框架中各个文件夹的相对路径配置
"""

import os

# 获取相对父路径信息
PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 谷歌驱动保存文件保存路径
CHROME_DRIVER_PATH = os.path.join(PARENT_PATH,"config","driver","chromedriver.exe")
# 全局变量文件路径
GLOBAL_PARAMS_PATH = os.path.join(PARENT_PATH,"config","globalParams.ini")
# 测试数据保存文件夹路径
TEST_DATA_PATH = os.path.join(PARENT_PATH,"data","UItest_data.xls")
# 错误截图保存文件夹路径
ERROR_IMG_PATH = os.path.join(PARENT_PATH,"result","img")
# 日志文件保存文件夹路径
LOG_SAVE_PATH = os.path.join(PARENT_PATH,"result","log")
# 测试报告保存文件夹路径
TEST_REPORT_PATH = os.path.join(PARENT_PATH,"result","report")
