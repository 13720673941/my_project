# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/19 10:21

from public.common import myDecorator
from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
from public.common.assertMode import Assert
import unittest

class Alter_Order_Charge(unittest.TestCase):

    """ 【修改工单服务费功能测试用例】 """

    # 实例化类
    read_excel = Read_Excel("alterCharge")
    
    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.search_order = SearchOrderPage(cls.driver)
        cls.order_details = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "alterCharge")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取网点服务商名称
        serverBranch = rwConfig.read_config_data("T西安好家帮家政有限公司","branch001")
        # 派单到服务商
        cls.send_order.send_order_main(cls.orderNumber,pageName=serverBranch,sendType="服务商")
        # 登录服务商
        cls.login.click_logout_button()
        cls.login.login_main(serverBranch)
        # 获取派单师傅
        master = rwConfig.read_config_data(serverBranch,"master001")
        # 派单到师傅
        cls.send_order.send_order_main(cls.orderNumber,pageName=master,takeOrder=True)
        # 完成服务
        cls.finish_order.finish_order_main(cls.orderNumber)
        cls.base.refresh_page()

    @unittest.skipUnless(read_excel.get_isRun_text("alter_charge_001"),"-跳过不执行该用例")
    def test_alter_charge_001(self):
        """修改服务费-成功修改工单服务费校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("alter_charge_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 退出服务商登录经销商
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入待回访工单列表页面
        self.visit_order.enter_visit_order_page()
        # 搜索工单
        self.search_order.search_order_by_number(self.orderNumber)
        # 选择工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击修改服务费
        self.order_details.click_alter_charge()
        # 输入服务费用
        self.order_details.input_server_charge(data["服务费价格"])
        # 点击确认修改服务费
        self.order_details.click_confirm_alter_charge()
        self.base.refresh_page()
        # 点击工单进入详情页
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)
        # 断言
        self.assert_mode.assert_equal(data,self.order_details.get_order_charge())

    @unittest.skipUnless(read_excel.get_isRun_text("alter_charge_002"),"-跳过不执行该用例")
    def test_alter_charge_002(self):
        """修改服务费-修改过的不能再次修改校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("alter_charge_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 搜索工单
        self.search_order.search_order_by_number(self.orderNumber)
        # 选择工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击修改服务费
        self.order_details.click_alter_charge()
        # 输入服务费用
        # self.order_details.input_server_charge(data["服务费价格"])
        # 点击确认修改服务费
        # self.order_details.click_confirm_alter_charge()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    # @unittest.skipUnless(read_excel.get_isRun_text("alter_charge_003"),"-跳过不执行该用例")
    # def test_alter_charge_001(self):
    #     """修改服务费-已确认的账单不能修改校验"""
    #
    #     # 获取测试数据
    #     data = self.read_excel.get_dict_data("alter_charge_003")
    #     # 打印测试用例名称
    #     self.base.print_case_name(data)
    #     """
    #     确认账单....
    #     """

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Alter_Order_Charge)

    unittest.TextTestRunner().run(suit)


