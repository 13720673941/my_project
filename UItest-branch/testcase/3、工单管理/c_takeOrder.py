# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/14 21:45

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.common.assertMode import Assert
import unittest

class Take_Order(unittest.TestCase):

    """" 【网点接单功能测试用例脚本】 """

    # 实例化操作类
    read_excel = Read_Excel("takeOrder")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"takeOrder")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单服务商
        cls.server_branch = rwConfig.read_config_data("T西安好家帮家政有限公司","branch001")
        # 派单到服务商
        cls.send_order.send_order_main(cls.orderNumber,pageName=cls.server_branch,sendType="服务商")

    @unittest.skipUnless(read_excel.get_isRun_text("take_order_001"),"-跳过不执行该测试用例")
    def test_take_order001(self):
        """未接单之前不能派单校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("take_order_001")
        # 打印测试用例名成
        self.base.print_case_name(data)
        # 退出当前网点登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.server_branch)
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        self.base.sleep(1)
        # 选择待派订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单按钮
        self.send_order.click_send_order_btn()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("take_order_002"),"-跳过不执行该测试用例")
    def test_take_order002(self):
        """成功接单校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("take_order_002")
        # 打印测试用例名成
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        self.base.sleep(1)
        # 选择待派订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击接单按钮
        self.send_order.click_take_order()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("take_order_003"),"-跳过不执行该测试用例")
    def test_take_order003(self):
        """成功接单之后可以派单校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("take_order_003")
        # 打印测试用例名成
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        self.base.sleep(1)
        # 选择待派订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击接单按钮
        self.send_order.click_send_order_btn()
        # 选择派单类型
        self.send_order.select_send_type(data["派单类型"])
        # 选择派单师傅
        self.send_order.select_send_page(data["派单对象"])
        # 点击派单
        self.send_order.click_confirm_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Take_Order)

    unittest.TextTestRunner().run(suit)