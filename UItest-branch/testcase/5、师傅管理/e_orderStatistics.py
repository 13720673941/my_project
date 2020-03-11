# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/2 17:59

from public.common.basePage import BasePage
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.rwConfig import read_config_data
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.masterStatisticsPage import MasterStatisticsPage
import unittest

class Order_Statistics(unittest.TestCase):

    """ 【合作师傅工单统计功能】 """

    # 实例化
    readExcel = Read_Excel("masterStatistics")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.please_order = SendOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.order_statistics = MasterStatisticsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"masterStatistics")
        # 登录服务商
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入师傅统计列表页面
        cls.order_statistics.enter_master_order_statistics_page()
        # 获取师傅名称
        cls.master_name = read_config_data("T西安好家帮家政有限公司","master001")
        # 搜索师傅
        cls.order_statistics.input_master_keyword_search(search_word=cls.master_name)
        cls.order_statistics.click_search_btn()
        cls.base_page.sleep(1)
        # 师傅初始化接单数量
        cls.take_order_count = cls.order_statistics.get_master_take_order_count()
        # 师傅初始化已完单数量
        cls.finish_order_count = cls.order_statistics.get_master_finished_count()
        # 师傅初始化待结算数量
        cls.wait_settle_count = cls.order_statistics.get_master_wait_settle_count()
        # 师傅初始化已结算数量
        cls.already_settle_count = cls.order_statistics.get_master_already_settle_count()
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.create_order.get_order_number()
        # 网点派单
        cls.please_order.send_order_main(cls.order_number,pageName=cls.master_name)
        # 网点完成服务
        cls.finish_order.finish_order_main(ordernumber=cls.order_number)

    def search_master(self):
        # 搜索师傅
        self.order_statistics.input_master_keyword_search(self.master_name)
        self.order_statistics.click_search_btn()
        self.base_page.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_001"),"-跳过不执行该用例")
    def test_order_statistics001(self):
        """师傅接单数量同步校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("order_statistics_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入师傅工单统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新数据
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        # 获取师傅接单数量
        new_master_count = int(self.order_statistics.get_master_take_order_count())
        # 获取差异值
        diff_count = new_master_count-int(self.take_order_count)
        # 断言
        self.assert_mode.assert_equal(data,str(diff_count))

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_002"),"-跳过不执行该用例")
    def test_order_statistics002(self):
        """师傅已完单数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("order_statistics_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 获取师傅已完单数量
        new_order_count = int(self.order_statistics.get_master_finished_count())
        # 前后差异值
        diff_count = new_order_count - int(self.finish_order_count)
        # 断言
        self.assert_mode.assert_equal(data,str(diff_count))

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_003"),"-跳过不执行该用例")
    def test_order_statistics003(self):
        """师傅待结算数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("order_statistics_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 获取师傅待结算数量
        global after_finish_settle
        after_finish_settle = int(self.order_statistics.get_master_wait_settle_count())
        # 前后差异值
        diff_count = after_finish_settle - int(self.wait_settle_count)
        # 断言
        self.assert_mode.assert_equal(data,str(diff_count))

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_004"),"-跳过不执行该用例")
    def test_order_statistics004(self):
        """师傅已结算数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("order_statistics_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 回访订单
        self.visit_order.visit_order_main(self.order_number)
        # 订单结算
        self.settle_order.settle_order_main(self.order_number)
        # 返回师傅统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新数据
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        self.base_page.sleep(1)
        # 获取已经结算订单数量
        already_settle_count = int(self.order_statistics.get_master_already_settle_count())
        # 计算结算前后的订单数量差值
        diff_number = already_settle_count - int(self.already_settle_count)
        # 断言1 已结算订单 +1
        self.assert_mode.assert_equal(data,str(diff_number))

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_005"),"-跳过不执行该用例")
    def test_order_statistics005(self):
        """师傅结算后待结算-1数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("order_statistics_005")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        self.base_page.sleep(1)
        # 获取结算后待结算订单数量
        after_settle_wait = int(self.order_statistics.get_master_wait_settle_count())
        # 结算后代结算 -1
        diff = after_finish_settle - after_settle_wait
        # 断言
        self.assert_mode.assert_equal(data,str(diff))

    @unittest.skipUnless(readExcel.get_isRun_text("order_statistics_006"),"-跳过不执行该用例")
    def test_order_statistics006(self):
        """师傅好评率校验"""

        # 进入师傅统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新页面
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        self.base_page.sleep(1)
        # 获取师傅订单总数
        master_all_finish_orders = int(self.order_statistics.get_master_finished_count())
        # 获取师傅好评订单数量
        master_favorable_orders = int(self.order_statistics.get_master_good_talk_count())
        # 获取师傅好评率
        master_favorable_rate = self.order_statistics.get_master_favorable_rate_count()
        # 计算好评率,保留两位
        favorable_rate = format(((master_favorable_orders/master_all_finish_orders)*100),".2f")
        # 写入期望值
        Update_Excel.update_expect_data("masterStatistics","order_statistics_006",str(favorable_rate+"%"))
        # 获取测试数据
        data = Read_Excel("masterStatistics").get_dict_data("order_statistics_006")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 断言
        self.assert_mode.assert_equal(data,master_favorable_rate)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':
    # unittest.main()


    suits = unittest.TestLoader().loadTestsFromTestCase(Order_Statistics)
    unittest.TextTestRunner().run(suits)