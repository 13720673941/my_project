# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:56

from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.rwconfig import read_config_data
from public.common import mytest
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest,ddt
"""
师傅列表页搜索师傅测试用例：
1、按照师傅手机号搜索师傅校验 2、按照师傅名称搜索师傅校验 3、按照师傅手机号模糊搜索师傅校验 
4、按照师傅名字模糊搜索师傅校验
"""
# 获取测试数据
test_data = get_test_data()["MasterListPage"]["search_master_fnc"]

@ddt.ddt
class Master_Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        # 师傅执行测试用例
        mytest.start_test()
        # 获取网点账号信息
        username = read_config_data("西安好家帮家政有限公司","username")
        password = read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入师傅列表页面
        cls.master_page.enter_master_list_page()

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()

    @ddt.data(*test_data)
    def test_master_search001(self,test_data):
        """师傅列表搜索功能测试用例"""

        # 打印测试用例名称
        self.base_page.print_case_name(test_data["CaseName"])
        # 输入搜索关键字
        self.master_page.input_keyword_for_search(search_word=test_data["KeyWord"])
        # 点击搜搜
        self.master_page.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行师傅信息
        first_master_info = self.master_page.get_first_master_info()
        # 断言
        self.assert_mode.assert_in(test_data["expect"],first_master_info)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Search)
    unittest.TextTestRunner().run(suits)