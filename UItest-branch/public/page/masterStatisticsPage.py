# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 10:01

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class MasterStatisticsPage(BasePage):

    """师傅工单统计页面"""

    # 统计页面师傅搜索输入框
    master_search_input = (By.XPATH,'//input[starts-with(@placeholder,"")]')
    # 搜索按钮
    master_search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 师傅列表第一行数据
    master_first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 师傅已接单订单统计数量
    master_take_order_count = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[4]//span')
    # 师傅已完单数量
    master_finish_order_count = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[5]//span')
    # 师傅待结算订单数量
    master_wait_settle_count = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[6]//span')
    # 师傅未完单订单数量
    master_not_finish_order_count = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[7]//span')
    # 师傅差评单订单数量
    master_negative_order_count = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[8]//span')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_master_order_statistics_page(self):
        """进入师傅工单统计列表页"""
        self.open_url(master_order_statistics_url)

    def input_master_keyword_search(self,search_word):
        """输入师傅关键字搜索"""
        self.input_message(self.master_search_input,search_word)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.master_search_btn)

    def get_list_first_row_info(self):
        """获取列表第一行数据"""
        return self.get_text(self.master_first_row_info)

    def get_master_take_order_count(self):
        """获取师傅结单数量"""
        return self.get_text(self.master_take_order_count)

    def get_master_finished_count(self):
        """获取师傅已完单数量"""
        return self.get_text(self.master_finish_order_count)

    def get_master_not_finished_count(self):
        """获取师傅未完单数量"""
        return self.get_text(self.master_not_finish_order_count)

    def get_master_wait_settle_count(self):
        """获取师傅待结算订单数量"""
        return self.get_text(self.master_wait_settle_count)

    def get_master_negative_count(self):
        """获取师傅差评单数量"""
        return self.get_text(self.master_negative_order_count)