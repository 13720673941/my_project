# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/15 23:33

"""
项目中封装的装饰器
"""

from common.tools.logConfig import Logger

import traceback

# 实例化类文件
Log = Logger().origin_logger


def error_collection(func):
    """
    错误日志收集器
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            Log.error("\n" + traceback.format_exc())

    return inner
