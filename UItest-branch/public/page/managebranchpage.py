# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/26 12:00
from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
"""
客户管理-经销商列表页面
"""
class ManageBranchPage(BasePage):

    def __init__(self,driver):
        BasePage.__init__(self,driver)