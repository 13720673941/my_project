# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/26 21:20

"""
封装所有页面对象的基础类，POM模式下所有页面类继承该基类
"""

from .click import Click
from .input import Input


class PySelenium(Click, Input):
    pass
