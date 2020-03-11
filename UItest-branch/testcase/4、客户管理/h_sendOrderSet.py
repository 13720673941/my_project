# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/12 18:13

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.facilitatorPage import FacilitatorPage
import unittest

class Send_Order_Set(unittest.TestCase):
    """ 【服务商派单设置功能】 """

    # 实例化类
    readExcel = Read_Excel("sendOrderSet")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.server_branch = FacilitatorPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "sendOrderSet")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()

    def search_server_branch(self,branch_keyword):
        # 搜索服务商
        self.server_branch.input_search_branch_keyword(branch_keyword)
        # 点击搜索按钮
        self.server_branch.click_search_branch_btn()

    def setUp(self):
        # 刷新数据页面
        self.base.refresh_page()
        # 进入服务商列表页面
        self.server_branch.enter_customer_list_page()
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        self.base.sleep(2)

    @unittest.skipUnless(readExcel.get_isRun_text("sendOrder_set_001"),"-跳过不执行该用例")
    def test_sendOrder_set001(self):
        """禁止派单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("sendOrder_set_001")
        # 打印用例名称
        self.base.print_case_name(data)
        # 进入服务设置页面
        self.search_server_branch(data["禁止派单网点"])
        # # 向右边滑动页面点击禁止派单
        # self.server_branch.click_and_roll_right_page()
        # 点击禁止派单
        self.server_branch.click_stop_please_order()
        # 确定禁止派单
        self.server_branch.click_confirm_stop_please()
        # 进入派单页面
        self.send_order.enter_send_order_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        self.base.sleep(1)
        # 派单到服务商
        self.send_order.select_send_type(data["派单类型"])
        # 搜索服务商
        self.send_order.input_search_name(data["禁止派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(2)
        # 判断不再页面显示
        self.assertMode.assert_el_not_in_page(data,self.send_order.search_branch_is_display())

    @unittest.skipUnless(readExcel.get_isRun_text("sendOrder_set_002"),"-跳过不执行该用例")
    def test_sendOrder_set002(self):
        """恢复派单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("sendOrder_set_002")
        # 打印用例名称
        self.base.print_case_name(data)
        # 进入服务设置页面
        self.search_server_branch(data["恢复派单网点"])
        # # 向右边滑动页面点击禁止派单
        # self.server_branch.click_and_roll_right_page()
        # 点击恢复派单
        self.server_branch.click_open_please_order()
        # 确定恢复派单
        self.server_branch.click_confirm_stop_please()
        # 进入派单页面
        self.send_order.enter_send_order_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        self.base.sleep(1)
        # 派单到服务商
        self.send_order.select_send_type(data["派单类型"])
        # 搜索服务商
        self.send_order.input_search_name(data["恢复派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(2)
        # 判断再页面显示
        self.assertMode.assert_el_in_page(data,self.send_order.search_branch_is_display())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Send_Order_Set)

    unittest.TextTestRunner().run(suits)