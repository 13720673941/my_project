# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/28 9:32

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class MyWalletPage(BasePage):

    """
    财务管理-【我的钱包】页面
    """

    # 余额充值按钮
    top_up_btn = (By.XPATH,'//a[contains(text(),"充值")]')
    # 余额体现按钮
    withdraw_deposit_btn = (By.XPATH,'//a[contains(text(),"提现")]')
    # 充值金额输入框
    top_up_input = (By.XPATH,'//label[text()="充值金额："]/..//input')
    # 选择微信支付
    wei_xin_pay_select = (By.XPATH,'//label[contains(text(),"选择支付")]/..//li[1]')
    # 选择支付宝
    ali_pay_select = (By.XPATH,'//label[contains(text(),"选择支付")]/..//li[2]')
    # 提现金额输入框
    withdraw_deposit_input = (By.XPATH,'//label[text()="提现金额："]/..//input')
    # 选择支付宝提现方式
    ali_pay_tx_select = (By.XPATH,'//label[text()="提现方式："]/..//div//label[1]')
    # 选择银行卡提现
    bank_card_tx_select = (By.XPATH,'//label[text()="提现方式："]/..//div//label[2]')
    # 提现用户名
    tx_name_input = (By.XPATH,'//label[text()="提现户名："]/..//input')
    # 支付宝账号输入框
    ali_pay_account_input = (By.XPATH,'//label[contains(text(),"支付宝账号")]/..//input')
    # 验证码输入框
    phone_code_input = (By.XPATH,'//label[contains(text(),"手机验证码")]/..//input')
    # 获取验证码按钮
    get_code_btn = (By.XPATH,'//button[contains(text(),"获取验证码")]')
    # 开户银行名称输入框
    bank_name_input = (By.XPATH,'//label[contains(text(),"开户银行")]/..//input')
    # 银行账号输入框
    bank_account_input = (By.XPATH,'//label[contains(text(),"银行账号")]/..//input')
    # 确认提现按钮
    confirm_button = (By.XPATH,'//div[contains(text(),"提现")]/../..//span[text()="确认"]')


    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_my_wallet_page(self):
        """进入我的钱包页面"""
        self.open_url(my_wallet_url)

    def click_top_up_button(self):
        """点击余额充值按钮"""
        self.click_button(self.top_up_btn)

    def input_top_up_money(self,top_up_money):
        """输入充值金额"""
        self.input_message(self.top_up_input,top_up_money)

    def select_wei_xin_pay(self):
        """选择微信支付"""
        self.click_button(self.wei_xin_pay_select)

    def select_ali_pay(self):
        """选择支付宝支付"""
        self.click_button(self.ali_pay_select)

    def click_withdraw_button(self):
        """点击余额提现按钮"""
        self.click_button(self.withdraw_deposit_btn)

    def input_withdraw_money(self,withdraw_money):
        """输入提现金额"""
        self.input_message(self.withdraw_deposit_input,withdraw_money)

    def input_account_name(self,account_name):
        """输入提现账号姓名"""
        self.input_message(self.tx_name_input,account_name)

    def select_tx_ali_pay(self):
        """选择提现到支付宝"""
        self.click_button(self.ali_pay_tx_select)

    def select_tx_bank_card(self):
        """选择提现到银行卡"""
        self.click_button(self.bank_card_tx_select)

    def input_ali_pay_account(self,ali_pay_account):
        """输入支付宝账号"""
        self.input_message(self.ali_pay_account_input,ali_pay_account)

    def input_bank_name(self,bank_name):
        """输入银行卡所在名称"""
        self.input_message(self.bank_name_input,bank_name)

    def input_bank_card_account(self,bank_account):
        """输入银行卡账号"""
        self.input_message(self.bank_account_input,bank_account)

    def click_get_code_number(self):
        """获取验证码"""
        self.click_button(self.get_code_btn)

    def input_code_number(self,code_number):
        """输入验证码"""
        self.input_message(self.phone_code_input,code_number)

    def click_confirm_button(self):
        """点击确认提现"""
        self.click_button(self.confirm_button)

