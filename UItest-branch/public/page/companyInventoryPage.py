# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 14:07

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class CompanyInventoryPage(BasePage):

    """
    【备件管理】->【库存管理】->【公司库存】页面
    """
    # 新增备件页面xpath
    add_sparePart_xpath = '//div[text()="新增备件"]/../..'
    # 备件条码输入框
    sparePart_number_search_input = (By.XPATH,'//label[contains(text(),"备件条码")]/..//input')
    # 备件名称输入框
    sparePart_name_search_input = (By.XPATH,'//label[contains(text(),"备件名称")]/..//input')
    # 备件品牌输入框
    sparePart_brand_search_input = (By.XPATH,'//label[contains(text(),"备件品牌")]/..//input')
    # 备件类型下拉打开按钮
    sparePart_type_search_open_btn = (By.XPATH,'//label[contains(text(),"备件类型")]/../div/div[1]')
    # 备件类型选择项父路径
    sparePart_type_search_parent_xpath = (By.XPATH,'//label[contains(text(),"备件类型")]/../div/div[2]//ul[2]')
    # 适用品类下拉打开按钮
    use_for_kind_open_btn = (By.XPATH,'//label[contains(text(),"适用品类")]/../div/div[1]')
    # 适用品类选择项父路径
    use_for_kind_parent_xpath = (By.XPATH,'//label[contains(text(),"适用品类")]/../div/div[2]//ul[2]')
    # 搜索按钮
    sparePart_search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 新增备件按钮
    add_new_sparePart_btn = (By.XPATH,'//div[@class="work-operation"]//li/a')
    # 备件名称输入框
    sparePart_name_add_input = (By.XPATH,'//label[contains(text(),"备件名称")]/../div/div/input')
    # 备件类型下拉打开按钮
    sparePart_type_add_open_btn = (By.XPATH, add_sparePart_xpath+'//label[contains(text(),"备件类型")]/../div/div[1]')
    # 备件类型选择项父路径
    sparePart_type_add_parent_xpath = (By.XPATH,'//label[contains(text(),"备件类型")]/../div/div/div[2]/ul[2]')
    # 计量单位下拉打开按钮
    measuring_unit_open_btn = (By.XPATH,'//label[contains(text(),"计量单位")]/../div/div')
    # 计量单位选项父路径
    measuring_unit_parent_xpath = (By.XPATH,'//label[contains(text(),"计量单位")]/../div/div//ul[2]')
    # 新建备件条码输入框
    sparePart_number_add_input = (By.XPATH,add_sparePart_xpath+'//label[contains(text(),"备件条码")]/..//input')
    # 备件品牌输入框
    sparePart_brand_add_input = (By.XPATH,add_sparePart_xpath+'//label[contains(text(),"备件品牌")]/..//input')
    # 备件来源下拉打开按钮
    sparePart_from_open_btn = (By.XPATH,'//label[contains(text(),"备件来源")]/../div/div')
    # 备件来源下拉选项父路径
    sparePart_from_add_parent_xpath = (By.XPATH,'//label[contains(text(),"备件来源")]/../div/div//ul[2]')
    # 备件型号输入框
    sparePart_type_number_input = (By.XPATH,'//label[contains(text(),"备件型号")]/..//input')
    # 适用品类父路径
    user_kind_add_parent_xpath = (By.XPATH,'(//label[contains(text(),"适用品类")]/..//div[@class="ivu-row"])[1]')
    # 上传图片按钮
    loading_up_picture = (By.XPATH,'(//label[contains(text(),"备件图片")]/..//input)[1]')
    # 入库价格输入框
    into_store_price = (By.XPATH,'(//label[contains(text(),"入库价格")]/..//input)[1]')
    # 零售价格
    user_buy_price = (By.XPATH,'(//label[contains(text(),"零售价")]/..//input)[1]')
    # 返还旧件按钮
    old_sparePart_return = (By.XPATH,'(//label[contains(text(),"是否返还旧件")]/..//div/label[1])[1]')
    # 不返还旧件按钮
    old_sparePart_not_return = (By.XPATH,'(//label[contains(text(),"是否返还旧件")]/..//div/label[2])[1]')
    # 保存按钮
    add_save_btn = (By.XPATH,'(//button[contains(text(),"保存")])[1]')
    # 修改备件确定
    alter_save_btn = (By.XPATH,'(//button[contains(text(),"保存")])[5]')
    # 备件删除按钮
    sparePart_del_btn = (By.XPATH,'//button[contains(text(),"删除")]')
    # 确定删除备件按钮
    confirm_del_btn = (By.XPATH,'//div[contains(text(),"是否")]/../..//a[2]')
    # 搜索备件第一条选择框
    first_sparePart_select_input = (By.XPATH,'//tr[@class="ivu-table-row"][1]//input[@type="checkbox"]')
    # 修改备件信息按钮
    alter_sparePart_btn = (By.XPATH,'//tr[@class="ivu-table-row"][1]//td[3]//a[2]')
    # 修改页面输入备件名称
    alter_sparePart_name = (By.XPATH,'(//label[contains(text(),"备件名称")]/../div/div/input)[2]')
    # 第一条备件的所有信息
    first_row_all_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_company_inventory_page(self):
        """进入备件库存页面"""
        self.open_url(company_inventory_url)

    def input_search_sparePart_number(self,sparePart_number):
        """输入备件条码"""
        self.input_message(self.sparePart_number_search_input,sparePart_number)

    def input_search_sparePart_name(self,sparePart_name):
        """输入备件名称"""
        self.input_message(self.sparePart_name_search_input,sparePart_name)

    def input_search_sparePart_brand(self,sparePart_brand):
        """输入备件品牌"""
        self.input_message(self.sparePart_brand_search_input,sparePart_brand)

    def select_search_sparePart_type(self,sparePart_type):
        """选择备件类型"""
        if sparePart_type != "":
            self.operate_not_select(open_el=self.sparePart_type_search_open_btn,
                                    parent_el=self.sparePart_type_search_parent_xpath,value=sparePart_type)

    def select_search_use_for_kind(self,use_kind):
        """选择适用品类"""
        if use_kind != "":
            self.operate_not_select(open_el=self.use_for_kind_open_btn,
                                    parent_el=self.use_for_kind_parent_xpath,value=use_kind)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_button(self.sparePart_search_btn)

    def click_add_new_sparePart(self):
        """点击新增备件按钮"""
        self.click_button(self.add_new_sparePart_btn)

    def input_add_sparePart_name(self,sparePart_name):
        """输入添加的备件名称"""
        self.input_message(self.sparePart_name_add_input,sparePart_name)

    def select_add_sparePart_type(self,sparePart_type):
        """选择添加的备件类型"""
        if sparePart_type != "":
            self.operate_not_select(open_el=self.sparePart_type_add_open_btn,
                                    parent_el=self.sparePart_type_add_parent_xpath,value=sparePart_type)

    def select_measuring_unit(self,measuring_unit):
        """选择计量单位"""
        if measuring_unit != "":
            self.operate_not_select(open_el=self.measuring_unit_open_btn,
                                    parent_el=self.measuring_unit_parent_xpath,value=measuring_unit)

    def input_add_sparePart_number(self,sparePart_number):
        """输入备件条码"""
        self.input_message(self.sparePart_number_add_input,sparePart_number)

    def input_add_sparePart_brand(self,sparePart_brand):
        """输入备件品牌"""
        self.input_message(self.sparePart_brand_add_input,sparePart_brand)

    def select_sparePart_from(self,sparePart_from):
        """选择备件来源"""
        if sparePart_from != "":
            self.operate_not_select(open_el=self.sparePart_from_open_btn,
                                    parent_el=self.sparePart_from_add_parent_xpath,value=sparePart_from)

    def input_sparePart_type_number(self,type_number):
        """输入备件型号"""
        self.input_message(self.sparePart_type_number_input,type_number)

    def select_use_kind(self,is_select):
        """选择适用品类"""

        if is_select == "True":
            # 统计所有的品类个数信息
            kind_count,kind_list = self.get_element_count(parentEl=self.user_kind_add_parent_xpath,childEl='label')
            # 选择全部的适用品类信息
            for i in range(1,kind_count+1):
                self.click_button(
                    element=(By.XPATH,'(//label[contains(text(),"适用品类")]/..'
                                      '//div[@class="ivu-row"])[1]//div['+str(i)+']/label//input'))

    def operate_up_loading_picture(self,loading_up):
        """操作上传图片"""
        if loading_up == 'True':
            self.up_loading_picture(num=5,element=self.loading_up_picture)

    def input_into_inventory_price(self,into_store_price):
        """输入入库价格"""
        self.input_message(self.into_store_price,into_store_price)

    def input_user_buy_price(self,use_buy_price):
        """输入零售价格"""
        self.input_message(self.user_buy_price,use_buy_price)

    def select_old_return_btn(self):
        """选择旧件返回备件操作"""
        self.click_button(self.old_sparePart_return)

    def select_old_not_return_btn(self):
        """选择旧件不返回按钮"""
        self.click_button(self.old_sparePart_not_return)

    def click_add_save_btn(self):
        """点击保存备件按钮"""
        self.click_button(self.add_save_btn)

    def click_alter_save_btn(self):
        """点击修改保存按钮"""
        self.click_button(self.alter_save_btn)

    def select_first_sparePart(self):
        """选择第一条备件"""
        self.click_button(self.first_sparePart_select_input)

    def click_del_sparePart_btn(self):
        """点击删除备件按钮"""
        self.click_button(self.sparePart_del_btn)

    def click_confirm_del_btn(self):
        """点击确定删除备件"""
        self.click_button(self.confirm_del_btn)

    def click_alter_button(self):
        """点击修改备件按钮"""
        self.click_button(self.alter_sparePart_btn)

    def input_alter_sparePart_name(self,sparePart_name):
        """输入修改备件名称"""

        # 清空备件名称
        self.clear_input(self.alter_sparePart_name)
        # 输入新备件名称
        self.input_message(self.alter_sparePart_name,sparePart_name)

    def get_first_row_info(self):
        """获取第一行备件所有信息"""
        return self.get_text(self.first_row_all_info)
