#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/4 11:57

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *
"""
搜索订单页面信息
"""
class SearchOrderPage(BasePage):

    """
    搜索页面元素信息
    """
    
    # 订单单号输入框
    order_num_input = (By.XPATH,'//label[text()="工单编号"]/following-sibling::input[1]')
    # 用户姓名输入框
    username_input = (By.XPATH,'//label[text()="用户姓名"]/following-sibling::input[1]')
    # 用户手机号输入框
    phe_num_input = (By.XPATH,'//label[text()="用户电话"]/following-sibling::input[1]')
    # 服务类型打开按钮
    server_type_open = (By.XPATH,'//label[text()="服务类型"]/following-sibling::div/div')
    # 服务类型选择框
    server_type_select = (By.XPATH,'//label[text()="服务类型"]/../div/div[2]/ul[2]')
    # 订单状态打开下拉按钮
    order_status_open = (By.XPATH,'//label[text()="工单状态"]/following-sibling::div/div')
    # 订单状态选择框
    order_status_select = (By.XPATH,'//label[text()="工单状态"]/../div[2]/div[2]/ul[2]')
    # 接单师傅打开按钮
    master_open = (By.XPATH,'//label[text()="服务师傅"]/following-sibling::div/div')
    # 接单师傅选择框
    master_select = (By.XPATH,'//label[text()="服务师傅"]/../div[3]/div[2]/ul[2]')
    # 第一个搜索按钮
    search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 更多搜索条件打开下拉
    more_search_btn = (By.XPATH,'//a[text()="更多"]')
    # 第一个订单信息(两部分)
    first_order_info = (By.XPATH,'//div/div[2]/table/tbody/tr[1]')
    first_order_info1 = (By.XPATH, '//div/div[2]/table/tbody/tr[1]')
    # 品牌选择框
    brands_select = (By.XPATH,'//label[text()="家电品牌"]/../select')
    # 品类选择框
    kinds_select = (By.XPATH,'//label[text()="家电品类"]/../select')
    # 产品型号输入框
    product_num_input = (By.XPATH,'//input[@placeholder="输入产品型号"]')
    # 内机条码输入框
    in_phe_num_input = (By.XPATH,'//input[@placeholder="输入内机条码"]')
    # 工单来源打开下拉
    order_from_open = (By.XPATH,'//span[text()="请选择工单来源"]')
    # 工单来源选择框
    parent_order_from = (By.XPATH,'//label[text()="工单来源"]/../div/div[2]/ul[2]')
    # 购买渠道打开下拉
    buy_place_open = (By.XPATH,'//label[text()="购买渠道"]/../div/div')
    # 购买渠道选择框
    parent_buy_place = (By.XPATH,'//span[text()="全部购买渠道"]/../../div[2]/ul[2]')
    # 下单开始日期输入框
    add_order_start_date = (By.XPATH,'//label[text()="下单日期"]/../div/div/div/input')
    # 下单结束日期输入框
    add_order_end_date = (By.XPATH,'//label[text()="下单日期"]/../div[2]/div/div/input')
    # 完成工单开始日期输入框
    finish_order_start_date = (By.XPATH,'//label[text()="完成日期"]/../div/div/div/input')
    # 完成工单结束日期输入框
    finish_order_end_date = (By.XPATH,'//label[text()="完成日期"]/../div[2]/div/div/input')
    # 更多页面的搜索按钮
    search_btn1 = (By.XPATH,'//label[text()="工单编号"]/../../../div[2]/div[9]/a')
    # 搜索订单条数
    order_count = (By.XPATH,'//span[@class="ivu-page-total"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_search_order_page(self):
        self.open_url(all_order_list_url)

    def input_order_Nnumber(self,orderNum):
        """输入工单编号"""
        self.input_message(self.order_num_input,orderNum)

    def input_username(self,username):
        """输入用户名字"""
        self.input_message(self.username_input,username)

    def input_user_phone(self,phoneNum):
        """输入用户手机号"""
        self.input_message(self.phe_num_input,phoneNum)

    def select_server_type(self,value):
        """选择服务类型"""
        if value != '':
            self.operate_not_select(self.server_type_open,self.server_type_select,value)

    def select_order_status(self,value):
        """选择工单状态"""
        if value != '':
            self.operate_not_select(self.order_status_open,self.order_status_select,value)

    def select_master(self,value):
        """选择服务师傅"""
        if value != '':
            self.operate_not_select(self.master_open,self.master_select,value)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def click_search_more(self):
        """点击搜索更多"""
        self.click_button(self.more_search_btn)

    def select_product_brand(self,value):
        """选择家电品牌"""
        if value != '':
            self.operate_select(self.brands_select,value)

    def select_product_kinds(self,value):
        """选择家电品类"""
        if value != '':
            self.operate_select(self.kinds_select,value)

    def input_product_number(self,productNum):
        """输入产品型号"""
        self.input_message(self.product_num_input,productNum)

    def input_in_pheNum(self,in_pheNum):
        """输入内机条码"""
        self.input_message(self.in_phe_num_input,in_pheNum)

    def select_order_from(self,value):
        """选择工单来源"""
        if value != '':
            self.operate_not_select(self.order_from_open,self.parent_order_from,value)

    def select_buy_place(self,value):
        """选择购买渠道"""
        if value != '':
            self.operate_not_select(self.buy_place_open,self.parent_buy_place,value)

    def input_create_start_date(self,date):
        """输入订单创建开始日期"""
        self.input_message(self.add_order_start_date,date)

    def input_create_end_date(self,date):
        """输入订单创建结束日期"""
        self.input_message(self.add_order_end_date,date)

    def input_finish_start_date(self,date):
        """输入完成订单开始日期"""
        self.input_message(self.finish_order_start_date,date)

    def input_finish_end_date(self,date):
        """输入完成订单结束日期"""
        self.input_message(self.finish_order_end_date,date)

    def click_more_search_btn(self):
        """点击更多订单搜索的搜索按钮"""
        self.click_button(self.search_btn1)

    def search_order_count(self):
        """获取搜索订单数量"""
        self.get_text(self.order_count)

    def get_first_order_info(self):
        """获取订单列表第一行订单的所有信息"""
        orderInfo = self.get_text(self.first_order_info) + self.get_text(self.first_order_info1)
        return orderInfo




