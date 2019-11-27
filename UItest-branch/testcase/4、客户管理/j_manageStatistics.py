# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/18 10:51

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
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.branchStatisticsPage import BranchStatisticsPage
import unittest
"""
经销商客户工单统计数据测试用例：
1、已结单订单数量统计 2、已完单订单数量统计 3、未完单订单数量统计 4、差评单订单数量统计
"""
# 获取订单测试数据
test_data = get_test_data()["ManageStatisticsPage"]["order_statistics_fnc"]

class Manage_Order_Statistics(unittest.TestCase):

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
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.order_statistics = BranchStatisticsPage(cls.driver)
        # 开始用例
        mytest.start_test()
        # 获取服务商账号信息
        cls.server_use = read_config_data("西安好家帮家政有限公司","username")
        cls.server_pwd = read_config_data("西安好家帮家政有限公司","password")
        # 登录服务商
        cls.login.login_main(cls.server_use,cls.server_pwd)
        # 获取经销商的名称
        cls.manage_branch_name = read_config_data("西安好家帮家政有限公司","manage_branch")
        # 进入客户订单统计页面
        cls.order_statistics.enter_statistics_page()
        # 搜索经销商
        cls.order_statistics.input_customer_search_keyword(keyword=cls.manage_branch_name)
        cls.order_statistics.click_search_btn()
        cls.base_page.sleep(1)
        # 获取经销商初始化的统计数据
        cls.not_finish_count = int(cls.order_statistics.get_not_finish_count())
        cls.already_finish_count = int(cls.order_statistics.get_already_finish_count())
        cls.negative_comment_count = int(cls.order_statistics.get_negative_comment_count())
        cls.already_settle_count = int(cls.order_statistics.get_already_settle_count())
        # 退出账号登陆经销商
        cls.login.click_logout_button()
        # 获取经销商账号
        cls.manage_use = read_config_data(cls.manage_branch_name,"username")
        cls.manage_pwd = read_config_data(cls.manage_branch_name,"password")
        cls.login.login_main(cls.manage_use,cls.manage_pwd)
        # 获取该经销商的合作服务商名称
        cls.server_branch_name = read_config_data(cls.manage_branch_name,"branch002")
        # 经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()

    def public_operate(self):
        """搜索经销商"""
        self.order_statistics.enter_statistics_page()
        self.base_page.refresh_page()
        self.order_statistics.input_customer_search_keyword(keyword=self.manage_branch_name)
        self.order_statistics.click_search_btn()
        self.base_page.sleep(2)

    def test_order_statistics001(self):
        """未完单订单数量统计校验"""

        # 获取用例测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 订单派给服务商 “西安好家帮家政有限公司”
        self.please_order.please_order_main(ordernumber=self.order_number,
                                            pagename=self.server_branch_name,
                                            please_to_branch=True)
        # 退出经销商
        self.login.click_logout_button()
        # 登录服务商 "西安好家帮家政有限公司"
        self.login.login_main(self.server_use,self.server_pwd)
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取未完单的工单数量
        new_not_finish_count = int(self.order_statistics.get_not_finish_count())
        # 实际统计未完成的订单数量
        different_count = new_not_finish_count-self.not_finish_count
        # 断言
        self.assert_mode.assert_equal(int(data["expect"]),different_count)

    def test_order_statistics002(self):
        """完单数量统计校验"""

        # 获取用例测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取派单师傅
        master = read_config_data("西安好家帮家政有限公司","master001")
        # 选择工单
        self.please_order.enter_please_order_page()
        self.base_page.select_new_order(self.order_number)
        # 接单
        self.please_order.click_take_order()
        # 派给师傅
        self.please_order.please_order_main(self.order_number,master)
        # 完成工单
        self.finish_order.finish_order_main(self.order_number)
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取未完工的订单数量统计
        new_not_finish_count = int(self.order_statistics.get_not_finish_count())
        # 断言::完成服务后未完单 -1
        self.assert_mode.assert_equal(self.not_finish_count,new_not_finish_count)
        # 获取完工统计的数据
        new_finish_count = int(self.order_statistics.get_already_finish_count())
        # 前后差异
        different_count = new_finish_count-self.already_finish_count
        # 断言
        self.assert_mode.assert_equal(int(data["expect"]),different_count)

    def test_order_statistics003(self):
        """差评单单量统计校验"""

        # 获取用例测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_use,self.manage_pwd)
        # 回访订单::差评回访
        self.visit_order.visit_order_main(orderNumber=self.order_number,
                                          serverStatus=data["ServerStatus"])
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.server_use,self.server_pwd)
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取差评单量统计
        new_negative_count = int(self.order_statistics.get_negative_comment_count())
        # 计算和初始化数据的差异
        different_count = new_negative_count-self.negative_comment_count
        # 断言
        self.assert_mode.assert_equal(int(data["expect"]),different_count)

    def test_order_statistics004(self):
        """已结算单单量统计校验"""

        # 获取用例测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_use,self.manage_pwd)
        # 进入结算订单页面
        self.settle_order.enter_branch_settle_page()
        # 进入订单详情页
        self.base_page.open_order_message(self.order_number)
        # 点击结算
        self.settle_order.click_settle_btn()
        # 选择线下结算
        self.settle_order.select_line_down_pay()
        # 确定支付
        self.settle_order.click_confirm_pay()
        self.base_page.refresh_page()
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.server_use,self.server_pwd)
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取已经算订单的数量
        new_already_settle_count = int(self.order_statistics.get_already_settle_count())
        # 获取相差的单数
        different_count = new_already_settle_count-self.already_settle_count
        # 断言
        self.assert_mode.assert_equal(int(data["expect"]),different_count)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestSuite()
    suits.addTest(Manage_Order_Statistics("test_order_statistics001"))
    suits.addTest(Manage_Order_Statistics("test_order_statistics002"))
    suits.addTest(Manage_Order_Statistics("test_order_statistics003"))
    suits.addTest(Manage_Order_Statistics("test_order_statistics004"))

    unittest.TextTestRunner().run(suits)
