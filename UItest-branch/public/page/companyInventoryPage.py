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
    sparePart_type_add_parent_xpath = (By.XPATH, '//label[contains(text(),"备件类型")]/../div/div[2]//ul[2]')
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
    # 备件删除按钮
    sparePart_del_btn = (By.XPATH,'//button[contains(text(),"删除")]')
    # 搜索备件第一条选择框
    first_sparePart_select_input = (By.XPATH,'//tr[@class="ivu-table-row"][1]//input[@type="checkbox"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_company_inventory_page(self):
        """进入备件库存页面"""
        self.open_url(company_inventory_url)

    def input_sparePart_number(self,sparePart_number):
        """输入备件条码"""
        self.input_message(self.sparePart_number_search_input,sparePart_number)

    def input_sparePart_name(self,sparePart_name):
        """输入备件名称"""
        self.input_message(self.sparePart_name_search_input,sparePart_name)

    def input_sparePart_brand(self,sparePart_brand):
        """输入备件品牌"""
        self.input_message(self.sparePart_brand_search_input,sparePart_brand)

    def select_sparePart_type(self,sparePart_type):
        """选择备件类型"""
        self.operate_not_select(open_el=self.sparePart_type_search_open_btn,
                                parent_el=self.sparePart_type_search_parent_xpath,value=sparePart_type)

    def select_use_for_kind(self,use_kind):
        """选择适用品类"""
        self.operate_not_select(open_el=self.use_for_kind_open_btn,
                                parent_el=self.use_for_kind_parent_xpath,value=use_kind)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_button(self.sparePart_search_btn)

    def click_add_new_sparePart(self):
        """点击新增备件按钮"""
        self.click_button(self.add_new_sparePart_btn)