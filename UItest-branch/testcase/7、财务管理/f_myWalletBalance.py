# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/13 14:33

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.marketOrderPage import MarketOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.myWalletPage import MyWalletPage
from public.page.invalidOrderPage import InvalidOrder
import unittest

class My_Wallet_Balance(unittest.TestCase):

    """ 【我的钱包余额可用/不可用余额校验】 """

    # 实例化操作类
    readExcel = Read_Excel("myBalance")

    @classmethod
    def setUpClass(cls):
        # 实例化浏览器驱动
        cls.driver = web_driver()
        # 实例化对象类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.market_order = MarketOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.my_wallet = MyWalletPage(cls.driver)
        cls.invalid_order = InvalidOrder(cls.driver)
        cls.assert_mode = Assert(cls.driver,"myBalance")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()

    @unittest.skipUnless(readExcel.get_isRun_text("my_balance_001"),"-跳过不执行该用例")
    def test_my_balance001(self):
        """余额管理-市场单派单冻结钱包余额校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("my_balance_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入我的钱包页面
        self.my_wallet.enter_my_wallet_page()
        self.base.refresh_page()
        # 获取我的余额
        global beforeNotUseBalance
        beforeUseBalance = self.my_wallet.get_my_use_balance_number()
        beforeNotUseBalance = self.my_wallet.get_my_not_use_balance_number()
        # 派单到市场
        self.market_order.send_to_market_main(self.orderNumber,fixedPrice=data["一口价"])
        # 进入我的钱包页面
        self.my_wallet.enter_my_wallet_page()
        # 获取我的余额
        global afterUseBalance
        afterUseBalance = self.my_wallet.get_my_use_balance_number()
        # 断言
        self.assert_mode.assert_equal(data,str(format((beforeUseBalance-afterUseBalance),".2f")))

    @unittest.skipUnless(readExcel.get_isRun_text("my_balance_002"),"-跳过不执行该用例")
    def test_my_balance002(self):
        """余额管理-余额管理-市场派单单增加不可用余额校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("my_balance_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入我的钱包页面
        self.my_wallet.enter_my_wallet_page()
        self.base.refresh_page()
        # 获取我的不可用余额
        global afterNotUseBalance
        afterNotUseBalance = self.my_wallet.get_my_not_use_balance_number()
        # 断言
        self.assert_mode.assert_equal(data,str(format((afterNotUseBalance-beforeNotUseBalance),".2f")))

    @unittest.skipUnless(readExcel.get_isRun_text("my_balance_003"),"-跳过不执行该用例")
    def test_my_balance003(self):
        """余额管理-工单退出市场解冻金额校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("my_balance_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 设置无效工单
        self.invalid_order.set_invalid_order_main(self.orderNumber)
        # 进入我的钱包页面
        self.my_wallet.enter_my_wallet_page()
        self.base.refresh_page()
        # 获取我的余额
        afterInvalidNotUseBalance = self.my_wallet.get_my_not_use_balance_number()
        # 断言
        self.assert_mode.assert_equal(data,str(format((afterNotUseBalance-afterInvalidNotUseBalance),".2f")))

    @unittest.skipUnless(readExcel.get_isRun_text("my_balance_004"),"-跳过不执行该用例")
    def test_my_balance004(self):
        """余额管理-工单退出市场增加可用余额校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("my_balance_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入我的钱包页面
        self.my_wallet.enter_my_wallet_page()
        self.base.refresh_page()
        # 获取我的余额
        afterInvalidUseBalance = self.my_wallet.get_my_use_balance_number()
        # 断言
        self.assert_mode.assert_equal(data,str(format((afterInvalidUseBalance-afterUseBalance),".2f")))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(My_Wallet_Balance)

    unittest.TextTestRunner().run(suits)