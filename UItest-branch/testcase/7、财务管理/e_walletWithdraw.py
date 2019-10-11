# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 11:01

from public.common import mytest
from public.common import rwconfig
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.page.loginPage import LoginPage
from public.page.myWalletPage import MyWalletPage
import unittest
"""
我的钱包提现测试用例：
1、提现金额不能小于100校验
"""
# 获取测试数据
test_data = get_test_data()["MyWalletPage"]["withdraw_fnc"]

class Wallet_Withdraw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.my_wallet = MyWalletPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        # 开始执行测试
        mytest.start_test()
        # 获取测试账号
        username = rwconfig.read_config_data("蓝魔科技","username")
        password = rwconfig.read_config_data("蓝魔科技","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入我的钱包页面
        cls.my_wallet.enter_my_wallet_page()
        cls.base_page.sleep(1)

    def setUp(self):

        self.base_page.refresh_page()
        # 点击提现按钮
        self.my_wallet.click_withdraw_button()
        self.base_page.sleep(1)

    def test_wallet_withdraw001(self):
        """提现金额不能小于100校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 输入提现金额
        self.my_wallet.input_withdraw_money(withdraw_money=data["Money"])
        # 选择提现支付宝
        self.my_wallet.select_tx_ali_pay()
        # 输入提现用户名
        self.my_wallet.input_account_name(account_name=data["UserName"])
        # 输入支付宝账号
        self.my_wallet.input_ali_pay_account(ali_pay_account=data["AliPay"])
        # 输入验证码
        self.my_wallet.input_code_number(code_number=data["CodeNum"])
        # 点击确认
        self.my_wallet.click_confirm_button()
        # 获取系统提示信息
        system_msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],system_msg)


    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Wallet_Withdraw)

    unittest.TextTestRunner().run(suits)