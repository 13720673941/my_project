# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/24 9:55

from public.common import rwconfig
from public.common import mytest
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.page.financeManagePage import FinanceManagePage
from public.page.loginPage import LoginPage
from config.pathconfig import *
import unittest
"""
我的收入页面搜索功能测试用例：
1、按收入类型搜索校验 2、按服务类型搜索校验 3、按服务师傅名称搜索校验 4、按工单编号搜索校验
"""
# 获取测试数据
test_data = get_test_data()["MyIncomePage"]

class My_Income_Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.my_income = FinanceManagePage(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        cls.username = rwconfig.read_config_data("西安超级售后有限公司","username")
        cls.password = rwconfig.read_config_data("西安超级售后有限公司","password")
        # 登录网点
        cls.login.login_main(cls.username,cls.password)
        # 进入我的收入页面
        cls.my_income.enter_my_income_page()

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()

    """
    前端代码问题页面选择项只有两个但是代码中有四个没法判断点击
    """
    # def test_my_income_search001(self):
    #     """按收入类型搜索校验"""
    #
    #     # 获取测试数据
    #     data = test_data["TestCase001"]
    #     # 打印测试用例名称
    #     self.base_page.print_case_name(data["CaseName"])
    #     # 选择支出类型
    #     self.my_income.select_income_type(income_type=data["IncomeType"])
    #     # 点击搜索
    #     self.my_income.click_search_btn()
    #     self.base_page.sleep(1)
    #     # 获取搜索后第一行所有信息
    #     first_row_info = self.my_income.get_income_first_row_info()
    #     # 断言
    #     self.assert_page.assert_in(data["expect"],first_row_info)

    def test_my_income_search002(self):
        """按服务类型搜索校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择服务类型
        self.my_income.select_server_type(server_type=data["ServerType"])
        # 点击搜索
        self.my_income.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索后第一行所有信息
        first_row_info = self.my_income.get_income_first_row_info()
        # 断言
        self.assert_page.assert_in(data["ServerType"],first_row_info)

    def test_my_income_search003(self):
        """按服务师傅名称搜索校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入师傅名称
        self.my_income.input_server_master_name(master_name=data["MasterName"])
        # 点击搜索
        self.my_income.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索后第一行所有信息
        first_row_info = self.my_income.get_income_first_row_info()
        # 断言
        self.assert_page.assert_in(data["MasterName"],first_row_info)

    def test_my_income_search004(self):
        """按工单编号搜索校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取工单编号
        order_number = rwconfig.read_config_data(
            "for_finance_manage_search","id",orderNumPath)
        # 输入工单号
        self.my_income.input_order_number(order_number)
        # 点击搜索
        self.my_income.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索后第一行所有信息
        first_row_info = self.my_income.get_income_first_row_info()
        # 断言
        self.assert_page.assert_in(order_number,first_row_info)

    def test_my_income_search005(self):
        """按结算日期收入结算搜索校验"""

        # 获取测试数据
        data = test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取当前日期
        now_date = self.base_page.get_now_time()
        # 输入开始时间
        self.my_income.input_settle_start_time(start_time=now_date)
        # 输入结束时间
        self.my_income.input_settle_end_time(end_time=now_date)
        # 点击查询
        self.my_income.click_find_btn()
        # 获取第一行查询的日期,获取的日期包含时间需要进行分割
        get_date = self.my_income.get_income_date().split(" ")[0]
        # 断言
        self.assert_page.assert_equal(now_date,get_date)


    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(My_Income_Search)

    unittest.TextTestRunner().run(suits)