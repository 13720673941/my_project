# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 10:05

from public.common.basePage import BasePage
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.myWalletPage import MyWalletPage
import unittest

class Wallet_Top_Up(unittest.TestCase):

    """ 【我的钱包充值功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("walletTopUp")

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.my_wallet = MyWalletPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"walletTopUp")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入我的钱包页面
        cls.my_wallet.enter_my_wallet_page()
        cls.base_page.sleep(1)
        # 点击充值
        cls.my_wallet.click_top_up_button()
        cls.base_page.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("wallet_topUp_001"),"跳过不执行该用例")
    def test_wallet_top_up001(self):
        """充值金额不能小于0校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("wallet_topUp_001")
        # 打印测试用例
        self.base_page.print_case_name(data)
        # 输入充值金额
        self.my_wallet.input_top_up_money(data["充值金额"])
        # 选择微信支付
        self.my_wallet.select_wei_xin_pay()
        # 点击充值
        self.my_wallet.click_top_up_button()
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("wallet_topUp_002"),"跳过不执行该用例")
    def test_wallet_top_up002(self):
        """支付宝充值可以跳转支付宝页面校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("wallet_topUp_002")
        # 打印测试用例
        self.base_page.print_case_name(data)
        # 刷新页面
        self.base_page.refresh_page()
        # 输入充值金额
        self.my_wallet.input_top_up_money(data["充值金额"])
        # 选择支付宝支付
        self.my_wallet.select_ali_pay()
        # 点击充值
        self.my_wallet.click_top_up_button()
        self.base_page.sleep(2)
        # 断言
        self.assert_page.assert_in(data,self.base_page.get_title())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Wallet_Top_Up)

    unittest.TextTestRunner().run(suits)
