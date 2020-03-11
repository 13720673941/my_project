# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 10:01

from public.common.basePage import BasePage
from config.urlConfig import *

class MasterStatisticsPage(BasePage):

    """师傅工单统计页面"""

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取页面元素文本"""
        return read_config_data("master_order_statistics",option,elementDataPath)

    def enter_master_order_statistics_page(self):
        """进入师傅工单统计列表页"""
        self.open_url(master_order_statistics_url,self.get_elements("master_search_input"))

    def input_master_keyword_search(self,search_word):
        """输入师傅关键字搜索"""
        self.input_message(self.get_elements("master_search_input"),search_word)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.sleep(2)
        self.click_button(self.get_elements("master_search_btn"))

    def get_list_first_row_info(self):
        """获取列表第一行数据"""
        return self.get_text(self.get_elements("master_first_row_info"))

    def get_master_take_order_count(self):
        """获取师傅结单数量"""
        return self.get_text(self.get_elements("master_take_order_count"))

    def get_master_finished_count(self):
        """获取师傅已完单数量"""
        return self.get_text(self.get_elements("master_finish_order_count"))

    def get_master_not_finished_count(self):
        """获取师傅未完单数量"""
        return self.get_text(self.get_elements("master_not_finish_order_count"))

    def get_master_wait_settle_count(self):
        """获取师傅待结算订单数量"""
        return self.get_text(self.get_elements("master_wait_settle_count"))

    def get_master_good_talk_count(self):
        """获取师傅好评单数量"""
        return self.get_text(self.get_elements("master_good_talk_count"))

    def get_master_already_settle_count(self):
        """获取师傅已结算订单数量"""
        return self.get_text(self.get_elements("master_already_settle_count"))

    def get_master_favorable_rate_count(self):
        """获取师傅好评率"""
        return self.get_text(self.get_elements("master_favorable_rate_count"))