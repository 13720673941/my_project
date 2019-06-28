# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:27

from selenium.webdriver.common.by import By
from public.common.basepage import BasePage
"""
客户管理-服务商列表页面
"""
class ServerBranchPage(BasePage):

    """页面元素路径"""
    #切换服务商的table按钮
    server_branch_table = (By.XPATH,'//a[text()="服务商]')





    def __init__(self,driver):
        BasePage.__init__(self,driver)

