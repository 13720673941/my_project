# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/18 10:51

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.branchStatisticsPage import BranchStatisticsPage
import unittest

class Dealer_order_statistic(unittest.TestCase):
    """ 【合作经销商工单统计功能】 """

    # 实例化类
    readExcel = Read_Excel("dealerOrderStatistic")

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
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.branch_statistic = BranchStatisticsPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "dealerOrderStatistic")
        # 登录服务商
        cls.login.login_main("T西安好家帮家政有限公司")
        # 获取经销商的名称
        cls.dealerName = rwConfig.read_config_data("T西安好家帮家政有限公司","manage_branch")
        # 进入客户订单统计页面
        cls.branch_statistic.enter_statistics_page()
        # 搜索经销商
        cls.branch_statistic.input_customer_search_keyword(cls.dealerName)
        cls.branch_statistic.click_search_btn()
        cls.base.sleep(2)
        # 获取经销商初始化的统计数据
        cls.not_finish_count = int(cls.branch_statistic.get_not_finish_count())
        cls.already_finish_count = int(cls.branch_statistic.get_already_finish_count())
        cls.negative_comment_count = int(cls.branch_statistic.get_negative_comment_count())
        cls.already_settle_count = int(cls.branch_statistic.get_already_settle_count())
        # 退出账号登陆经销商
        cls.login.click_logout_button()
        # 登录经销商账号
        cls.login.login_main(cls.dealerName)
        # 经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()

    def public_operate(self):
        """搜索经销商"""
        self.branch_statistic.enter_statistics_page()
        self.base.refresh_page()
        self.branch_statistic.input_customer_search_keyword(self.dealerName)
        self.branch_statistic.click_search_btn()
        self.base.sleep(4)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_order_statistic001"),"-跳过不执行该用例")
    def test_dealer_order_statistic001(self):
        """未完单订单数量统计校验"""

        # 获取用例测试数据
        data = self.readExcel.get_dict_data("dealer_order_statistic001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 订单派给服务商 “T西安好家帮家政有限公司”
        self.send_order.send_order_main(
            sendType=data["派单类型"],orderNumber=self.orderNumber,pageName=data["派单网点"])
        # 退出经销商
        self.base.sleep(1)
        self.login.click_logout_button()
        # 登录服务商 "西安好家帮家政有限公司"
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入经销商工单统计列表页
        self.public_operate()
        # 设置全局变量
        global new_not_finish_count
        # 获取未完单的工单数量
        new_not_finish_count = int(self.branch_statistic.get_not_finish_count())
        # 实际统计未完成的订单数量
        different_count = new_not_finish_count-self.not_finish_count
        # 断言
        self.assertMode.assert_equal(data,str(different_count))

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_order_statistic002"),"-跳过不执行该用例")
    def test_dealer_order_statistic002(self):
        """完单数量统计校验"""

        # 获取用例测试数据
        data = self.readExcel.get_dict_data("dealer_order_statistic002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入派单页面
        self.send_order.enter_send_order_page()
        # 选择工单
        self.create_order.select_operate_order(self.orderNumber)
        # 接单
        self.send_order.click_take_order()
        # 派给师傅
        self.send_order.send_order_main(
            sendType=data["派单类型"],orderNumber=self.orderNumber,pageName=data["派单师傅"])
        # 完成工单
        self.finish_order.finish_order_main(self.orderNumber)
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取完工统计的数据
        new_finish_count = int(self.branch_statistic.get_already_finish_count())
        # 前后差异
        different_count = new_finish_count-self.already_finish_count
        # 断言
        self.assertMode.assert_equal(data,str(different_count))

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_order_statistic003"),"-跳过不执行该用例")
    def test_dealer_order_statistic003(self):
        """经销商工单统计-完成服务后未完单数量减去完成订单校验"""

        # 获取用例测试数据
        data = self.readExcel.get_dict_data("dealer_order_statistic003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 在次获取未完单订单数量
        after_finish_of_not = int(self.branch_statistic.get_not_finish_count())
        # 断言
        self.assertMode.assert_equal(data,str(new_not_finish_count-after_finish_of_not))

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_order_statistic004"),"-跳过不执行该用例")
    def test_dealer_order_statistic004(self):
        """差评单单量统计校验"""

        # 获取用例测试数据
        data = self.readExcel.get_dict_data("dealer_order_statistic004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.dealerName)
        # 回访订单::差评回访
        self.visit_order.visit_order_main(orderNumber=self.orderNumber,serverStatus=data["服务态度"])
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取差评单量统计
        new_negative_count = int(self.branch_statistic.get_negative_comment_count())
        # 计算和初始化数据的差异
        different_count = new_negative_count-self.negative_comment_count
        # 断言
        self.assertMode.assert_equal(data,str(different_count))

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_order_statistic005"),"-跳过不执行该用例")
    def test_dealer_order_statistic005(self):
        """已结算单单量统计校验"""

        # 获取用例测试数据
        data = self.readExcel.get_dict_data("dealer_order_statistic005")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.dealerName)
        # 结算订单
        self.settle_order.settle_order_main(self.orderNumber)
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入经销商工单统计列表页
        self.public_operate()
        # 获取已经算订单的数量
        new_already_settle_count = int(self.branch_statistic.get_already_settle_count())
        # 获取相差的单数
        different_count = new_already_settle_count-self.already_settle_count
        # 断言
        self.assertMode.assert_equal(data,str(different_count))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Dealer_order_statistic)

    unittest.TextTestRunner().run(suits)
