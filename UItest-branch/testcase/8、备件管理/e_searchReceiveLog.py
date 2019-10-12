# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/12 10:56

from public.common import mytest
from public.common import rwconfig
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.page.loginPage import LoginPage
from public.page.masterReceivePage import MasterReceivePage
import unittest,ddt
"""
师傅领取备件页面搜索功能测试用例：
1、按领取备件师傅名称搜索校验 2、按领取备件时间搜索校验  3、按领取备件条码搜索校验    
4、按领取备件名称搜索校验   5、备件领取记录混合搜索校验
"""
# 获取测试数据
ddt_data = get_test_data()["MasterReceivePage"]["log_search_fnc"]

@ddt.ddt
class Search_Receive_Log(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.receive_sparePart = MasterReceivePage(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("蓝魔科技", "username")
        password = rwconfig.read_config_data("蓝魔科技", "password")
        # 登录网点
        cls.login.login_main(username, password)

    def setUp(self):
        # 刷新清除数据
        self.base_page.refresh_page()
        # 进入师傅领取记录页面
        self.receive_sparePart.enter_receive_log_page()
        self.base_page.sleep(1)

    @ddt.data(*ddt_data)
    def test_search_receive_log001(self,ddt_data):
        """师傅领取备件记录页面搜索功能"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(master_name=ddt_data["MasterName"])
        # 输入开始日期
        self.receive_sparePart.input_receive_start_time(start_date=ddt_data["ReceiveTime"])
        # 输入结束日期
        self.receive_sparePart.input_receive_end_time(end_date=ddt_data["ReceiveTime"])
        # 输入备件条码
        self.receive_sparePart.input_sparePart_number(spartPart_number=ddt_data["SP_Number"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(sparePart_name=ddt_data["SP_Name"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索结果第一行数据
        first_search_info = self.receive_sparePart.get_first_search_info()
        # 断言
        self.assert_page.assert_in(ddt_data["expect"],first_search_info)

    @classmethod
    def tearDownClass(cls):

        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Search_Receive_Log)

    unittest.TextTestRunner(verbosity=2).run(suits)