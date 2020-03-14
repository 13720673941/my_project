#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/4 11:57

from public.common.basePage import BasePage
from public.common.rwConfig import read_config_data
from config.urlConfig import *
from config.pathConfig import *

class SearchOrderPage(BasePage):
    """
        【搜索订单页面信息】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中全部订单列表搜索功能的元素信息"""
        return read_config_data("search_order_page",option,elementDataPath)

    def enter_search_order_page(self):
        self.open_url(all_order_list_url,self.get_elements("order_number_input"))

    def input_order_Nnumber(self,orderNum):
        """输入工单编号"""
        self.input_message(self.get_elements("order_number_input"),orderNum)

    def input_username(self,username):
        """输入用户名字"""
        self.input_message(self.get_elements("username_input"),username)

    def input_user_phone(self,phoneNum):
        """输入用户手机号"""
        self.input_message(self.get_elements("phe_number_input"),phoneNum)

    def select_server_type(self,value):
        """选择服务类型"""
        if value != '':
            self.operate_not_select(
                self.get_elements("server_type_open"),self.get_elements("server_type_select"),value)

    def select_order_status(self,value):
        """选择工单状态"""
        if value != '':
            self.operate_not_select(
                self.get_elements("order_status_open"),self.get_elements("order_status_select"),value)

    def select_master(self,value):
        """选择服务师傅"""
        if value != '':
            self.operate_not_select(
                self.get_elements("master_open"),self.get_elements("master_select"),value)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def click_search_more(self):
        """点击搜索更多"""
        self.click_button(self.get_elements("more_search_btn"))

    def select_product_brand(self,value):
        """选择家电品牌"""
        if value != '':
            self.operate_select(self.get_elements("brands_select"),value)

    def select_product_kinds(self,value):
        """选择家电品类"""
        if value != '':
            self.operate_select(self.get_elements("kinds_select"),value)

    def input_product_number(self,productNum):
        """输入产品型号"""
        self.input_message(self.get_elements("product_num_input"),productNum)

    def input_in_pheNum(self,in_pheNum):
        """输入内机条码"""
        self.input_message(self.get_elements("in_phe_num_input"),in_pheNum)

    def select_order_from(self,value):
        """选择工单来源"""
        if value != '':
            self.operate_not_select(
                self.get_elements("order_from_open"),self.get_elements("parent_order_from"),value)

    def select_buy_place(self,value):
        """选择购买渠道"""
        if value != '':
            self.operate_not_select(
                self.get_elements("buy_place_open"),self.get_elements("parent_buy_place"),value)

    def input_create_start_date(self,date):
        """输入订单创建开始日期"""
        self.input_message(self.get_elements("add_order_start_date"),date)

    def input_create_end_date(self,date):
        """输入订单创建结束日期"""
        self.input_message(self.get_elements("add_order_end_date"),date)

    def input_finish_start_date(self,date):
        """输入完成订单开始日期"""
        self.input_message(self.get_elements("finish_order_start_date"),date)

    def input_finish_end_date(self,date):
        """输入完成订单结束日期"""
        self.input_message(self.get_elements("finish_order_end_date"),date)

    def click_more_search_btn(self):
        """点击更多订单搜索的搜索按钮"""
        self.click_button(self.get_elements("search_btn1"))
        self.sleep(1)
        self.click_button(self.get_elements("search_btn1"))

    def search_order_count(self):
        """获取搜索订单数量"""
        return self.get_text(self.get_elements("order_count"))

    def get_first_order_info(self):
        """获取订单列表第一行订单的所有信息"""
        try:
            return self.get_text(self.get_elements("first_order_info"))
        except:
            return "Not find search text in order info !"

    def search_order_by_number(self,order_number):
        """按照订单号搜索订单"""

        # 输入订单号
        self.input_order_Nnumber(order_number)
        # 点击搜索
        self.click_search_btn()
        self.sleep(2)
        if order_number in self.get_first_order_info():
            self.log.info(" ** search order number: {0} . ".format(order_number))
        else:
            raise TimeoutError(" ** Not find order: {0} ! ".format(order_number))


