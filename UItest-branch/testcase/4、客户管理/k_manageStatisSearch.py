# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/18 17:25

from public.common.driver import browser_driver
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.assertmode import Assert
from public.page.loginPage import LoginPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.branchStatisticsPage import BranchStatisticsPage
import unittest,ddt
"""
经销商统计列表页面搜索功能测试：
1、按客户手机号搜索客户校验 2、按客户名称搜索客户校验 3、按订单下单时间搜索订单数量统计校验
"""
# 获取测试数据
search_data = get_test_data()["ManageStatisticsPage"]
ddt_data = search_data["search_manage_fnc"]

@ddt.ddt
class ManageStatisticsSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.search_order = SearchOrderPage(cls.driver)
        cls.order_statistics = BranchStatisticsPage(cls.driver)
        # 开始执行
        mytest.start_test()
        # 获取服务商账号信息
        cls.server_use = read_config_data("蓝魔科技","username")
        cls.server_pwd = read_config_data("蓝魔科技","password")
        # 登录服务商
        cls.login.login_main(cls.server_use,cls.server_pwd)

    @ddt.data(*ddt_data)
    def test_statistics_search001(self,ddt_data):
        """客户订单统计页面搜索功能"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 进入客户统计页面
        self.order_statistics.enter_statistics_page()
        self.base_page.refresh_page()
        # 输入关键搜索字
        self.order_statistics.input_customer_search_keyword(keyword=ddt_data["search_keyword"])
        # 点击搜索
        self.order_statistics.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索后的经销商所有信息
        search_after_info = self.order_statistics.get_after_search_customer_info()
        # 断言
        self.assert_mode.assert_in(ddt_data["expect"],search_after_info)

    def test_statistics_search002(self):
        """按下单时间搜索订单统计数量的校验"""

        # 获取测试数据
        data = search_data["create_time_search_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取当天的该经销商所有订单数量
        self.search_order.enter_search_order_page()
        # 点击更多条件搜索
        self.search_order.click_search_more()
        # 选择工单来源
        self.search_order.select_order_from(value=data["OrderFrom"])
        # 下单日期当前时间
        self.search_order.input_create_start_date(self.base_page.get_now_time())
        self.search_order.input_create_end_date(self.base_page.get_now_time())
        # 点击搜索
        self.search_order.click_more_search_btn()
        # 等待搜索结果
        self.base_page.sleep(2)
        # 获取订单数量: 共 x 条
        order_count_str = self.search_order.search_order_count()
        # 处理数据
        order_count = int(order_count_str.split(" ")[1])
        # 进入客户工单统计页面
        self.order_statistics.enter_statistics_page()
        self.base_page.refresh_page()
        # 搜索当天订单数量
        self.order_statistics.input_customer_search_keyword(keyword=data["OrderFrom"])
        # 下单时间
        self.order_statistics.input_start_date(start_date=self.base_page.get_now_time())
        self.order_statistics.input_end_date(end_date=self.base_page.get_now_time())
        # 等待搜索结果
        self.base_page.sleep(1)
        # 获取经销商的已完单和未完单数量
        not_finish_count = int(self.order_statistics.get_not_finish_count())
        finish_count = int(self.order_statistics.get_already_finish_count())
        # 断言
        self.assert_mode.assert_equal(order_count,not_finish_count+finish_count)

    @classmethod
    def tearDownClass(cls):

        cls.base_page.quit_browser()
        mytest.end_test()



if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(ManageStatisticsSearch)
    unittest.TextTestRunner().run(suit)

