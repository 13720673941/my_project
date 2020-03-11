# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/16 19:07

from public.common.basePage import BasePage
from config.urlConfig import *

class NewReturnFactoryPage(BasePage):

    """
        【备件管理】-【新件返还】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self, option):
        """获取element_data文件中新建返厂功能的元素信息"""
        return read_config_data("new_sp_return_factory_page",option,elementDataPath)

    def enter_wait_return_page(self):
        """进入待返厂备件页面"""
        self.open_url(wait_return_factory_url)

    def enter_already_return_page(self):
        """进入已返厂备件页面"""
        self.open_url(already_return_faction_url)

    def click_new_sp_return(self):
        """点击新件返厂"""
        self.click_button(self.get_elements("new_parts_return_btn"))

    def input_return_count(self,spCount):
        """输入返厂备件数量"""
        self.input_message(self.get_elements("parts_count_input"),spCount)

    def get_count_number(self):
        """获取输入的最大返厂数量"""
        return self.get_att(self.get_elements("parts_count_input"),"value")

    def click_save_return(self):
        """点击确定返厂"""
        self.sleep(2)
        self.click_button(self.get_elements("save_new_parts_return"))

    def select_all_return_sp(self):
        """批量返厂选择全部备件"""
        self.click_button(self.get_elements("batch_select_input"))

    def click_batch_return_btn(self):
        """点击批量返厂按钮"""
        self.click_button(self.get_elements("batch_return_factory_btn"))

    def input_batch_return_remark(self,returnRemark):
        """输入批量返厂备注"""
        self.input_message(self.get_elements("remark_input"),returnRemark)

    def click_confirm_batch_return(self):
        """点击确认批量返厂"""
        self.click_button(self.get_elements("save_remark_btn"))

    def click_confirm_return_btn(self):
        """点击确认返厂按钮"""
        self.click_button(self.get_elements("confirm_return_factory_btn"))

    def get_first_row_log_info(self):
        """获取待返厂第一条全部的信息"""
        return self.get_text(self.get_elements("first_row_info"))

