# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/21 11:53

from public.common.basePage import BasePage
from config.urlConfig import *

class ShortMsgLogPage(BasePage):

    """短信发送记录页面"""

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中短信日志记录页面的元素信息"""
        return read_config_data("short_msg_log_page",option,elementDataPath)

    def get_short_msg_count(self):
        """获取首页短信余量总数"""
        return self.get_text(self.get_elements("short_msg_count"))

    def enter_short_msg_list_page(self):
        """进入发送短信记录的页面"""
        self.open_url(short_msg_log_url,self.get_elements("short_msg_type_btn"))

    def  input_order_number(self,order_number):
        """输入工单编号"""
        self.input_message(self.get_elements("short_msg_type_btn"),order_number)

    def select_short_msg_type(self,value):
        """发送短信类型信息"""
        self.operate_not_select(
            open_el=self.get_elements("short_msg_type_btn"),
            parent_el=self.get_elements("msg_type_parent_path"),
            value=value
        )

    def input_phe_number(self,phone_number):
        """输入工单编号"""
        self.input_message(self.get_elements("phe_num_input"),phone_number)

    def input_send_start_time(self,send_start_time):
        """输入发送开始时间"""
        self.input_message(self.get_elements("send_start_time_input"),send_start_time)

    def input_send_end_time(self,send_end_time):
        """输入发送结束时间"""
        self.input_message(self.get_elements("send_end_time_input"),send_end_time)

    def click_search_btn(self):
        """"点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def get_first_row_info(self):
        """获取第一行所有信息"""
        return self.get_text(self.get_elements("first_row_info"))