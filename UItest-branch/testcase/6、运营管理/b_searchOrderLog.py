# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/20 17:08

from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.common import rwConfig
from public.page.loginPage import LoginPage
from public.page.orderLogPage import OrderLogPage
from config.pathConfig import *
from public.common.operateExcel import *
import unittest

class Search_Order_Log(unittest.TestCase):

    """ 【扣除工单日志搜索功能】 """

    # 实例化类
    readExcel = Read_Excel("searchOrderLog")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.order_log = OrderLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"searchOrderLog")
        # 登录
        cls.login.login_main("T西安超级售后有限公司")
        # 进入工单日志页面
        cls.order_log.enter_order_log_page()
        # 页面加载
        cls.base_page.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("search_order_log_001"),"-跳过不执行")
    def test_order_log001(self):
        """按下单日期搜索扣除订单的记录信息"""

        # 写入当前日期
        Update_Excel.update_expect_data(
            "searchOrderLog","search_order_log_001",self.base_page.get_now_time())
        # 获取测试数据
        data = Read_Excel("searchOrderLog").get_dict_data("search_order_log_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入开始日期
        self.order_log.input_start_date(self.base_page.get_now_time())
        # 输入结束日期
        self.order_log.input_end_date(self.base_page.get_now_time())
        # 点击搜索按钮
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(data,first_log_info)

    @unittest.skipUnless(readExcel.get_isRun_text("search_order_log_002"),"-跳过不执行")
    def test_order_log002(self):
        """按扣除类型搜索日志记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("search_order_log_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 刷新页面
        self.base_page.refresh_page()
        # 选择类型信息
        self.order_log.select_deduct_type(data["扣除类型"])
        # 点击搜索
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(data,first_log_info)

    @unittest.skipUnless(readExcel.get_isRun_text("search_order_log_003"),"-跳过不执行")
    def test_order_log003(self):
        """按工单编号搜索订单余量扣除记录校验"""

        # 获取工单编号- 关联扣除单量脚本中创建的订单单号
        orderNumber = rwConfig.read_config_data("for_order_log_search","id",orderNumPath)
        # 工单编号写期望值中
        Update_Excel.update_expect_data("searchOrderLog","search_order_log_003",orderNumber)
        # 获取测试数据
        data = Read_Excel("searchOrderLog").get_dict_data("search_order_log_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 刷新页面
        self.base_page.refresh_page()
        # 输入工单编号
        self.order_log.input_order_number(orderNumber)
        # 点击搜索
        self.order_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_log_info = self.order_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(data,first_log_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Search_Order_Log)

    unittest.TextTestRunner().run(suits)