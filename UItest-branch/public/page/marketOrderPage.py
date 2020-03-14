# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/11 17:12

from public.common.basePage import BasePage
from public.page.createOrderPage import CreateOrderPage
from public.page.loginPage import LoginPage
from config.urlConfig import *

class MarketOrderPage(BasePage):

    """市场单/报价单->派单、抢单、报单"""

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.create_order = CreateOrderPage(driver)
        self.login = LoginPage(driver)

    def get_elements(self,option):
        """获取element_data文件中派单页面的元素信息"""
        return read_config_data("market_order_page",option,elementDataPath)

    def enter_send_order_page(self):
        """进入派单页面"""
        self.open_url(all_order_list_url,self.get_elements("send_to_market_btn"))

    def enter_market_order_page(self):
        """进入市场单页面抢单"""
        self.open_url(wait_grad_order_url,self.get_elements("grad_market_title"))

    def click_send_to_market(self):
        """点击发布订单到市场"""
        self.click_button(self.get_elements("send_to_market_btn"))

    def click_fixed_price_btn(self):
        """选择一口价订单"""
        self.click_button(self.get_elements("select_grad_market_btn"))

    def input_fixed_price(self,fixedPrice):
        """输入一口价格"""
        self.input_message(self.get_elements("fixed_price_input"),fixedPrice)

    def input_cash_back_price(self,cashBackPrice):
        """输入返现价格"""
        self.input_message(self.get_elements("high_praise_cash_back_input"),cashBackPrice)

    def input_emergency_price(self,emergencyPrice):
        """输入加急费用"""
        self.input_message(self.get_elements("emergency_fee_input"),emergencyPrice)

    def click_quote_price_btn(self):
        """选择派单市场报价单"""
        self.click_button(self.get_elements("select_quote_order_btn"))

    def input_expect_quote_price(self,quotePrice):
        """输入期望报价"""
        self.input_message(self.get_elements("expect_quote_price_input"),quotePrice)

    def click_confirm_send(self):
        """点击确定派单"""
        self.click_button(self.get_elements("confirm_send_order_btn"))

    def get_send_order_msg(self):
        """获取派单提醒->余额不足"""
        return self.get_text(self.get_elements("wallet_not_enough_msg"))

    def click_grad_order_btn(self):
        """点击抢单按钮"""
        self.sleep(2)
        self.click_button(self.get_elements("grad_order_btn"))

    def click_confirm_grad_order(self):
        """点击确定抢单按钮"""
        self.click_button(self.get_elements("confirm_grad_order_btn"))

    def send_to_market_main(self,orderNumber,quoteOrder=False,quotePrice="0.01",
                            fixedPrice="0.01",cashBackPrice="0",emergencyPrice="0"):
        """
        派单到抢单市场主程序
        :param orderNumber      订单单号
        :param quoteOrder       是否为报价单，默认为一口价订单
        :param quotePrice       期望报价金额 默认 0.01
        :param fixedPrice       一口价订单结算金额 默认 0.01
        :param cashBackPrice    好评返现金额 默认 0.01
        :param emergencyPrice   加急费用 默认 0.01
        """

        self.log.info("-=【发布到市场】=-")
        # 进入全部订单页面
        self.enter_send_order_page()
        # 选择订单
        self.create_order.select_operate_order(orderNumber)
        # 点击发布到市场
        self.click_send_to_market()
        # 判断一口价订单/报价订单,默认选择一口价订单
        if quoteOrder:
            self.click_quote_price_btn()
            # 输入期望报价金额
            self.input_expect_quote_price(quotePrice)
        else:
            # 一口价订单输入一口价金额
            self.input_fixed_price(fixedPrice)
            # 好评返现价格金额
            self.input_cash_back_price(cashBackPrice)
            # 输入加急价格费用
            self.input_emergency_price(emergencyPrice)
        # 点确定派单按钮
        self.click_confirm_send()
        # 判断派单是否成功
        if "派发成功" in self.login.get_system_msg():
            self.log.info(" ** Send order to market success !")
        else:
            raise Exception(" ** Send order to market fail !")

    def grad_order_main(self,orderNumber):
        """抢单主程序"""

        self.log.info("-=【市场抢单】=-")
        # 进入市场订单列表页面
        self.enter_market_order_page()
        self.sleep(2)
        # 进入工单详情页
        self.create_order.open_order_details(orderNumber)
        # 点击抢单按钮
        self.click_grad_order_btn()
        # 点击确认抢单
        self.click_confirm_grad_order()
        # 判断派单是否成功
        if "接单成功" in self.login.get_system_msg():
            self.log.info(" ** Grad order success !")
        else:
            raise Exception(" ** Grad order fail !")