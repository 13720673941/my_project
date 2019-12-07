# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/22 11:50

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.shortMsgLogPage import ShortMsgLogPage
from config.pathconfig import *
import unittest
"""
短信发送记录日志筛选功能：
1、按工单编号搜索短信发送记录校验  2、按短信类型搜索短信发送记录校验  
3、按手机号搜索短信发送记录校验  4、按发送日期搜索短信发送记录校验
"""
# 获取测试数据
test_data = get_test_data()["ShortMsgLogPage"]["search_log_fnc"]

class Search_ShortMsg_Log(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.shortMsg_log = ShortMsgLogPage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        mytest.start_test()
        # 获取网点登录账号信息
        username = read_config_data("西安超级售后有限公司", "username")
        password = read_config_data("西安超级售后有限公司", "password")
        # 登录
        cls.login.login_main(username, password)
        # 进入短信发送记录页面
        cls.shortMsg_log.enter_short_msg_list_page()

    def setUp(self):

        # 刷新清除页面历史纪录
        self.base_page.refresh_page()

    def test_search_shortMsg_log001(self):
        """按工单编号搜索短信发送记录校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取工单编号
        order_number = read_config_data("for_operate_log_search","id",orderNumPath)
        # 输入工单编号
        self.shortMsg_log.input_order_number(order_number=order_number)
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行搜索后的信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(order_number,first_row_info)

    def test_search_shortMsg_log002(self):
        """按短信类型搜索短信发送记录校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择短信类型
        self.shortMsg_log.select_short_msg_type(value=data["ShortMsgType"])
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言 判断搜索
        self.assert_mode.assert_in(data["ShortMsgType"],first_row_info)

    def test_search_shortMsg_log003(self):
        """按手机号搜索短信发送记录校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入手机号
        self.shortMsg_log.input_phe_number(phone_number=data["PhoneNum"])
        # 点击搜索
        self.shortMsg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行信息
        first_row_info = self.shortMsg_log.get_first_row_info()
        # 断言 判断搜索
        self.assert_mode.assert_in(data["PhoneNum"],first_row_info)

    def test_search_shortMsg_log004(self):
        """按发送日期搜索短信发送记录校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
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
        self.assert_mode.assert_in(now_date,first_row_info)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Search_ShortMsg_Log)

    unittest.TextTestRunner(verbosity=2).run(suits)