# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/5 14:09

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
import unittest

class Order_Details(unittest.TestCase):

    """" 【工单详情页修改工单/新建工单/打印工单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("orderDetails")
    
    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.order_details = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "orderDetails")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取工单单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单师傅
        master = rwConfig.read_config_data('T西安好家帮家政有限公司','master001')
        # 派单到师傅
        cls.send_order.send_order_main(cls.orderNumber,pageName=master)

    def setUp(self):
        """工共操作"""
        # 刷新
        self.base.refresh_page()
        # 进入订单列表页
        self.send_order.enter_send_order_page()
        # 进入订单详情
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(1)

    @unittest.skipUnless(read_excel.get_isRun_text("alter_order_001"),"-跳过不执行该用例")
    def test_alter_order_001(self):
        """订单详情页修改订单内容功能用例"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("alter_order_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击修改订单
        self.order_details.click_alter_order_btn()
        # 页面加载慢等待原始数据加载出来再修改
        self.base.sleep(2)
        # 输入手机号
        self.create_order.input_username(data["修改用户姓名"])
        # 点击保存订单
        self.create_order.click_save_btn()
        # 进入订单列表页
        self.send_order.enter_send_order_page()
        # 进入订单详情判断
        self.create_order.open_order_details(self.orderNumber)
        # 加载
        self.base.sleep(2)
        # 判断修改订单成功
        self.assert_mode.assert_in(data,self.order_details.get_alter_text_of_order())

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_002"),"-跳过不执行该用例")
    def test_create_order_002(self):
        """订单详情页新建订单功能用例"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击新建订单
        self.order_details.click_new_create_btn()
        self.base.sleep(2)
        # 点击保存订单
        self.create_order.click_save_btn()
        # 判断新建订单成功
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("print_order_003"),"-跳过不执行该用例")
    def test_print_order_003(self):
        """订单详情页打印订单功能用例"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("print_order_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取当前窗口handle
        old_handle = self.base.get_current_handle()
        # 点击打印订单
        self.order_details.click_print_order_btn()
        # 获取全部handles
        handles = self.base.get_all_handles()
        # 切换页面
        self.base.switch_to_new_handle(handles,old_handle)
        # 判断新建订单成功
        self.assert_mode.assert_equal(data,self.base.get_title())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Order_Details)

    unittest.TextTestRunner().run(suit)