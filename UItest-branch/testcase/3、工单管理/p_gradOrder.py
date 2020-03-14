# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/21 21:23

from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.marketOrderPage import MarketOrderPage
import unittest

class Grad_Order(unittest.TestCase):

    """ 【派单到抢单市场/抢单功能】 """

    """
        ---------- 引入账户余额校验少于 0.01 不得派单到市场 ---------
    """

    # 实例化类
    read_excel = Read_Excel("gradOrder")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.market_order = MarketOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"gradOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 进入全部工单列表页面
        cls.market_order.enter_send_order_page()

    @unittest.skipUnless(read_excel.get_dict_data("grad_order_001"),"-跳过不执行该用例")
    def test_grad_order001(self):
        """市场抢单-派单价格为空校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("grad_order_001")
        # 测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.market_order.click_send_to_market()
        # 选择派单到市场
        self.market_order.click_fixed_price_btn()
        # 输入抢单价格
        self.market_order.input_fixed_price(data["抢单价格"])
        # 点击派单
        self.market_order.click_confirm_send()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_dict_data("grad_order_002"),"-跳过不执行该用例")
    def test_grad_order002(self):
        """市场抢单-派单金额不足校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("grad_order_002")
        # 测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.market_order.click_send_to_market()
        # 选择派单到市场
        self.market_order.click_fixed_price_btn()
        # 输入抢单价格
        self.market_order.input_fixed_price(data["抢单价格"])
        # 点击派单
        self.market_order.click_confirm_send()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.market_order.get_send_order_msg())

    @unittest.skipUnless(read_excel.get_dict_data("grad_order_003"),"-跳过不执行该用例")
    def test_grad_order003(self):
        """市场抢单-成功派单到市场校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("grad_order_003")
        # 测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.market_order.click_send_to_market()
        # 选择派单到市场
        self.market_order.click_fixed_price_btn()
        # 输入抢单价格
        self.market_order.input_fixed_price(data["抢单价格"])
        # 点击派单
        self.market_order.click_confirm_send()
        self.base.sleep(2)
        # 退出登录
        self.login.click_logout_button()
        # 登录抢单网点
        self.login.login_main("T西安超级售后有限公司")
        # 进入待抢单工单页面
        self.market_order.enter_market_order_page()
        # 判断订单在订单列表中
        orderIsDisplayed = self.create_order.assert_order_in_list(self.orderNumber)
        # 断言
        self.assert_mode.assert_el_in_page(data,orderIsDisplayed)

    @unittest.skipUnless(read_excel.get_dict_data("grad_order_004"),"-跳过不执行该用例")
    def test_grad_order004(self):
        """市场抢单-抢单成功校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("grad_order_004")
        # 测试用例名称
        self.base.print_case_name(data)
        # 进入待抢单工单页面
        self.market_order.enter_market_order_page()
        # 刷新页面
        self.base.refresh_page()
        # 点击订单进入订单详情页
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)
        # 点击抢单按钮
        self.market_order.click_grad_order_btn()
        # 点击确定抢单按钮
        self.market_order.click_confirm_grad_order()
        # 获取系统提示信息
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Grad_Order)

    unittest.TextTestRunner().run(suit)