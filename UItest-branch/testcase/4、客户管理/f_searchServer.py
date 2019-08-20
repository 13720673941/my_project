# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/8 18:07

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.rwconfig import read_config_data
from public.common import mytest
from public.page.loginPage import LoginPage
from public.page.serverBranchPage import ServerBranchPage
import unittest,ddt
"""
服务商列表搜索服务商功能：
1、按照客户手机号搜索校验 2、按照客户名称搜索校验 3、按客户名称模糊搜索校验 4、按客户手机号模糊搜索校验
"""
# 获取测试数据
search_data = get_test_data()["AddServerPage"]["search_branch_fnc"]

@ddt.ddt
class Search_Branch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.server_branch = ServerBranchPage(cls.driver)
        # 开始运行
        mytest.start_test()
        # 获取网点账号密码
        cls.username = read_config_data("蓝魔科技","username")
        cls.password = read_config_data("蓝魔科技","password")
        # 网点登录
        cls.login.login_main(cls.username,cls.password)
        # 进入客户列表页面
        cls.server_branch.enter_customer_list_page()

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()
        # 切换服务商列表
        self.server_branch.click_server_branch_table()

    @ddt.data(*search_data)
    def test_search_serverBranch(self,search_data):
        """服务商列表搜索功能"""

        # 打印用例名称
        self.base_page.print_case_name(search_data["CaseName"])
        # 输入搜索关键字
        self.server_branch.input_search_branch_keyword(branch_keyword=search_data["SearchWord"])
        # 点击搜索
        self.server_branch.click_search_branch_btn()
        # 等待搜索结果
        self.base_page.sleep(1)
        # 获取搜索结果
        search_result = self.server_branch.get_first_branch_info()
        # 断言结果
        self.assert_mode.assert_in(search_data["expect"],search_result)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()



if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Search_Branch("test_search_serverBranch"))

    unittest.TextTestRunner().run(suit)