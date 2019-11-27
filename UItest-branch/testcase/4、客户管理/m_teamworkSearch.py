# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 14:22

from public.common.driver import browser_driver
from public.common.rwconfig import read_config_data
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.teamworkNewsPage import TeamWorkNewsPage
import unittest,ddt
"""
客户管理模块申请合作页面：
1、按客户名称搜索校验  2、按客户手机号搜索校验
"""
# 获取测试数据
test_data = get_test_data()["TeamWorkPage"]
ddt_data = test_data["search_teamwork_msg"]

@ddt.ddt
class Visit_News_Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.teamwork_visit = TeamWorkNewsPage(cls.driver)
        # 开始执行
        mytest.start_test()
        # 获取账号信息
        username = read_config_data("西安好家帮家政有限公司","username")
        password = read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入客户合作页面
        cls.teamwork_visit.enter_teamwork_news_page()

    @ddt.data(*ddt_data)
    def test_visit_news_search(self,ddt_data):
        """合作申请页面搜索客户校验"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 切换到发出的申请页面
        self.teamwork_visit.click_table_send_visit()
        # 输入搜索关键字
        self.teamwork_visit.input_customer_name_phone(search_word=ddt_data["keyword"])
        # 点击搜索
        self.teamwork_visit.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行字段信息
        first_row_info = self.teamwork_visit.get_first_row_info()
        # 断言
        self.assert_mode.assert_in(ddt_data["expect"],first_row_info)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Visit_News_Search)

    unittest.TextTestRunner().run(suits)







































































































































































































