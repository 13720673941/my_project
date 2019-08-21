# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/20 17:08

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.orderLogPage import OrderLogPage
from config.pathconfig import *
import unittest
"""
工单余量日志记录页面搜索筛选:
1、按照创建订单日期搜索校验  2、按照派单类型搜索校验  3、按照订单单号搜索校验  4、混合搜索扣除记录校验
"""
# 获取测试数据
test_data = get_test_data()["OrderLogPage"]["search_log_fnc"]

class Search_Order_Log(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.order_log = OrderLogPage(cls.driver)
        mytest.start_test()
        # 获取网点登录账号信息
        username = read_config_data("XM科技有限公司","username")
        password = read_config_data("XM科技有限公司","password")
        # 登录
        cls.login.login_main(username,password)
        # 进入工单日志页面
        cls.order_log.enter_order_log_page()

    def test_order_log001(self):
        """按下单日期搜索扣除订单的记录信息"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入开始日期
        self.order_log.input_start_date(start_date=self.base_page.get_now_time())
        # 输入结束日期
        self.order_log.input_end_date(end_date=self.base_page.get_now_time())
        # 点击搜索按钮
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(self.base_page.get_now_time(),first_log_info)

    def test_order_log002(self):
        """按扣除类型搜索日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 选择类型信息
        self.order_log.select_deduct_type(value=data["SearchType"])
        # 点击搜索
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(data["SearchType"],first_log_info)

    def test_order_log003(self):
        """按工单编号搜索订单余量扣除记录校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取工单编号- 关联扣除单量脚本中创建的订单单号
        order_number = read_config_data("for_operate_log_search","id",orderNumPath)
        # 刷新页面
        self.base_page.refresh_page()
        # 输入工单编号
        self.order_log.input_order_number(order_number=order_number)
        # 点击搜索
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(order_number,first_log_info)

    @classmethod
    def tearDownClass(cls):

        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Search_Order_Log)

    unittest.TextTestRunner().run(suits)