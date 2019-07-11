#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/28 10:47

from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.manageBranchPage import DealerBranchPage
import unittest,ddt
"""
邀请经销商功能测试：
1、添加经销商-用户账号为空校验 2、添加经销商-用户名称为空校验 3、添加经销商-用户账号格式左边界值校验 
4、添加经销商-用户账号格式右边界值校验 5、添加经销商-用户账号格式校验 6、添加经销商-成功邀请经销商校验 
7、重复邀请校验
"""
# 获取数据
dealer_page_data = get_test_data()["AddDealerPage"]
add_dealer_data = dealer_page_data["add_branch_fnc"]
@ddt.ddt
class Visit_Dealer(unittest.TestCase):

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

    def test_visit_dealer001(self):
        """已经注册的用户可以自动带出用户名称校验"""
        # 获取测试数据
        auto_name_data = dealer_page_data["auto_name_fnc"]
        # 打印测试名称
        self.base_page.print_case_name(auto_name_data["CaseName"])
        # 点击添加经销商
        self.dealer_page.click_add_manage_branch()
        # 输入客户主账号
        self.dealer_page.input_branch_phone_num(phone_num=auto_name_data["PhoneNum"])
        self.base_page.sleep(1)
        # 获取自动带出的经销商名称
        branch_name = self.dealer_page.get_branch_name()
        # 判断
        self.assert_mode.assert_equal(auto_name_data["expect"],branch_name)

    @ddt.data(*add_dealer_data)
    def test_visit_dealer002(self,add_dealer_data):
        """添加经销商功能校验"""
        # 打印测试名称
        self.base_page.print_case_name(add_dealer_data["CaseName"])
        # 点击添加经销商
        self.dealer_page.click_add_manage_branch()
        # 输入客户主账号
        self.dealer_page.input_branch_phone_num(phone_num=add_dealer_data["PhoneNum"])
        # 输入客户名称
        self.dealer_page.input_branch_name(branch_name=add_dealer_data["RemarkName"])
        # 点击确定按钮
        self.dealer_page.click_confirm_add()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_equal(add_dealer_data["expect"],self.base_page.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览
        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suits = unittest.TestSuite()
    suits.addTest(Visit_Dealer("test_visit_dealer001"))
    suits.addTest(Visit_Dealer("test_visit_dealer002"))
    unittest.TextTestRunner().run(suits)
