#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 15:11

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.dealerPage import DealerPage
import unittest,ddt

@ddt.ddt
class Search_Dealer(unittest.TestCase):

    """ 【经销商列表搜索功能】 """

    # 实例化类
    read_excel = Read_Excel("searchDealer")
    # ddt 测试用例集合
    case_list = [
        "search_dealer_001","search_dealer_002"
    ]
    # 获取ddt类型测试数据
    ddt_data = read_excel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.manage_branch = DealerPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "searchDealer")
        # 登录测试网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入经销商列表页面
        cls.manage_branch.enter_dealer_page()

    def setUp(self):
        self.base.refresh_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_search_dealer(self,ddt_data):
        """搜索经销商功能校验"""

        # 打印测试名称
        self.base.print_case_name(ddt_data)
        # 输入搜索关键字
        self.manage_branch.input_search_message(ddt_data["搜索字段"])
        # 点击搜索
        self.manage_branch.click_search()
        self.manage_branch.sleep(1)
        # 输出第一行的所有数据字段
        first_branch_info = self.manage_branch.get_first_branch_info()
        # 断言
        self.assert_mode.assert_in(ddt_data,first_branch_info)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Search_Dealer)
    unittest.TextTestRunner().run(suits)