# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 10:12

from public.common.driver import browser_driver
from public.common import mytest
from config.pathconfig import *
from public.common.rwconfig import read_config_data
from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.assertmode import Assert
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.settleOrderPage import SettleOrderPage
from public.page.branchStatisticsPage import BranchStatisticsPage
import unittest
"""
合作服务商订单统计测试用例：
1、未完单订单数据的同步校验 2、已完单订单数据的同步校验 3、待结单订单数据的同步校验
4、已结单订单数据的同步校验
"""
# 获取订单测试数据
test_data = get_test_data()["ServerStatisticsPage"]["order_statistics_fnc"]

class Server_Order_Statistics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.order_statistics = BranchStatisticsPage(cls.driver)
        # 开始用例
        mytest.start_test()
        # 获取经销商账号信息
        cls.manage_use = read_config_data("蓝魔科技","username")
        cls.manage_pwd = read_config_data("蓝魔科技","password")
        # 登录服务商
        cls.login.login_main(cls.manage_use,cls.manage_pwd)
        # 进入订单统计页面
        cls.order_statistics.enter_statistics_page()
        # 点击table切换服务商
        cls.order_statistics.click_table_to_server()
        # 获取网点：蓝魔科技 的合作服务商
        cls.server_branch_name = read_config_data("蓝魔科技","branch001")
        # 搜索该服务商
        cls.order_statistics.input_customer_search_keyword(keyword=cls.server_branch_name)
        # 点击搜索
        cls.order_statistics.click_search_btn()
        cls.base_page.sleep(1)
        # 获取服务商初始化数据
        cls.not_finish_count = int(cls.order_statistics.get_not_finish_count())
        cls.already_finish_count = int(cls.order_statistics.get_already_finish_count())
        cls.wait_settle_count = int(cls.order_statistics.get_wait_settle_count())
        cls.already_settle_count = int(cls.order_statistics.get_already_settle_count())
        # 获取订单信息
        user = read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = read_config_data("NotReturnOrder", "品牌", orderInfo)
        kinds = read_config_data("NotReturnOrder", "品类", orderInfo)
        # 经销商下单程序下单
        cls.create_order.create_order_main(user, phe, address, collage, order_type, server, brands, kinds)
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()

    def public_operate(self):
        """工共操作-进入统计页面搜索服务商"""

        self.order_statistics.enter_statistics_page()
        self.order_statistics.click_table_to_server()
        self.order_statistics.input_customer_search_keyword(keyword=self.server_branch_name)
        self.order_statistics.click_search_btn()
        self.base_page.sleep(1)

    def test_server_statistics001(self):
        """未完单订单数量统计校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 派单给服务商
        self.please_order.please_order_main(ordernumber=self.order_number,
                                            pagename=self.server_branch_name,
                                            please_to_branch=True)
        # 进入订单统计页面搜索服务商
        self.public_operate()
        # 获取该服务商未完单数量
        new_not_finish_count = int(self.order_statistics.get_not_finish_count())
        # 断言
        self.assert_mode.assert_equal(int(data["expect"]),new_not_finish_count-self.not_finish_count)

    def test_server_statistics002(self):
        """已完单订单数据的同步校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 退出经销商登录
        self.login.click_logout_button()
        # 获取服务商登录账号
        self.server_use = read_config_data(self.server_branch_name,"username")
        self.server_pwd = read_config_data(self.server_branch_name,"password")
        # 登录服务商
        self.login.login_main(self.server_use,self.server_pwd)
        # 获取服务商师傅
        master = read_config_data(self.server_branch_name,"master001")
        # 派单到师傅
        self.please_order.please_order_main(ordernumber=self.order_number,
                                            pagename=master)
        # 完成服务
        self.finish_order.finish_order_main(ordernumber=self.order_number)
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_use,self.manage_pwd)
        # 进入服务商订单统计页面
        self.public_operate()
        # 获取已完单数量
        finish_order_count = int(self.order_statistics.get_already_finish_count())
        # 获取未完单
        not_finish_count = int(self.order_statistics.get_not_finish_count())
        # 断言: 已完单 +1
        self.assert_mode.assert_equal(int(data["expect"]),finish_order_count-self.already_finish_count)
        # 断言: 未完单 -1
        self.assert_mode.assert_equal(not_finish_count,self.not_finish_count)

    def test_server_statistics003(self):
        """待结单订单数据的同步校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 获取待结算订单数量
        new_wait_settle_count = int(self.order_statistics.get_wait_settle_count())
        # 断言 待结算 +1
        self.assert_mode.assert_equal(int(data["expect"]),new_wait_settle_count-self.wait_settle_count)

    def test_server_statistics004(self):
        """已结单订单数据的同步校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例
        self.base_page.print_case_name(data["CaseName"])
        # 进入订单结算页面
        self.settle_order.enter_branch_settle_page()
        # 进入订单详情
        self.base_page.open_order_message(self.order_number)
        # 点击结算
        self.settle_order.click_settle_btn()
        # 选择线下支付
        self.settle_order.select_line_down_pay()
        # 确定支付
        self.settle_order.click_confirm_pay()
        self.base_page.sleep(1)
        # 进入订单统计页面
        self.public_operate()
        # 获取已结算订单数量
        new_already_settle_count = int(self.order_statistics.get_already_settle_count())
        # 获取待结算订单数量
        new_wait_settle_count = int(self.order_statistics.get_wait_settle_count())
        # 断言: 待结算订单数量 -1
        self.assert_mode.assert_equal(self.wait_settle_count,new_wait_settle_count)
        # 断言: 已结算订单数量 +1
        self.assert_mode.assert_equal(int(data["expect"]),new_already_settle_count-self.already_settle_count)

    @classmethod
    def tearDownClass(cls):

        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Server_Order_Statistics)

    unittest.TextTestRunner().run(suits)

