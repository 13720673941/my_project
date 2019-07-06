#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 15:11

from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest,writetestresult
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.manageBranchPage import DealerBranchPage
import unittest,ddt
"""
经销商列表搜索功能：
1、按手机号搜索校验 2、按名称搜索校验
"""
# 获取数据
dealer_page_data = get_test_data()["AddDealerPage"]
search_branch_data = dealer_page_data["search_branch_fnc"]
# 默认写入测试结果
isWrite=True
@ddt.ddt
class Search_Dealer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览驱动
        cls.driver = browser_driver()
        # 实例化
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.dealer_page = DealerBranchPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 获取网点账号密码
        cls.username = read_config_data("蓝魔科技","username")
        cls.password = read_config_data("蓝魔科技","password")
        # 登录网点
        cls.login.login_main(cls.username,cls.password)
        # 进入邀请经销商页面
        cls.dealer_page.enter_dealer_page()

    def setUp(self):
        self.base_page.refresh_page()

    @ddt.data(*search_branch_data)
    def test_search_dealer(self, search_branch_data):
        """搜索经销商功能校验"""
        # 打印测试名称
        self.base_page.print_case_name(search_branch_data["CaseName"])
        # 输入搜索关键字
        self.dealer_page.input_search_message(search_info=search_branch_data["SearchInfo"])
        # 点击搜索
        self.dealer_page.click_search()
        self.base_page.sleep(2)
        # 输出第一行的所有数据字段
        first_branch_info = self.dealer_page.get_first_branch_info()
        # 断言
        isSuccess = self.assert_mode.assert_in(search_branch_data["expect"],first_branch_info)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",search_branch_data["CaseName"])

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览
        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Search_Dealer("test_search_dealer"))
    unittest.TextTestRunner().run(suit)