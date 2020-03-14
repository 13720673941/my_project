#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/3 18:50

from public.common.basePage import BasePage
from public.page.searchOrderPage import SearchOrderPage
from public.page.createOrderPage import CreateOrderPage
from config.urlConfig import *

class InvalidOrder(BasePage):
    """
        【设置无效工单页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search = SearchOrderPage(driver)
        self.create = CreateOrderPage(driver)

    def enter_invalid_list_page(self):
        """无效工单列表页"""
        self.open_url(invalid_order_url)

    def get_elements(self,option):
        """获取element_data文件中设置无效工单的元素信息"""
        return read_config_data("invalid_order_page",option,elementDataPath)

    def click_invalid_btn(self):
        """点击无效工单按钮"""
        self.click_button(self.get_elements("invalid_order_btn"))

    def select_invalid_type(self,invalidType="用户拒修"):
        """
        选择无效工单类型: 用户拒修、价格高拒修、用户自己修好、用户找人修好、产品自行恢复、非服务产品
        """
        if invalidType != '':
            self.operate_select(self.get_elements("invalid_type_select"),invalidType)

    def input_invalid_reason(self,invalidReason):
        """输入无效工单原因"""
        self.input_message(self.get_elements("invalid_reason_input"),invalidReason)

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.get_elements("confirm_btn"))

    def set_invalid_order_main(self,orderNumber):
        """设置无效工单主程序"""

        # 全部工单列表中搜索工单
        for i in range(10):
            try:
                self.search.enter_search_order_page()
                self.search.input_order_Nnumber(orderNumber)
                self.search.click_search_btn()
                self.sleep(1)
                if orderNumber in self.search.get_first_order_info():
                    break
            except:
                if i == 9:
                    raise TimeoutError(" 全部工单列表中搜索不到该订单：{}".format(orderNumber))
                else:
                    continue
        # 设置无效工单
        self.create.select_operate_order(orderNumber)
        # 点击无效工单按钮
        self.click_invalid_btn()
        # 选择无效工单原因
        self.select_invalid_type()
        # 点击确认
        self.click_confirm_btn()
        # 判断
        self.sleep(1)
        if "无效工单" in self.search.get_first_order_info():
            self.log.info(" ** Set invalid order success !")
        else:
            raise Exception(" ** Set invalid order fail !")

