# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/9 11:08

from public.common.pySelenium import PySelenium

"""
    所有页面的page类全部继承该base类
"""

class Page:
    def __init__(self,driver:PySelenium): # this 指向PySelenium类，指定参数 this 为PySelenium类型的变量
        self.driver = driver