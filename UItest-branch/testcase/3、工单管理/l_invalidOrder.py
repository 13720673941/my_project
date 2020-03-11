#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/4 10:29

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.invalidOrderPage import InvalidOrder
from public.page.searchOrderPage import SearchOrderPage
import unittest

class Set_InvalidOrder(unittest.TestCase):

    """" 【设置无效工单功能测试用例脚本】 """
    
    # 实例化类

    read_excel = Read_Excel("invalidOrder")
    
    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.invalid_order = InvalidOrder(cls.driver)
        cls.search_order = SearchOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "invalidOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 网点下单程序下单
        cls.create_order.create_not_return_order()
        # 获取创建成功的订单单号
        cls.orderNumber = cls.create_order.get_order_number()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()

    @unittest.skipUnless(read_excel.get_isRun_text("invalid_order_001"),"-跳过不执行该用例")
    def test_set_invalid001(self):
        """设置无效工单类型为空校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("invalid_order_001")
        # 打印测试用力名称
        self.base.print_case_name(data)
        # 选择新建工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击无效工单
        self.invalid_order.click_invalid_btn()
        # 选择无效工单类型
        self.invalid_order.select_invalid_type(data["无效工单类型"])
        # 输入无效工单原因
        self.invalid_order.input_invalid_reason(data["无效原因"])
        # 点击确定
        self.invalid_order.click_confirm_btn()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("invalid_order_002"),"-跳过不执行该用例")
    def test_set_invalid002(self):
        """设置无效工单类型成功校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("invalid_order_002")
        # 打印测试用力名称
        self.base.print_case_name(data)
        # 选择新建工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击无效工单
        self.invalid_order.click_invalid_btn()
        # 选择无效工单类型
        self.invalid_order.select_invalid_type(data["无效工单类型"])
        # 输入无效工单原因
        self.invalid_order.input_invalid_reason(data["无效原因"])
        # 点击确定
        self.invalid_order.click_confirm_btn()
        self.base.sleep(1)
        # 进入无效工单列表页面
        self.invalid_order.enter_invalid_list_page()
        self.base.refresh_page()
        # 判断订单在列表中
        isDisplay = self.create_order.assert_order_in_list(self.orderNumber)
        # 断言
        self.assert_mode.assert_el_in_page(data,isDisplay)

    @unittest.skipUnless(read_excel.get_isRun_text("invalid_order_003"),"-跳过不执行该用例")
    def test_set_invalid003(self):
        """待服务商派单订单不能设置无效工单校验"""

        # 获取派单数据
        branchName = rwConfig.read_config_data('T西安好家帮家政有限公司','branch001')
        # 获取测试数据
        data = self.read_excel.get_dict_data("invalid_order_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 选择派单服务商
        self.send_order.send_order_main(self.orderNumber,pageName=branchName,sendType="服务商")
        self.base.refresh_page()
        # 选择订单
        self.base.sleep(1)
        self.create_order.select_operate_order(self.orderNumber)
        # 点击无效工单
        self.invalid_order.click_invalid_btn()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("invalid_order_004"),"-跳过不执行该用例")
    def test_set_invalid004(self):
        """已结算的订单设置无效工单校验"""

        # 获取数据
        data = self.read_excel.get_dict_data("invalid_order_004")
        # 打印测试用名称
        self.base.print_case_name(data)
        # 获取已结算订单单号
        OrderNumber = rwConfig.read_config_data('for_invalid_and_search','id',orderNumPath)
        # 刷新页面
        self.base.refresh_page()
        # 搜索订单
        self.search_order.search_order_by_number(OrderNumber)
        # 选择结算订单
        self.create_order.select_operate_order(OrderNumber)
        # 点击无效工单
        self.invalid_order.click_invalid_btn()
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
    unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Set_InvalidOrder)

    unittest.TextTestRunner().run(suit)