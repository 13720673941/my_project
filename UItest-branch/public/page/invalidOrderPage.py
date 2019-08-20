#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/3 18:50

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By

class InvalidOrder(BasePage):
    """
    设置无效工单页面
    """

    # 无效工单按钮
    invalid_order_btn = (By.XPATH,'//a[text()="无效工单"]')
    # 无效类型选择框
    invalid_type_select = (By.XPATH,'//label[contains(text(),"无效工单类型：")]/../div/select')
    # 无效原因输入框
    invalid_reason_input = (By.XPATH,'//label[text()="无效工单理由："]/../*/*/textarea')
    # 无效工单确定按钮
    confirm_btn = (By.XPATH,'//div[text()="无效工单"]/../../div[3]/button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_invalid_btn(self):
        """点击无效工单按钮"""
        self.click_button(self.invalid_order_btn)

    def select_invalid_type(self,invalidType):
        """选择无效工单类型"""
        if invalidType != '':
            self.operate_select(self.invalid_type_select,invalidType)

    def input_invalid_reason(self):
        """输入无效工单原因"""
        self.input_message(self.invalid_reason_input,self.get_now_time(Time=True))

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.confirm_btn)
