# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/22 11:50

from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.common import rwConfig
from public.page.loginPage import LoginPage
from public.page.shortMsgLogPage import ShortMsgLogPage
from config.pathConfig import *
import unittest

class Search_ShortMsg_Log(unittest.TestCase):

    """ 【扣除短信日志搜索功能】 """

    # 实例化类
    readExcel = Read_Excel("searchShortMsg")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.shortMsg_log = ShortMsgLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "searchShortMsg")
        # 登录
        cls.login.login_main("T西安超级售后有限公司")
        # 进入短信发送记录页面
        cls.shortMsg_log.enter_short_msg_list_page()

    def setUp(self):

        # 刷新清除页面历史纪录
        self.base_page.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("search_shortMsg_log_001"),"-跳过不执行")
    def test_search_shortMsg_log001(self):
        """按工单编号搜索短信发送记录校验"""

        # 获取工单编号
        order_number = rwConfig.read_config_data(
            "for_shortMsg_log_search","id",orderNumPath)
        # 单号写入期望值中
        Update_Excel.update_expect_data(
            "searchShortMsg","search_shortMsg_log_001",order_number)
        # 获取测试数据
        data = Read_Excel("searchShortMsg").get_dict_data("search_shortMsg_log_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入工单编号
        self.shortMsg_log.input_order_number(order_number)
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行搜索后的信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(data,first_row_info)

    @unittest.skipUnless(readExcel.get_isRun_text("search_shortMsg_log_002"),"-跳过不执行")
    def test_search_shortMsg_log002(self):
        """按短信类型搜索短信发送记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("search_shortMsg_log_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择短信类型
        self.shortMsg_log.select_short_msg_type(data["短信类型"])
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言 判断搜索
        self.assert_mode.assert_in(data,first_row_info)

    @unittest.skipUnless(readExcel.get_isRun_text("search_shortMsg_log_003"),"-跳过不执行")
    def test_search_shortMsg_log003(self):
        """按手机号搜索短信发送记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("search_shortMsg_log_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 输入手机号
        self.shortMsg_log.input_phe_number(data["手机号码"])
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言 判断搜索
        self.assert_mode.assert_in(data,first_row_info)

    @unittest.skipUnless(readExcel.get_isRun_text("search_shortMsg_log_004"),"-跳过不执行")
    def test_search_shortMsg_log004(self):
        """按发送日期搜索短信发送记录校验"""

        # 单号写入期望值中
        Update_Excel.update_expect_data(
            "searchShortMsg","search_shortMsg_log_004",self.base_page.get_now_time())
        # 获取测试数据
        data = Read_Excel("searchShortMsg").get_dict_data("search_shortMsg_log_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 当前日期
        now_date = self.base_page.get_now_time()
        # 输入手机发送短信剋是日期
        self.shortMsg_log.input_send_start_time(send_start_time=now_date)
        # 输入手机发送短信结束日期
        self.shortMsg_log.input_send_end_time(send_end_time=now_date)
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言 判断搜索
        self.assert_mode.assert_in(data,first_row_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Search_ShortMsg_Log)

    unittest.TextTestRunner(verbosity=2).run(suits)