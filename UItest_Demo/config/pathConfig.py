# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 14:43

import os

"""
    数据以及文件夹路径配置文件
"""

# 获取 UItest_Demo 文件夹的相对路径
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 输出日志的文件夹路径
logPath = os.path.join(parentPath,"result","log")