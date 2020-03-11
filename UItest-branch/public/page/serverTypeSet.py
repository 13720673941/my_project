# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/11 10:42

from public.common.basePage import BasePage
from selenium.webdriver.common.by import By

class ServerTypeSet(BasePage):

    """
    系统设置-工单基本设置-服务类型设置
    """

    def click_add_server_type(self):
        """点击添加服务类型"""
        self.click_button(By.XPATH,'//a[contains(text(),"添加服务类型")]')

