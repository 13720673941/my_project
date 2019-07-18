# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 17:16

from selenium.webdriver.common.by import By
from config.urlconfig import *
from public.common.basepage import BasePage
"""
客户统计页面
"""
class ManageStatisticsPage(BasePage):

    """经销商订单统计页面数据获取元素"""

    # 客户名称手机号搜索输入框
    customer_search_input = (By.XPATH,'//label[text()="客户名称/手机号："]/..//input')
    # 下单开始时间输入框
    create_order_start_time = (By.XPATH,'//label[text()="下单时间："]/../div[1]/.//input')
    # 下单结束时间输入框
    create_order_end_time = (By.XPATH,'//label[text()="下单时间："]/../div[2]/.//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 已结单订单数量::第一个经销商的数据必须搜索才能使用
    already_to_settle = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[3]//span')
    # 已完单订单数量
    already_to_finish = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[4]//span')
    # 未完单订单数量
    not_finish_order = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[5]//span')
    # 差评单订单数量
    negative_comment_order = (By.XPATH,'//tr[@class="ivu-table-row"][1]/td[6]//span')
    # 客户名称
    customer_first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_statistics_page(self):
        """进入经销商工单统计页面"""
        self.open_url(customer_statistics_url)

    def input_customer_search_keyword(self,keyword):
        """输入客户搜索关键词"""
        self.input_message(self.customer_search_input,keyword)

    def input_start_date(self,start_date):
        """输入开始时间"""
        self.input_message(self.create_order_start_time,start_date)

    def input_end_date(self,end_date):
        """输入结束时间"""
        self.input_message(self.create_order_end_time,end_date)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def get_already_settle_count(self):
        """获取已结单单数"""
        return self.get_text(self.already_to_settle)

    def get_already_finish_count(self):
        """获取已完成订单数量"""
        return self.get_text(self.already_to_finish)

    def get_not_finish_count(self):
        """获取未完单数量"""
        return self.get_text(self.not_finish_order)

    def get_negative_comment_count(self):
        """获取差评单数量"""
        return self.get_text(self.negative_comment_order)

    def get_after_search_customer_info(self):
        """获取客户统计列表第一行所有的信息"""
        return self.get_text(self.customer_first_row_info)
