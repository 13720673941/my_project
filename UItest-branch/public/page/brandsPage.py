# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/12 19:03

from public.common.basePage import BasePage
from config.urlConfig import *

class BrandsPage(BasePage):

    """
        【厂商系统添加页面】 添加厂商账号、删除厂商账号
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取页面元素文本"""
        return read_config_data("brands_page",option,elementDataPath)

    def enter_customer_list_page(self):
        """进入客户列表页面"""
        self.open_url(teamwork_branch_list_url,self.get_elements("brands_table_btn"))

    def click_brands_table_btn(self):
        """点击切换厂商的table按钮"""
        self.click_button(self.get_elements("brands_table_btn"))

    def click_add_brands_account(self):
        """点击添加系统厂商账号"""
        self.click_button(self.get_elements("add_brands_btn"))

    def open_brands_system_select(self):
        """打开选择下拉"""
        self.click_button(self.get_elements("open_brands_select"))

    def select_brands_system(self,brandsName):
        """选择下拉厂商系统文本"""
        open_select = self.get_elements("open_brands_select")
        parent_select = self.get_elements("parent_brands_select")
        if brandsName != '':
            self.operate_not_select(open_select,parent_select,value=brandsName)

    def input_login_username(self,brandsUsername):
        """输入登录用户名"""
        self.input_message(self.get_elements("login_use_input"),brandsUsername)

    def input_login_password(self,brandsPassword):
        """输入登录密码"""
        self.input_message(self.get_elements("login_pwd_input"),brandsPassword)

    def click_confirm_add_brands(self):
        """点击确定添加厂商账号"""
        self.click_button(self.get_elements("confirm_add_btn"))

    def click_edit_brands_btn(self,editBrandName):
        """点击编辑厂商账号"""

        # 获取品牌商列表父元素文本
        parent_of_brands_list = self.get_elements("parent_brands_count")
        # 品牌商列表中品牌商名称元素
        brands_name_in_list = self.get_elements("brands_name_in_list")
        # 统计所有的厂商账号个数
        brand_count,brand_el_list = self.get_element_count(parent_of_brands_list,"tr")
        # 循环遍历系统名称
        for i in range(1,brand_count+1):
            try:
                brandName = self.get_text(brands_name_in_list.raplace("+num+",str(i)))
                if brandName == editBrandName:
                    self.click_button(self.get_elements("edit_btn").replace("+num+",str(i)))
                    break
            except:
                if i == brand_count:
                    raise TimeoutError("Not find brand name: {} in list !".format(editBrandName))
                else:
                    continue

    def click_delete_brands(self,delBrandName):
        """删除厂商账号"""

        # 获取品牌商列表父元素文本
        parent_of_brands_list = self.get_elements("parent_brands_count")
        # 品牌商列表中品牌商名称元素
        brands_name_in_list = self.get_elements("brands_name_in_list")
        # 统计所有的厂商账号个数
        brand_count,brand_el_list = self.get_element_count(parent_of_brands_list,"tr")
        # 循环遍历系统名称
        for i in range(1,brand_count+1):
            try:
                brandName = self.get_text(brands_name_in_list.raplace("+num+",str(i)))
                if brandName == delBrandName:
                    self.click_button(self.get_elements("delete_btn").replace("+num+",str(i)))
                    break
            except:
                if i == brand_count:
                    raise TimeoutError("Not find brand name: {} in list !".format(delBrandName))
                else:
                    continue

    def click_confirm_del_brands(self):
        """确认删除厂商按钮"""
        self.click_button(self.get_elements("confirm_del_brands"))