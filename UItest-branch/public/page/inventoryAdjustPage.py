# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/12 15:37

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class InventoryAdjust(BasePage):
    """
    【备件管理】-【库存调整】页面、库存调整功能
    """
    # 库存调整按钮
    inventory_adjust_btn = (By.XPATH,'//tr[@class="ivu-table-row"]//td[3]//a[3]')
    # 调整备件数量输入框
    adjust_number_input = (By.XPATH,'//input[@class="number-input"]')
    # 调整原因输入框
    adjust_reason_input = (By.XPATH,'//label[contains(text(),"调整原因")]/..//textarea')
    # 调整库存确定按钮
    confirm_adjust_btn = (By.XPATH,'//div[contains(text(),"调整库存")]/../..//button[2]')
    # 备件总库存数量信息
    all_inventory_number = (By.XPATH,'//tr[@class="ivu-table-row"]//td[10]//span')
    # 操作人筛选打开按钮
    open_operator_btn = (By.XPATH,'//label[contains(text(),"操作人")]/../div')
    # 操作人父节点元素
    operator_parent_element = (By.XPATH,'//label[contains(text(),"操作人")]/..//ul[2]')
    # 操作开始时间输入框
    operate_start_date_input = (By.XPATH,'//label[contains(text(),"操作时间")]/../div[1]//input')
    # 操作结束时间输入框
    operate_end_date_input = (By.XPATH,'//label[contains(text(),"操作时间")]/../div[2]//input')
    # 备件条码输入框
    spare_part_number_input = (By.XPATH,'//label[contains(text(),"备件条码")]/..//input')
    # 备件名称输入框
    spare_part_name_input = (By.XPATH,'//label[contains(text(),"备件名称")]/..//input')
    # 出入库类型打开下拉按钮
    open_IO_inventory_btn = (By.XPATH,'//label[contains(text(),"出入库类型")]/../div')
    # 出入库类型父节点元素
    IO_inventory_parent_element = (By.XPATH,'//label[contains(text(),"出入库类型")]/..//ul[2]')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 第一行全部数据
    first_log_info = (By.XPATH,'(//tr[@class="ivu-table-row"])[1]')


    def enter_inventory_adjust_log_page(self):
        """进入库存调整页面"""
        self.open_url(inventory_adjust_url)

    def click_inventory_adjust(self):
        """点击库存调整"""
        self.click_button(self.inventory_adjust_btn)

    def input_after_adjust_inventory(self,after_adjust_number):
        """输入调整后的备件库存数量"""
        self.clear_input(self.adjust_number_input)
        self.sleep(1)
        self.input_message(self.adjust_number_input,after_adjust_number)

    def input_adjust_reason(self,adjust_reason):
        """输入调整库存备注信息"""
        self.input_message(self.adjust_reason_input,adjust_reason)

    def click_confirm_adjust(self):
        """点击保存确定调整"""
        self.click_button(self.confirm_adjust_btn)

    def get_all_inventory_count(self):
        """获取总库存数量"""
        return self.get_text(self.all_inventory_number)

    def select_operator_name(self,operator_name):
        """选择操作人"""
        if operator_name != "":
            self.operate_not_select(
                open_el=self.open_operator_btn,
                parent_el=self.operator_parent_element,
                value=operator_name
            )

    def input_operate_start_date(self,start_date):
        """输入操作开始日期"""

        # 这里使用的ddt模式所以给一个参数判断日期输入，一般日期为当前日期筛选
        if start_date == "True":
            self.input_message(self.operate_start_date_input,self.get_now_time())

    def input_operate_end_date(self,end_date):
        """输入操作结束日期"""
        if end_date == "True":
            self.input_message(self.operate_end_date_input,self.get_now_time())

    def input_spare_part_number(self,spare_part_number):
        """输入备件条码"""
        self.input_message(self.spare_part_number_input,spare_part_number)

    def input_spare_part_name(self,spare_part_name):
        """输入备件名称"""
        self.input_message(self.spare_part_name_input, spare_part_name)

    def select_IO_inventory_type(self,inventory_type):
        """选择出入库类型"""

        if inventory_type != "":

            self.operate_not_select(
                open_el=self.open_IO_inventory_btn,
                parent_el=self.IO_inventory_parent_element,
                value=inventory_type
            )

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def get_first_log_info(self):
        """获取第一行日志记录信息"""
        return self.get_text(self.first_log_info)