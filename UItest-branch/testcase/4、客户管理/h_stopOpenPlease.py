# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/12 18:13

from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.serverBranchPage import ServerBranchPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from config.pathconfig import *
import unittest
"""
设置服务商禁止派单/恢复派单操作：
1、禁止派单功能校验 2、恢复派单功能校验
"""
# 获取测试数据
stop_open_please_data = get_test_data()["AddServerPage"]["stop_open_please_fnc"]

class Stop_Open_Please(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.server_branch = ServerBranchPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        mytest.start_test()
        # 获取网点登录账号密码
        cls.username = read_config_data("西安好家帮家政有限公司","username")
        cls.password = read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(cls.username,cls.password)
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()

    def search_server_branch(self,branch_keyword):
        # 搜索服务商
        self.server_branch.input_search_branch_keyword(branch_keyword)
        # 点击搜索按钮
        self.server_branch.click_search_branch_btn()

    def setUp(self):
        # 刷新数据页面
        self.base_page.refresh_page()

    def test_stop_or_open001(self):
        """禁止派单功能校验"""

        # 获取测试数据
        data = stop_open_please_data["TestCase001"]
        # 打印用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入服务商列表页面
        self.server_branch.enter_customer_list_page()
        # 刷新页面
        self.base_page.refresh_page()
        self.base_page.sleep(2)
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 进入服务设置页面
        self.search_server_branch(branch_keyword=data["StopPleaseBranch"])
        # 向右边滑动页面点击禁止派单
        self.server_branch.click_and_roll_right_page()
        # 点击禁止派单
        self.server_branch.click_stop_please_order()
        # 确定禁止派单
        self.server_branch.click_confirm_stop_please()
        # 进入派单页面
        self.please_order.enter_please_order_page()
        # 选择订单
        self.base_page.select_new_order(OrderNumber=self.order_number)
        # 点击派单
        self.please_order.click_pleaseOrder_btn()
        self.base_page.sleep(1)
        # 派单到服务商
        self.please_order.please_to_branch()
        # 搜索服务商
        self.please_order.input_search_branch_name(branch_name=data["StopPleaseBranch"])
        # 点击搜索
        self.please_order.click_search_branch()
        self.base_page.sleep(2)
        # 判断不再页面显示
        self.assert_mode.assert_el_not_in_page(self.please_order.search_branch_is_display())

    def test_stop_or_open002(self):
        """恢复派单功能校验"""

        # 获取测试数据
        data = stop_open_please_data["TestCase001"]
        # 打印用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入服务商列表页面
        self.server_branch.enter_customer_list_page()
        self.base_page.sleep(2)
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 进入服务设置页面
        self.search_server_branch(branch_keyword=data["StopPleaseBranch"])
        # 向右边滑动页面点击禁止派单
        self.server_branch.click_and_roll_right_page()
        # 点击恢复派单
        self.server_branch.click_open_please_order()
        # 确定恢复派单
        self.server_branch.click_confirm_stop_please()
        # 进入派单页面
        self.please_order.enter_please_order_page()
        # 选择订单
        self.base_page.select_new_order(OrderNumber=self.order_number)
        # 点击派单
        self.please_order.click_pleaseOrder_btn()
        self.base_page.sleep(1)
        # 派单到服务商
        self.please_order.please_to_branch()
        # 搜索服务商
        self.please_order.input_search_branch_name(branch_name=data["StopPleaseBranch"])
        # 点击搜索
        self.please_order.click_search_branch()
        self.base_page.sleep(2)
        # 判断再页面显示
        self.assert_mode.assert_el_in_page(self.please_order.search_branch_is_display())

    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestSuite()
    suits.addTest(Stop_Open_Please("test_stop_or_open001"))
    suits.addTest(Stop_Open_Please("test_stop_or_open002"))

    unittest.TextTestRunner().run(suits)