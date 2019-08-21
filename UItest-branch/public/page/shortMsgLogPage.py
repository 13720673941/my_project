# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/21 11:53

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class ShortMsgLogPage(BasePage):

    """
    短信发送记录页面
    """

    # 工单编号输入框
    order_number_input = (By.XPATH,'//label[text()="工单编号："]/../input')
    # 短信类型选择框按钮
    short_msg_type_btn = (By.XPATH,'//label[text()="短信类型："]/../div/div[1]')
    # 短信类型选择父元素路径
    msg_type_parent_path = (By.XPATH,'//label[text()="短信类型："]/../div/div[2]/ul[2]')
    # 手机号输入框
    phe_num_input = (By.XPATH,'//label[text()="手机号："]/../input')
    # 发送开始时间输入框
    send_start_time_input = (By.XPATH,'//input[@placeholder="选择开始日期"]')
    # 发送结束时间输入框
    send_end_time_input = (By.XPATH,'//input[@placeholder="选择结束日期"]')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_short_msg_list_page(self):
        """进入发送短信记录的页面"""
        self.open_url(short_msg_log_url)

    def  input_order_number(self,order_number):
        """输入工单编号"""
        self.input_message(self.order_number_input,order_number)

    def select_short_msg_type(self,value):
        """发送短信类型信息"""
        self.operate_not_select(open_el=self.short_msg_type_btn,
                                parent_el=self.msg_type_parent_path,
                                value=value)

    def input_phe_number(self,phone_number):
        """输入工单编号"""
        self.input_message(self.phe_num_input,phone_number)

    def input_send_start_time(self,send_start_time):
        """输入发送开始时间"""
        self.input_message(self.send_start_time_input,send_start_time)

    def input_send_end_time(self,send_end_time):
        """输入发送结束时间"""
        self.input_message(self.send_end_time_input,send_end_time)

    def click_search_btn(self):
        """"点击搜索按钮"""
        self.click_button(self.search_btn)