# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 11:37

from selenium.webdriver.common.by import By
from config.urlconfig import *
from public.page.brandsPage import BasePage

class TeamWorkNewsPage(BasePage):
    """
    合作申请页面: 收到的申请/发出的申请
    """

    # 切换发出申请的table
    table_btn = (By.XPATH,'//a[contains(text(),"发出的申请")]')
    # 客户搜索输入框
    customer_search_input = (By.XPATH,'//input[starts-with(@placeholder,"输入客户名称")]')
    # 点击搜索
    search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 第一行所有的字段信息
    first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 接收端网点拒绝成为服务商申请
    refuse_manage_visit = (By.XPATH,'//tr[@class="ivu-table-row"][1]//a[contains(text(),"拒绝")]')
    # 确定拒绝申请合作
    confirm_refuse_btn = (By.XPATH,'//div[contains(text(),"是否")]/..//a[2]')
    # 发出的申请中的已拒绝字段-我方
    my_refuse_text = (By.XPATH,'//tr[@class="ivu-table-row"][1]//td[6]/div/div')
    # 发出的申请中的已拒绝字段-他方
    it_refuse_text = (By.XPATH, '//tr[@class="ivu-table-row"][1]//td[6]/div/div')
    # 发出端网点撤销服务商申请
    del_teamwork_btn1 = (By.XPATH,'//tr[@class="ivu-table-row"][1]//td[7]//a')
    del_teamwork_btn2 = (By.XPATH,'//tr[@class="ivu-table-row"][1]//td[7]//a')
    # 再次邀请
    again_to_visit = (By.XPATH,'//tr[@class="ivu-table-row"][1]//td[7]//a')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_teamwork_news_page(self):
        """进入申请消息页面"""
        self.open_url(teamwork_news_list_url)

    def click_table_send_visit(self):
        """点击切换发出的申请"""
        self.click_button(self.table_btn)

    def input_customer_name_phone(self,search_word):
        """输入客户名称或者手机号"""
        self.input_message(self.customer_search_input,search_word)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def get_first_row_info(self):
        """获取第一行搜索的所有字段信息"""
        return self.get_text(self.first_row_info)

    def click_refuse_btn(self):
        """点击拒绝按钮"""
        self.click_button(self.refuse_manage_visit)

    def click_confirm_refuse(self):
        """点击确定拒绝邀请"""
        self.click_button(self.confirm_refuse_btn)

    def get_refuse_my_text(self):
        """获取已拒绝字段-我方"""
        return self.get_text(self.my_refuse_text)

    def get_refuse_it_text(self):
        """获取已拒绝字段-他方"""
        return self.get_text(self.it_refuse_text)

    def click_del_teamwork_visit(self):
        """点击撤销所有的邀请"""
        self.click_button(self.del_teamwork_btn1)
        self.click_confirm_refuse()
        self.sleep(1)
        self.click_button(self.del_teamwork_btn2)
        self.click_confirm_refuse()

    def click_again_visit_teamwork(self):
        """点击再次邀请"""
        self.click_button(self.again_to_visit)