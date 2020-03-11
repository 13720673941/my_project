# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:56

from public.common.operateExcel import *
from public.common import myDecorator
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest,ddt

@ddt.ddt
class Master_Search(unittest.TestCase):

    """ 【师傅列表搜索功能】 """

    # 实例化
    readExcel = Read_Excel("masterSearch")
    # ddt测试类型用例编号
    case_list = [
        "master_search_001","master_search_002",
        "master_search_003","master_search_004"
    ]
    # 获取ddt测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"masterSearch")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入师傅列表页面
        cls.master_page.enter_master_list_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_master_search001(self,ddt_data):
        """师傅列表搜索功能测试用例"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 输入搜索关键字
        self.master_page.input_keyword_for_search(ddt_data["搜索字段"])
        # 点击搜索
        self.master_page.click_search_btn()
        self.base.sleep(1)
        # 获取第一行师傅信息
        first_master_info = self.master_page.get_first_master_info()
        # 断言
        self.assert_mode.assert_in(ddt_data,first_master_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Search)

    unittest.TextTestRunner().run(suits)