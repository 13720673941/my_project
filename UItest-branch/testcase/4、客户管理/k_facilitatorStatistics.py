# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 10:12

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

class Facilitator_branch_statistic(unittest.TestCase):
    """ 【合作服务商工单统计功能】 """

    # 实例化类
    readExcel = Read_Excel("facilitatorOrderStatistic")

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
        cls.assertMode = Assert(cls.driver, "facilitatorOrderStatistic")
        # 登录服务商
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入订单统计页面
        cls.branch_statistic.enter_statistics_page()
        # 点击table切换服务商
        cls.branch_statistic.click_table_to_server()
        # 获取网点：西安好家帮家政有限公司 的合作服务商
        cls.facilitatorName = rwConfig.read_config_data("T西安好家帮家政有限公司","branch001")
        # 搜索该服务商
        cls.branch_statistic.input_customer_search_keyword(cls.facilitatorName)
        # 点击搜索
        cls.branch_statistic.click_search_btn()
        cls.base.sleep(4)
        # 获取服务商初始化数据
        cls.not_finish_count = int(cls.branch_statistic.get_not_finish_count())
        cls.already_finish_count = int(cls.branch_statistic.get_already_finish_count())
        cls.wait_settle_count = int(cls.branch_statistic.get_wait_settle_count())
        cls.already_settle_count = int(cls.branch_statistic.get_already_settle_count())
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()
    
    def public_operate(self):
        """工共操作-进入统计页面搜索服务商"""

        self.branch_statistic.enter_statistics_page()
        self.branch_statistic.click_table_to_server()
        self.branch_statistic.input_customer_search_keyword(self.facilitatorName)
        self.branch_statistic.click_search_btn()
        self.base.sleep(2)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic001"),"-跳过不执行")
    def test_facilitator_statistics001(self):
        """服务商工单统计-未完单订单数据的同步校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic001")
        # 打印测试用例
        self.base.print_case_name(data)
        # 派单给服务商
        self.send_order.send_order_main(
            self.orderNumber,sendType=data["派单类型"],pageName=self.facilitatorName)
        # 进入订单统计页面搜索服务商
        self.public_operate()
        # 获取该服务商未完单数量
        global new_not_finish_count
        new_not_finish_count = int(self.branch_statistic.get_not_finish_count())
        # 断言
        self.assertMode.assert_equal(data,str(new_not_finish_count-self.not_finish_count))

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic002"),"-跳过不执行")
    def test_facilitator_statistics002(self):
        """服务商工单统计-已完单订单数据的同步校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic002")
        # 打印测试用例
        self.base.print_case_name(data)
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.facilitatorName)
        # 派单到师傅
        self.send_order.send_order_main(
            self.orderNumber,sendType=data["派单类型"],pageName=data["派单师傅"],takeOrder=True)
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        self.base.refresh_page()
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入服务商订单统计页面
        self.public_operate()
        # 获取已完单数量
        finish_order_count = int(self.branch_statistic.get_already_finish_count())
        # 断言: 已完单 +1
        self.assertMode.assert_equal(data,str(finish_order_count-self.already_finish_count))

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic003"),"-跳过不执行")
    def test_facilitator_statistics003(self):
        """服务商工单统计-未完单中减去已完成订单数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic003")
        # 打印测试用例
        self.base.print_case_name(data)
        # 完成服务工单再次获取未完单
        after_finish_count = int(self.branch_statistic.get_not_finish_count())
        # 断言: 未完单 -1
        self.assertMode.assert_equal(data,str(new_not_finish_count-after_finish_count))

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic004"),"-跳过不执行")
    def test_facilitator_statistics004(self):
        """服务商工单统计-待结单订单数据的同步校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic004")
        # 打印测试用例
        self.base.print_case_name(data)
        # 获取待结算订单数量
        global new_wait_settle_count
        new_wait_settle_count = int(self.branch_statistic.get_wait_settle_count())
        # 断言 待结算 +1
        self.assertMode.assert_equal(data,str(new_wait_settle_count-self.wait_settle_count))

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic005"),"-跳过不执行")
    def test_facilitator_statistics005(self):
        """服务商工单统计-已结单订单数据的同步校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic005")
        # 打印测试用例
        self.base.print_case_name(data)
        # 回访订单
        self.visit_order.visit_order_main(self.orderNumber)
        # 订单结算
        self.settle_order.settle_order_main(self.orderNumber)
        self.base.sleep(1)
        # 进入订单统计页面
        self.public_operate()
        # 获取已结算订单数量
        new_already_settle_count = int(self.branch_statistic.get_already_settle_count())
        # 断言: 已结算订单数量 +1
        self.assertMode.assert_equal(data,str(new_already_settle_count-self.already_settle_count))

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_order_statistic006"),"-跳过不执行")
    def test_facilitator_statistics006(self):
        """服务商工单统计-待结单中减去已结单订单数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_order_statistic006")
        # 打印测试用例
        self.base.print_case_name(data)
        # 获取待结算订单数量
        after_settle_count = int(self.branch_statistic.get_wait_settle_count())
        # 断言: 待结算订单数量 -1
        self.assertMode.assert_equal(data,str(new_wait_settle_count-after_settle_count))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Facilitator_branch_statistic)

    unittest.TextTestRunner().run(suits)

