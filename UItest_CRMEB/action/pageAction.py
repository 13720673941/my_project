# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:36

"""
webdriver类中操作浏览器方法二次封装
"""

from util.browserDriver import BrowserDriver


class PageAction(BrowserDriver):

    def __init__(self):
        BrowserDriver.__init__(self)



