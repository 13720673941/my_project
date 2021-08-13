# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/16 18:06

"""
    项目中全部使用的文件夹的路径
"""

import os

# 获取父路径
PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# log 日志保存文件夹路径
LOG_SAVE_PATH = os.path.join(PARENT_PATH,"log")+"\\"
# 测试用例保存文件路径
TEST_CASE_PATH = os.path.join(PARENT_PATH,"params","data","apiTestCase.xls")
# 工共变量储存地址
GLOBAL_PARAMS_PATH = os.path.join(PARENT_PATH,"config","globalParams.ini")
# 请求数据保存文件夹
REQUEST_DATA_PATH = os.path.join(PARENT_PATH,"params","data","requestData.json")