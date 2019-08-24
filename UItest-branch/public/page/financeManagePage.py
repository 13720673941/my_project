# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/22 16:30

from public.page.brandsPage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class FinanceManagePage(BasePage):

    """
    我的收入和支出页面
    """
    # 打开下拉收入类型按钮
    open_income_type_btn = (By.XPATH,'//label[text()="收入类型："]/../div/div')
    # 收入类型选项父节点
    income_type_parent_xpath = (By.XPATH,'//label[text()="收入类型："]/..//ul[2]')
    # 打开下拉支出类型按钮
    open_expend_type_btn = (By.XPATH,'//label[text()="支出类型："]/../div/div')
    # 支出类型选项父节点
    expend_type_parent_xpath = (By.XPATH, '//label[text()="支出类型："]/..//ul[2]')
    # 打开服务类型下拉按钮
    open_server_type_btn = (By.XPATH,'//label[text()="服务类型："]/../div/div')
    # 服务类型选项父节点
    server_type_parent_xpath = (By.XPATH,'//label[text()="服务类型："]/..//ul[2]')
    # 服务师傅输入框
    server_master_input = (By.XPATH,'//label[text()="服务师傅："]/..//input')
    # 工单编号输入框
    order_number_input = (By.XPATH,'//label[text()="工单编号："]/..//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 结算时间开始日期
    settle_start_time = (By.XPATH,'//label[contains(text(),"结算时间")]/../div/div[1]//input')
    # 结算时间结束日期
    settle_end_time = (By.XPATH,'//label[contains(text(),"结算时间")]/../div/div[2]//input')
    # 查询按钮
    find_btn = (By.XPATH,'//a[contains(text(),"查询")]')
    # 收入列表第一行全部信息
    income_first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 支出列表第一行全部信息
    expend_first_row_info = (By.XPATH,'//label[text()="支出类型："]/../../../div/div[2]'
                                      '//tr[@class="ivu-table-row"][1]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_my_income_page(self):
        """进入我的收入页面"""
        self.open_url(my_income_url)

    def enter_my_expend_page(self):
        """进入我的支出页面"""
        self.open_url(my_expend_url)

    def select_income_type(self,income_type):
        """选择收入类型"""
        self.operate_not_select(
            open_el=self.open_income_type_btn,parent_el=self.income_type_parent_xpath,value=income_type)

    def select_expend_type(self,expend_type):
        """选择支出类型"""
        self.operate_not_select(
            open_el=self.open_expend_type_btn,parent_el=self.expend_type_parent_xpath,value=expend_type)

    def select_server_type(self,server_type):
        """选择服务类型"""
        self.operate_not_select(
            open_el=self.open_server_type_btn,parent_el=self.server_type_parent_xpath,value=server_type)

    def input_server_master_name(self,master_name):
        """输入师傅名称"""
        self.input_message(self.server_master_input,master_name)

    def input_order_number(self,order_number):
        """输入工单编号"""
        self.input_message(self.order_number_input,order_number)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def input_settle_start_time(self,start_time):
        """输入结算开始时间"""
        self.input_message(self.settle_start_time,start_time)

    def input_settle_end_time(self,end_time):
        """输入结算结束时间"""
        self.input_message(self.settle_end_time,end_time)

    def click_find_btn(self):
        """点击查询按钮"""
        self.click_button(self.find_btn)

    def get_income_first_row_info(self):
        """我的收入列表第一行全部信息"""
        return self.get_text(self.income_first_row_info)

    def get_expend_first_row_info(self):
        """我的支出列表第一行全部信息"""
        return self.get_text(self.expend_first_row_info)