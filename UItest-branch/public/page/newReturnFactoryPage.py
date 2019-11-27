# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/16 19:07

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By

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

    def