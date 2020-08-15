# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/14 17:21

"""
所有页面路由地址存放文件
"""

from public.common.operateFile import OperateFile

# 读取工共url变量
GLOBAL_URL = OperateFile().get_config_data("GLOBAL_URL","URL")