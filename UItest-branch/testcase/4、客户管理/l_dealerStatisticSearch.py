# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/18 17:25

from public.common.operateExcel import *
from public.common import myDecorator
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.branchStatisticsPage import BranchStatisticsPage
import unittest,ddt

@ddt.ddt
class Dealer_Statistics_Search(unittest.TestCase):
    """ 【合作网点工单统计搜索功能】 """

    # 实例化类
    readExcel = Read_Excel("dealerStatisticSearch")
    # ddt测试数据类型的用例编号列表
    case_list = [
        "dealer_statistic_search001","dealer_statistic_search002",
        "dealer_statistic_search003","dealer_statistic_search004"
    ]
    # 获取ddt模式测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

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
        cls.search_order = SearchOrderPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "dealerStatisticSearch")
        # 登录服务商
        cls.login.login_main("T西安好家帮家政有限公司")

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_statistics_search001(self,ddt_data):
        """客户订单统计页面搜索功能"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 进入客户统计页面
        self.branch_statistic.enter_statistics_page()
        self.base.refresh_page()
        # 输入关键搜索字
        self.branch_statistic.input_customer_search_keyword(ddt_data["搜索关键字"])
        # 点击搜索
        self.branch_statistic.click_search_btn()
        self.base.sleep(1)
        # 获取搜索后的经销商所有信息
        search_after_info = self.branch_statistic.get_after_search_customer_info()
        # 断言
        self.assertMode.assert_in(ddt_data,search_after_info)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_statistic_search005"),"-跳过不执行该用例")
    def test_statistics_search002(self):
        """按下单时间搜索订单统计数量的校验"""

        data = self.readExcel.get_dict_data("dealer_statistic_search005")
        # 获取当天的该经销商所有订单数量
        self.search_order.enter_search_order_page()
        # 点击更多条件搜索
        self.search_order.click_search_more()
        # 选择工单来源
        self.search_order.select_order_from(data["工单来源"])
        # 下单日期当前时间
        self.search_order.input_create_start_date(self.base.get_now_time())
        self.search_order.input_create_end_date(self.base.get_now_time())
        # 点击搜索
        self.search_order.click_more_search_btn()
        # 等待搜索结果
        self.base.sleep(5)
        # 获取订单数量: 共 x 条
        order_count_str = self.search_order.search_order_count()
        # 处理数据
        order_count = int(order_count_str.split(" ")[1])
        # 写入期望值
        Update_Excel.update_expect_data(
            "dealerStatisticSearch", "dealer_statistic_search005", order_count)
        # 获取测试数据
        data1 = Read_Excel("dealerStatisticSearch").get_dict_data("dealer_statistic_search005")
        # 打印测试用例名称
        self.base.print_case_name(data1)
        # 进入客户工单统计页面
        self.branch_statistic.enter_statistics_page()
        self.base.refresh_page()
        # 搜索当天订单数量
        self.branch_statistic.input_customer_search_keyword(data1["工单来源"])
        # 下单时间
        self.branch_statistic.input_start_date(self.base.get_now_time())
        self.branch_statistic.input_end_date(self.base.get_now_time())
        # 点击搜索
        self.branch_statistic.click_search_btn()
        # 等待搜索结果
        self.base.sleep(1)
        # 获取经销商的已完单和未完单数量
        not_finish_count = int(self.branch_statistic.get_not_finish_count())
        finish_count = int(self.branch_statistic.get_already_finish_count())
        # 断言
        self.assertMode.assert_equal(data1,str(not_finish_count+finish_count))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Dealer_Statistics_Search)

    unittest.TextTestRunner().run(suit)

