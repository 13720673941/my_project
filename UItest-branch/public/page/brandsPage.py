# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/12 19:03

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *
"""
厂商系统添加页面
"""
class BrandsPage(BasePage):

    """厂商系统账号列表页面元素"""

    # 厂商系统table按钮
    brands_table_btn = (By.XPATH,'//a[text()="签约厂商系统"]')
    # 添加厂商账号按钮
    add_brands_btn = (By.XPATH,'//a[text()="添加厂商系统账号"]')
    # 打开厂商系统选择框
    open_brands_select = (By.XPATH,'//label[text()="厂商系统"]/.././/span[@class="ivu-select-placeholder"]')
    # 厂商系统选择父元素节点
    parent_brands_select = (By.XPATH,'//label[text()="厂商系统"]/.././/ul[@class="ivu-select-dropdown-list"]')
    # 厂商名称输入框
    brands_name_input = (By.XPATH,'//label[text()="厂商名称"]/.././/input')
    # 厂商地址输入框
    brands_address_input = (By.XPATH,'//label[text()="厂商地址"]/.././/input')
    # 登录账号输入框
    login_use_input = (By.XPATH,'//label[text()="登录账号"]/.././/input')
    # 登录密码输入框
    login_pwd_input = (By.XPATH, '//label[text()="登录密码"]/.././/input')
    # 确定添加厂商账号按钮
    confirm_add_btn = (By.XPATH,'//div[contains(text(),"系统账号")]/../.././/button[2]')
    # 统计所有厂商账号的父路径
    parent_brands_count = (By.XPATH,'//a[text()="添加厂商系统账号"]/../../..//tbody')
    # 编辑按钮
    # edit_btn = (By.XPATH,'(//a[text()="编辑"])')
    # 删除按钮
    # delete_btn = (By.XPATH,'(//a[text()="删除"])')
    # 确认删除按钮
    confirm_del_brands = (By.XPATH,'//div[contains(text(),"确认删除")]/..//a[2]')


    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_customer_list_page(self):
        """进入客户列表页面"""
        self.open_url(teamwork_branch_list_url)

    def click_brands_table_btn(self):
        """点击切换厂商的table按钮"""
        self.click_button(self.brands_table_btn)

    def click_add_brands_account(self):
        """点击添加系统厂商账号"""
        self.click_button(self.add_brands_btn)

    def open_brands_system_select(self):
        """打开选择下拉"""
        self.click_button(self.open_brands_select)

    def select_brands_system(self,brands_name):
        """选择下拉的文本"""
        if brands_name != '':
            self.operate_not_select(open_el=self.open_brands_select,
                                    parent_el=self.parent_brands_select,
                                    value=brands_name)

    def input_login_username(self,brands_username):
        """输入登录用户名"""
        self.input_message(self.login_use_input,brands_username)

    def input_login_password(self,brands_password):
        """输入登录密码"""
        self.input_message(self.login_pwd_input,brands_password)

    def click_confirm_add_brands(self):
        """点击确定添加厂商账号"""
        self.click_button(self.confirm_add_btn)

    def click_edit_account_btn(self,edit_brand_name):
        """点击编辑厂商账号"""

        # 统计所有的厂商账号个数
        brand_count,brand_el_list = self.get_element_count(self.parent_brands_count,"tr")
        # 循环遍历系统名称
        for i in range(1,brand_count+1):
            try:
                brand_name = self.get_text(element=(By.XPATH,'//a[text()="添加厂商系统账号"]/../../..'
                                                             '//tbody/tr['+str(i)+']/td[2]'))
                if brand_name == edit_brand_name:
                    self.click_button(element=(By.XPATH,'(//a[text()="编辑"])['+str(i)+']'))
                    break
            except Exception as e:
                raise e

    def click_delete_brands(self,del_brand_name):
        """删除厂商账号"""

        # 统计所有的厂商账号个数
        brand_count, brand_el_list = self.get_element_count(self.parent_brands_count,"tr")
        # 循环遍历系统名称
        for i in range(1,brand_count+1):
            try:
                brand_name = self.get_text(element=(By.XPATH,'//a[text()="添加厂商系统账号"]/../../..'
                                                             '//tbody/tr['+str(i)+']/td[2]'))
                if brand_name == del_brand_name:
                    self.click_button(element=(By.XPATH,'(//a[text()="删除"])['+str(i)+']'))
                    break
            except Exception as e:
                raise e

    def click_confirm_del_brands(self):

        """确认删除厂商按钮"""
        self.click_button(self.confirm_del_brands)