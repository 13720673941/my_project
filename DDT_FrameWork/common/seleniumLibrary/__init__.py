# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/26 21:20

"""
封装所有页面对象的基础类，POM模式下所有页面类继承该基类
"""

from .window import Window
from .alert import Alert
from .element import Element
from .frame import Frame
from .actions import Actions
from .cookie import Cookie


class PySelenium(Window, Alert, Element, Frame, Actions, Cookie):
    pass
