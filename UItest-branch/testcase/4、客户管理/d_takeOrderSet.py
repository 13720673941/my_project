#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 15:14

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.dealerPage import DealerPage
import unittest

class Take_Order_Set(unittest.TestCase):

    """ 【经销商设置暂停/恢复接单功能】 """

    # 实例化类
    readExcel = Read_Excel("takeOrderSet")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.manage_branch = DealerPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "takeOrderSet")
        # 获取经销商名称
        cls.dealerName = rwConfig.read_config_data("T西安好家帮家政有限公司","manage_branch")
        # 登录经销商网点
        cls.login.login_main(cls.dealerName)
        # 经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 退出登录
        cls.login.click_logout_button()
        # 登录服务商网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入邀请经销商页面
        cls.manage_branch.enter_dealer_page()

    def setUp(self):
        self.base.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("takeOrder_set_001"),"-跳过不执行该用例")
    def test_takeOrder_set_001(self):
        """暂停接单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("takeOrder_set_001")
        # 打印测试名称
        self.base.print_case_name(data)
        # 搜索经销商
        self.manage_branch.input_search_message(data["暂停接单网点"])
        # 点击搜索
        self.manage_branch.click_search()
        # 点击暂停接单
        self.manage_branch.click_stop_take_order()
        self.base.sleep(2)
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.dealerName)
        # 进入派单页面
        self.send_order.enter_send_order_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        # 选择派单服务商
        self.send_order.select_send_type(data["派单类型"])
        self.base.sleep(1)
        # 搜索服务商名称
        self.send_order.input_search_name(data["派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(2)
        # 验证是否有暂停接单字段
        self.assertMode.assert_el_in_page(data,self.send_order.stop_take_order_is_displayed())

    @unittest.skipUnless(readExcel.get_isRun_text("takeOrder_set_002"),"-跳过不执行该用例")
    def test_takeOrder_set_002(self):
        """开启接单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("takeOrder_set_002")
        # 打印测试名称
        self.base.print_case_name(data)
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务撒
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入客户列表
        self.manage_branch.enter_dealer_page()
        # 搜索经销商
        self.manage_branch.input_search_message(data["恢复接单网点"])
        # 点击搜索
        self.manage_branch.click_search()
        # 点击恢复接单
        self.manage_branch.click_open_take_order()
        self.base.sleep(2)
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.dealerName)
        # 进入派单页面
        self.send_order.enter_send_order_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        # 选择派单服务商
        self.send_order.select_send_type(data["派单类型"])
        self.base.sleep(1)
        # 搜索服务商名称
        self.send_order.input_search_name(data["派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(2)
        # 验证是否有暂停接单字段
        self.assertMode.assert_el_not_in_page(data,self.send_order.stop_take_order_is_displayed())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Take_Order_Set)

    unittest.TextTestRunner().run(suit)
