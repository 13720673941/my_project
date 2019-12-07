# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 10:05

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
我的钱包页面功能测试用例：
1、充值金额不能小于0校验 2、支付宝充值可以跳转支付宝页面校验
"""
# 获取测试数据
test_data = get_test_data()["MyWalletPage"]["top_up_fnc"]

class Wallet_Top_Up(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.my_wallet = MyWalletPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行测试
        mytest.start_test()
        # 获取测试账号
        username = rwconfig.read_config_data("西安好家帮家政有限公司","username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入我的钱包页面
        cls.my_wallet.enter_my_wallet_page()
        cls.base_page.sleep(1)
        # 点击充值
        cls.my_wallet.click_top_up_button()
        cls.base_page.sleep(1)

    def test_wallet_top_up001(self):
        """充值金额不能小于0校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 输入充值金额
        self.my_wallet.input_top_up_money(top_up_money=data["Money"])
        # 选择微信支付
        self.my_wallet.select_wei_xin_pay()
        # 点击充值
        self.my_wallet.click_top_up_button()
        # 获取系统提示信息
        system_msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],system_msg)

    def test_wallet_top_up002(self):
        """支付宝充值可以跳转支付宝页面校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 输入充值金额
        self.my_wallet.input_top_up_money(top_up_money=data["Money"])
        # 选择支付宝支付
        self.my_wallet.select_ali_pay()
        # 点击充值
        self.my_wallet.click_top_up_button()
        self.base_page.sleep(2)
        # 获取页面标题信息
        page_title = self.base_page.get_title()
        # 断言
        self.assert_page.assert_in(data["expect"],page_title)


    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Wallet_Top_Up)

    unittest.TextTestRunner().run(suits)
