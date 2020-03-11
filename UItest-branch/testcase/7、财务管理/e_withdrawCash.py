# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 11:01

from public.common.basePage import BasePage
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.myWalletPage import MyWalletPage
import unittest,ddt

@ddt.ddt
class Withdraw_Cash(unittest.TestCase):

    """ 【我的钱包提现功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("withdrawCash")
    # 获取ddt测试用例集合
    case_list1 = [
        "withdraw_cash_001","withdraw_cash_002",
        "withdraw_cash_003","withdraw_cash_004"
    ]
    case_list2 = [
        "withdraw_cash_005","withdraw_cash_006"
    ]
    # 读取ddt格式测试数据
    ddt_data1 = readExcel.get_ddt_data(case_list1)
    ddt_data2 = readExcel.get_ddt_data(case_list2)

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.my_wallet = MyWalletPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"withdrawCash")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入我的钱包页面
        cls.my_wallet.enter_my_wallet_page()
        cls.base_page.sleep(2)

    def setUp(self):
        self.base_page.refresh_page()

    @ddt.data(*ddt_data1)
    @myDecorator.skipped_case
    def test_wallet_withdraw001(self,ddt_data1):
        """提现到支付宝校验"""

        # 点击提现按钮
        self.my_wallet.click_withdraw_button()
        self.base_page.sleep(1)
        # 打印测试用例
        self.base_page.print_case_name(ddt_data1)
        # 输入提现金额
        self.my_wallet.input_withdraw_money(ddt_data1["提现金额"])
        # 选择提现支付宝
        self.my_wallet.select_tx_ali_pay()
        # 输入提现用户名
        self.my_wallet.input_account_name(ddt_data1["用户名"])
        # 输入支付宝账号
        self.my_wallet.input_ali_pay_account(ddt_data1["支付宝账号"])
        # 输入验证码
        self.my_wallet.input_code_number(ddt_data1["验证码"])
        # 点击确认
        self.my_wallet.click_confirm_button()
        # 断言
        self.assert_page.assert_equal(ddt_data1,self.login.get_system_msg())

    """
        提现金额首先判断大于100，因钱包余额不足后面的必填项逻辑测试脚本无法编辑
    """

    @ddt.data(*ddt_data2)
    @myDecorator.skipped_case
    def test_wallet_withdraw002(self,ddt_data2):
        """提现到银行卡校验"""

        # 清除数据
        self.base_page.refresh_page()
        # 点击提现按钮
        self.my_wallet.click_withdraw_button()
        self.base_page.sleep(1)
        # 打印测试用例
        self.base_page.print_case_name(ddt_data2)
        # 输入提现金额
        self.my_wallet.input_withdraw_money(ddt_data2["提现金额"])
        # 选择提现支付宝
        self.my_wallet.select_tx_bank_card()
        # 输入提现用户名
        self.my_wallet.input_account_name(ddt_data2["用户名"])
        # 输入开户银行
        self.my_wallet.input_bank_name(ddt_data2["银行名称"])
        # 输入验证码
        self.my_wallet.input_bank_card_account(ddt_data2["银行卡账号"])
        # 输入验证码
        self.my_wallet.input_code_number(ddt_data2["验证码"])
        # 点击确认
        self.my_wallet.click_confirm_button()
        # 断言
        self.assert_page.assert_equal(ddt_data2,self.login.get_system_msg())


    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Withdraw_Cash)

    unittest.TextTestRunner().run(suits)