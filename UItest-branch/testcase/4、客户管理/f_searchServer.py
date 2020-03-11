# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/8 18:07

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.facilitatorPage import FacilitatorPage
import unittest,ddt

@ddt.ddt
class Search_Branch(unittest.TestCase):

    """ 【搜索服务商功能】 """

    # 实例化类
    readExcel = Read_Excel("searchFacilitator")
    # ddt 测试数据用例编号
    case_list = [
        "search_facilitator_001","search_facilitator_002",
        "search_facilitator_003","search_facilitator_004"
    ]
    # 获取ddt测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.server_branch = FacilitatorPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "searchFacilitator")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入客户列表页面
        cls.server_branch.enter_customer_list_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 切换服务商列表
        self.server_branch.click_server_branch_table()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_search_serverBranch(self,ddt_data):
        """服务商列表搜索功能"""

        # 打印用例名称
        self.base.print_case_name(ddt_data)
        # 输入搜索关键字
        self.server_branch.input_search_branch_keyword(ddt_data["搜索字段"])
        # 点击搜索
        self.server_branch.click_search_branch_btn()
        # 等待搜索结果
        self.base.sleep(2)
        # 断言结果
        self.assertMode.assert_in(ddt_data,self.server_branch.get_first_branch_info())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Search_Branch("test_search_serverBranch"))

    unittest.TextTestRunner().run(suit)