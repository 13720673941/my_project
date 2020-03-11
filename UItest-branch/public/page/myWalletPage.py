# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/28 9:32

from public.common.basePage import BasePage
from config.urlConfig import *

class MyWalletPage(BasePage):

    """
        财务管理-【我的钱包】页面
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_my_wallet_page(self):
        """进入我的钱包页面"""
        self.open_url(my_wallet_url,self.get_elements("top_up_btn"))

    def get_elements(self,option):
        """获取element_data文件中我的钱包页面的元素信息"""
        return read_config_data("my_wallet_page",option,elementDataPath)

    def click_top_up_button(self):
        """点击余额充值按钮"""
        self.click_button(self.get_elements("top_up_btn"))

    def input_top_up_money(self,topUpMoney):
        """输入充值金额"""
        self.input_message(self.get_elements("top_up_input"),topUpMoney)

    def select_wei_xin_pay(self):
        """选择微信支付"""
        self.click_button(self.get_elements("wei_xin_pay_select"))

    def select_ali_pay(self):
        """选择支付宝支付"""
        self.click_button(self.get_elements("ali_pay_select"))

    def click_withdraw_button(self):
        """点击余额提现按钮"""
        self.click_button(self.get_elements("withdraw_deposit_btn"))

    def input_withdraw_money(self,withdrawMoney):
        """输入提现金额"""
        self.input_message(self.get_elements("withdraw_deposit_input"),withdrawMoney)

    def input_account_name(self,accountName):
        """输入提现账号姓名"""
        self.input_message(self.get_elements("tx_name_input"),accountName)

    def select_tx_ali_pay(self):
        """选择提现到支付宝"""
        self.click_button(self.get_elements("ali_pay_tx_select"))

    def select_tx_bank_card(self):
        """选择提现到银行卡"""
        self.click_button(self.get_elements("bank_card_tx_select"))

    def input_ali_pay_account(self,aliPayAccount):
        """输入支付宝账号"""
        self.input_message(self.get_elements("ali_pay_account_input"),aliPayAccount)

    def input_bank_name(self,bankName):
        """输入银行卡所在名称"""
        self.input_message(self.get_elements("bank_name_input"),bankName)

    def input_bank_card_account(self,bankAccount):
        """输入银行卡账号"""
        self.input_message(self.get_elements("bank_account_input"),bankAccount)

    def click_get_code_number(self):
        """获取验证码"""
        self.click_button(self.get_elements("get_code_btn"))

    def input_code_number(self,codeNumber):
        """输入验证码"""
        self.input_message(self.get_elements("phone_code_input"),codeNumber)

    def click_confirm_button(self):
        """点击确认提现"""
        self.click_button(self.get_elements("confirm_button"))

