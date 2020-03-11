# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 17:16

from public.common.basePage import BasePage
from config.urlConfig import *

class BranchStatisticsPage(BasePage):

    """
        【客户统计页面: 经销商/服务商订单统计页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取模块页面元素位置文本"""
        return read_config_data("branch_statistics_page",option,elementDataPath)

    def enter_statistics_page(self):
        """进入经销商工单统计页面"""
        self.open_url(customer_statistics_url)

    def click_table_to_server(self):
        """点击table按钮切换服务商"""
        self.click_button(self.get_elements("server_table_btn"))

    def input_customer_search_keyword(self,keyword):
        """输入客户搜索关键词"""
        self.sleep(2)
        self.input_message(self.get_elements("customer_search_input"),keyword)

    def input_start_date(self,startDate):
        """输入开始时间"""
        self.input_message(self.get_elements("create_order_start_time"),startDate)

    def input_end_date(self,endDate):
        """输入结束时间"""
        self.input_message(self.get_elements("create_order_end_time"),endDate)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.sleep(2)
        for i in range(1,4):
            try:
                self.click_button(self.get_elements("search_btn").replace("+num+",str(i)))
                self.click_button(self.get_elements("search_btn").replace("+num+",str(i)))
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find search button in page !")
                else:
                    continue

    def get_already_settle_count(self):
        """获取已结单单数"""
        return self.get_text(self.get_elements("already_to_settle"))

    def get_already_finish_count(self):
        """获取已完成订单数量"""
        return self.get_text(self.get_elements("already_to_finish"))

    def get_not_finish_count(self):
        """获取未完单数量"""
        return self.get_text(self.get_elements("not_finish_order"))

    def get_negative_comment_count(self):
        """获取差评单数量"""
        return self.get_text(self.get_elements("negative_comment_order"))

    def get_wait_settle_count(self):
        """待结算单量统计数量"""
        return self.get_text(self.get_elements("wait_settle_order"))

    def get_after_search_customer_info(self):
        """获取客户统计列表第一行所有的信息"""
        return self.get_text(self.get_elements("customer_first_row_info"))
