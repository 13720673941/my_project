# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 11:50

from public.page.brandsPage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class OrderLogPage(BasePage):

    """网点单量记录页面"""

    # 搜索开始日期输入框
    start_date_input = (By.XPATH,'//input[@placeholder="选择开始日期"]')
    # 搜索结束日期输入框
    end_date_input = (By.XPATH,'//input[@placeholder="选择结束日期"]')
    # 打开类型下拉按钮
    open_down_list = (By.XPATH,'//label[contains(text(),"类型")]/..//div[1]')
    # 扣除类型搜索父路径
    type_select_parent_path = (By.XPATH,'//label[contains(text(),"类型")]/..//ul[2]')
    # 工单编号输入框
    order_number_input = (By.XPATH,'//label[contains(text(),"编号")]/..//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 第一行日志记录的信息
    first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 首页工单余量
    order_count = (By.XPATH,'//div[contains(text(),"工单余量")]/span')
    # 首页短信余量
    message_count = (By.XPATH,'//div[contains(text(),"短信余量")]/span')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_order_log_page(self):
        """进入单量扣除日志页面"""
        self.open_url(master_order_number_url)

    def input_start_date(self,start_date):
        """输入开始开始的日期"""
        self.input_message(self.start_date_input,start_date)

    def input_end_date(self,end_date):
        """输入结束日期"""
        self.input_message(self.end_date_input,end_date)

    def select_deduct_type(self,value):
        """选择扣除类型筛选"""
        self.operate_not_select(open_el=self.open_down_list,
                                parent_el=self.type_select_parent_path,
                                value=value)

    def input_order_number(self,order_number):
        """输入工单编号"""
        self.input_message(self.order_number_input,order_number)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def get_first_row_info(self):
        """获取日志记录第一行的信息"""
        return self.get_text(self.first_row_info)

    def get_order_count(self):
        """获取网点工单余量"""
        return self.get_text(self.order_count)

    def get_short_msg_count(self):
        """获取网点短信余量"""
        return self.get_text(self.message_count)