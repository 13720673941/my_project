# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/24 9:55

from public.common import rwConfig
from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.financeManagePage import FinanceManagePage
from config.pathConfig import *
import unittest

class Finance_Log_Search(unittest.TestCase):

    """ 【账单支出、收入搜索功能校验】 """

    # 实例化类
    readExcel = Read_Excel("financeSearch")

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.finance_log = FinanceManagePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"financeSearch")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")

    def setUp(self):
        # 刷新页面
        self.login.enter_first_page_review()
        # 进入工单支出页面
        self.finance_log.enter_my_expend_page()
        self.base_page.sleep(2)

    @unittest.skipUnless(readExcel.get_isRun_text("finance_search_001"),"-跳过不执行该用例")
    def test_finance_search001(self):
        """按账单编号搜索校验"""

        # 获取账单编号
        billNumber = rwConfig.read_config_data(
            "for_finance_manage_search","id",orderNumPath)
        # 写入期望值中
        Update_Excel.update_expect_data("financeSearch","finance_search_001",billNumber)
        # 获取测试数据
        data = Read_Excel("financeSearch").get_dict_data("finance_search_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入账单编号
        self.finance_log.input_bill_number(billNumber)
        # 点击搜索
        self.finance_log.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(data,self.finance_log.get_first_row_info())

    @unittest.skipUnless(readExcel.get_isRun_text("finance_search_002"),"-跳过不执行该用例")
    def test_finance_search002(self):
        """按服务账单日期搜索校验"""

        # 获取当前日期
        nowDate = self.base_page.get_now_time()
        # 写入期望值中
        Update_Excel.update_expect_data("financeSearch","finance_search_002",nowDate)
        # 获取测试数据
        data = Read_Excel("financeSearch").get_dict_data("finance_search_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入账单日期
        self.finance_log.input_bill_start_date(nowDate)
        self.finance_log.input_bill_end_date(nowDate)
        # 点击搜索
        self.finance_log.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(data,self.finance_log.get_first_row_info())

    @unittest.skipUnless(readExcel.get_isRun_text("finance_search_003"),"-跳过不执行该用例")
    def test_finance_search003(self):
        """按结算对象搜索校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("finance_search_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入结算对象
        self.finance_log.input_settle_page(data["结算对象"])
        # 点击搜索
        self.finance_log.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(data,self.finance_log.get_first_row_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Finance_Log_Search)

    unittest.TextTestRunner().run(suits)