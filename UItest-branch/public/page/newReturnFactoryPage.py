# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/16 19:07

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class NewReturnFactoryPage(BasePage):

    """
    【备件管理】-【新件返还】
    """

    # 新件返厂按钮
    new_parts_return_btn = (By.XPATH,'//button[contains(text(),"新件返厂")]')
    # 新件返厂数量输入框
    parts_count_input = (By.XPATH,'//label[contains(text(),"返厂数量")]/..//input')
    # 保存按钮
    save_new_parts_return = (By.XPATH,'//div[contains(text(),"新件返厂")]/../../div[3]//button[2]')
    # 批量返厂按钮
    batch_return_factory_btn = (By.XPATH,'//button[contains(text(),"批量返厂")]')
    # 批量勾选按钮
    batch_select_input = (By.XPATH,'(//input[@type="checkbox"])[1]')
    # 输入批量返厂备注
    remark_input = (By.XPATH,'//label[contains(text(),"返厂备注")]/..//textarea')
    # 保存备注按钮
    save_remark_btn = (By.XPATH,'//div[contains(text(),"备件返厂")]/../../div[3]//button[2]')
    # 确认返厂按钮
    confirm_return_factory_btn = (By.XPATH,'(//tr[@class="ivu-table-row"])[1]/td[3]//a')
    # 待返厂第一条信息
    first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')

    def enter_wait_return_page(self):
        """进入待返厂备件页面"""
        self.open_url(wait_return_factory_url)

    def enter_already_return_page(self):
        """进入已返厂备件页面"""
        self.open_url(already_return_faction_url)

    def click_new_sp_return(self):
        """点击新件返厂"""
        self.click_button(self.new_parts_return_btn)

    def input_return_count(self,sp_count):
        """输入返厂备件数量"""
        self.input_message(self.parts_count_input,sp_count)

    def get_count_number(self):
        """获取输入的最大返厂数量"""
        return self.get_att(self.parts_count_input,"value")

    def click_save_return(self):
        """点击确定返厂"""
        self.click_button(self.save_new_parts_return)

    def select_all_return_sp(self):
        """批量返厂选择全部备件"""
        self.click_button(self.batch_select_input)

    def click_batch_return_btn(self):
        """点击批量返厂按钮"""
        self.click_button(self.batch_return_factory_btn)

    def input_batch_return_remark(self,return_remark):
        """输入批量返厂备注"""
        self.input_message(self.remark_input,return_remark)

    def click_confirm_batch_return(self):
        """点击确认批量返厂"""
        self.click_button(self.save_remark_btn)

    def click_confirm_return_btn(self):
        """点击确认返厂按钮"""
        self.click_button(self.confirm_return_factory_btn)

    def get_first_row_log_info(self):
        """获取待返厂第一条全部的信息"""
        return self.get_text(self.first_row_info)

