# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:34

from public.common.basePage import BasePage
from config.urlConfig import *

class MasterReturnPage(BasePage):

    """
        【备件管理】-【师傅返还】页面
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中师傅返还备件页面的元素信息"""
        return read_config_data("master_return_page",option,elementDataPath)

    def click_master_return_button(self):
        """点击师傅返还"""
        self.click_button(self.get_elements("master_return_btn"))

    def select_return_master_name(self,masterName):
        """选择返还备件的师傅名称"""

        self.operate_not_select(
            open_el=self.get_elements("open_allot_out_btn"),
            parent_el=self.get_elements("allot_out_parent_element"),
            value=masterName
        )

    def input_spare_part_number(self,spNumber):
        """输入备件条码"""
        self.input_message(self.get_elements("return_sp_number_input"),spNumber)

    def click_spare_part_number(self):
        """选择模糊匹配的备件条码"""
        self.click_button(self.get_elements("sp_number_parent_element"))

    def get_search_sp_number(self):
        """获取模糊匹配的备件条码"""

        try:
            sp_number = self.get_text(self.get_elements("sp_number_parent_element"))
        except:
            sp_number = "没有按条码匹配出备件"

        return sp_number

    def input_spare_part_name(self,spName):
        """输入备件名称"""
        self.input_message(self.get_elements("return_sp_name_input"),spName)

    def click_spare_part_name(self):
        """选择模糊匹配的备件名称"""
        self.click_button(self.get_elements("sp_name_parent_element"))

    def get_search_sp_name(self):
        """获取模糊匹配的备件名称"""

        try:
            sp_name = self.get_text(self.get_elements("sp_name_parent_element"))
        except:
            sp_name = "没有按名称匹配出备件"

        return sp_name

    def get_master_inventory_count(self):
        """获取师傅备件库存数量"""

        try:
            master_inventory = self.get_text(self.get_elements("master_sp_inventory_count"))
        except:
            master_inventory = "没有获取到师傅库存"

        return master_inventory

    def input_sp_return_count(self,spCount):
        """输入备件返还数量"""
        self.input_message(self.get_elements("return_count_input"),spCount)

    def get_input_return_count(self):
        """获取输入的返还数量大于库存会自动变为师傅最大库存值"""

        try:
            input_number = self.get_att(self.get_elements("return_count_input"),"value")
        except:
            input_number = "没有获取到输入的库存"

        return input_number

    def click_save_button(self):
        """点击返还保存"""
        self.click_button(self.get_elements("save_return_info"))

    def get_search_sp_all_info(self):
        """获取模糊匹配的备件的全部信息"""

        first_row_info = self.get_text(self.get_elements("search_sp_info"))
        # 第一行默认的没有备件信息，用删除字段判断是否有备件匹配出来
        if "删除" not in first_row_info:
            return "没有模糊匹配出备件信息"
        else:
            return first_row_info
