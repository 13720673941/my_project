# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 11:50

from public.page.brandsPage import BasePage
from config.urlConfig import *

class OrderLogPage(BasePage):

    """网点单量记录页面"""

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中工单日志页面的元素信息"""
        return read_config_data("order_log_page",option,elementDataPath)

    def enter_order_log_page(self):
        """进入单量扣除日志页面"""
        self.open_url(order_log_list_url,self.get_elements("start_date_input"))

    def input_start_date(self,start_date):
        """输入开始开始的日期"""
        self.input_message(self.get_elements("start_date_input"),start_date)

    def input_end_date(self,end_date):
        """输入结束日期"""
        self.input_message(self.get_elements("end_date_input"),end_date)

    def select_deduct_type(self,value):
        """选择扣除类型筛选"""
        self.operate_not_select(
            open_el=self.get_elements("open_down_list"),
            parent_el=self.get_elements("type_select_parent_path"),
            value=value)

    def input_order_number(self,order_number):
        """输入工单编号"""
        self.input_message(self.get_elements("order_number_input"),order_number)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def get_first_row_info(self):
        """获取日志记录第一行的信息"""
        return self.get_text(self.get_elements("first_row_info"))

    def get_order_count(self):
        """获取网点工单余量"""
        return self.get_text(self.get_elements("order_count"))

    def get_short_msg_count(self):
        """获取网点短信余量"""
        return self.get_text(self.get_elements("message_count"))