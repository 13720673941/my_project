# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2021/2/21 20:53

"""
所有页面类对象继承该base基础类
"""

from util.pySelenium import PySelenium


class BasePages:

    def __init__(self, driver: PySelenium): # 声明driver类型为PySelenium中的变量
        self.driver = driver