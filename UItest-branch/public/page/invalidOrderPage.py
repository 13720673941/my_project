#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/3 18:50

from public.common.basePage import BasePage
from public.common.rwConfig import read_config_data
from config.urlConfig import *
from config.pathConfig import *

class InvalidOrder(BasePage):
    """
        【设置无效工单页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_invalid_list_page(self):
        """无效工单列表页"""
        self.open_url(invalid_order_url)

    def get_elements(self,option):
        """获取element_data文件中设置无效工单的元素信息"""
        return read_config_data("invalid_order_page",option,elementDataPath)

    def click_invalid_btn(self):
        """点击无效工单按钮"""
        self.click_button(self.get_elements("invalid_order_btn"))

    def select_invalid_type(self,invalidType):
        """选择无效工单类型"""
        if invalidType != '':
            self.operate_select(self.get_elements("invalid_type_select"),invalidType)

    def input_invalid_reason(self,invalidReason):
        """输入无效工单原因"""
        self.input_message(self.get_elements("invalid_reason_input"),invalidReason)

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.get_elements("confirm_btn"))
