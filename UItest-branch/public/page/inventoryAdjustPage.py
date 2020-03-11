# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/12 15:37

from public.common.basePage import BasePage
from public.page.spartPartListPage import SparePartListPage
from config.urlConfig import *

class InventoryAdjust(BasePage):
    """
        【备件管理】-【库存调整】页面、库存调整功能
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        # 实例化备件搜索类
        self.search_sp = SparePartListPage(driver)

    def get_elements(self,option):
        """获取element_data文件中备件库存调整页面的元素信息"""
        return read_config_data("inventory_adjust_page",option,elementDataPath)

    def enter_inventory_adjust_log_page(self):
        """进入库存调整页面"""
        self.open_url(inventory_adjust_url,self.get_elements("operate_start_date_input"))

    def click_inventory_adjust(self):
        """点击库存调整"""
        self.click_button(self.get_elements("inventory_adjust_btn"))

    def input_after_adjust_inventory(self,afterAdjustCount):
        """输入调整后的备件库存数量"""
        self.clear_input(self.get_elements("adjust_number_input"))
        self.sleep(1)
        self.input_message(self.get_elements("adjust_number_input"),afterAdjustCount)

    def input_adjust_reason(self,adjustReason):
        """输入调整库存备注信息"""
        self.input_message(self.get_elements("adjust_reason_input"),adjustReason)

    def click_confirm_adjust(self):
        """点击保存确定调整"""
        self.click_button(self.get_elements("confirm_adjust_btn"))

    def get_all_inventory_count(self):
        """获取总库存数量"""
        try:
            return self.get_text(self.get_elements("all_inventory_number"))
        except:
            return 0

    def select_operator_name(self,operatorName):
        """选择操作人"""
        if operatorName != "":
            self.operate_not_select(
                open_el=self.get_elements("open_operator_btn"),
                parent_el=self.get_elements("operator_parent_element"),
                value=operatorName
            )

    def input_operate_start_date(self,startDate):
        """输入操作开始日期"""

        # 这里使用的ddt模式所以给一个参数判断日期输入，一般日期为当前日期筛选
        if startDate != "":
            self.input_message(self.get_elements("operate_start_date_input"),startDate)

    def input_operate_end_date(self,endDate):
        """输入操作结束日期"""
        if endDate != "":
            self.input_message(self.get_elements("operate_end_date_input"),endDate)

    def input_spare_part_number(self,sparePartNumber):
        """输入备件条码"""
        self.input_message(self.get_elements("spare_part_number_input"),sparePartNumber)

    def input_spare_part_name(self,sparePartName):
        """输入备件名称"""
        self.input_message(self.get_elements("spare_part_name_input"),sparePartName)

    def select_IO_inventory_type(self,inventoryType):
        """选择出入库类型"""

        if inventoryType != "":
            self.operate_not_select(
                open_el=self.get_elements("open_IO_inventory_btn"),
                parent_el=self.get_elements("IO_inventory_parent_element"),
                value=inventoryType
            )

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def get_first_log_info(self):
        """获取第一行日志记录信息"""
        return self.get_text(self.get_elements("first_adjust_log_info"))