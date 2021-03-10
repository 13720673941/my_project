# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/02/10 21:13

"""
    异常堆栈收集捕获
"""

import traceback

from util.logConfig import Logger

Log = Logger().logger


def exception_stack(func):
    def inner(self, *args):
        try:
            func(self, args)
        except:
            Log.error(traceback.format_exc())
    return inner