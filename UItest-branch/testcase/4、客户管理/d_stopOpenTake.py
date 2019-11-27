#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 15:14

from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.manageBranchPage import DealerBranchPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
import unittest
"""
经销商暂停恢复接单功能：
1、暂停接单经销商不能选择该服务撒派单校验 2、恢复接单经销商可以选择该服务商派单校验
"""
# 获取数据
dealer_page_data = get_test_data()["AddDealerPage"]

class Stop_Open_TakeOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览驱动
        cls.driver = browser_driver()
        # 实例化
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.dealer_page = DealerBranchPage(cls.driver)
        cls.create_order_page = AddOrderPage(cls.driver)
        cls.please_order_page = PleaseOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 登录经销账号下单
        cls.manage_branch_use = read_config_data("西安超级售后有限公司","username")
        cls.manage_branch_pwd = read_config_data("西安超级售后有限公司","password")
        cls.login.login_main(cls.manage_branch_use,cls.manage_branch_pwd)
        #  经销商下单程序下单
        cls.create_order_page.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()
        # 退出登录
        cls.login.click_logout_button()
        # 获取网点账号密码
        cls.username = read_config_data("西安好家帮家政有限公司","username")
        cls.password = read_config_data("西安好家帮家政有限公司","password")
        # 登录服务商网点
        cls.login.login_main(cls.username,cls.password)
        # 进入邀请经销商页面
        cls.dealer_page.enter_dealer_page()

    def setUp(self):
        self.base_page.refresh_page()

    def test_stop_open_takeOrder001(self):
        """暂停接单功能校验"""
        # 获取测试数据
        stop_take_data = dealer_page_data["stop_take_fnc"]
        # 打印测试名称
        self.base_page.print_case_name(stop_take_data["CaseName"])
        # 搜索经销商
        self.dealer_page.input_search_message(search_info=stop_take_data["StopTakeBranch"])
        # 点击搜索
        self.dealer_page.click_search()
        # 点击暂停接单
        self.dealer_page.click_stop_take_order()
        # 点击暂停接单确定
        self.dealer_page.click_stop_take_confirm()
        self.base_page.sleep(2)
        # 输出第一行的所有数据字段
        first_branch_info = self.dealer_page.get_first_branch_info()
        # 断言
        self.assert_mode.assert_in(stop_take_data["expect"],first_branch_info)
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_branch_use,self.manage_branch_pwd)
        # 进入派单页面
        self.please_order_page.enter_please_order_page()
        # 选择订单
        self.base_page.select_new_order(self.order_number)
        # 点击派单
        self.please_order_page.click_pleaseOrder_btn()
        # 选择派单服务商
        self.please_order_page.please_to_branch()
        self.base_page.sleep(1)
        # 搜索服务商名称
        self.please_order_page.input_search_branch_name(branch_name=stop_take_data["BranchName"])
        # 点击搜索
        self.please_order_page.click_search_branch()
        self.base_page.sleep(2)
        # 验证是否有暂停接单字段
        self.assert_mode.assert_el_in_page(self.please_order_page.stop_take_order_is_displayed())

    def test_stop_open_takeOrder002(self):
        """开启接单功能校验"""
        # 获取测试数据
        open_take_data = dealer_page_data["open_take_fnc"]
        # 打印测试名称
        self.base_page.print_case_name(open_take_data["CaseName"])
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务撒
        self.login.login_main(self.username,self.password)
        # 进入客户列表
        self.dealer_page.enter_dealer_page()
        # 搜索经销商
        self.dealer_page.input_search_message(search_info=open_take_data["OpenTakeBranch"])
        # 点击搜索
        self.dealer_page.click_search()
        # 点击恢复接单
        self.dealer_page.click_open_take_order()
        # 点击恢复接单确定
        self.dealer_page.click_open_take_confirm()
        self.base_page.sleep(2)
        # 输出第一行的所有数据字段
        first_branch_info = self.dealer_page.get_first_branch_info()
        # 断言
        self.assert_mode.assert_in(open_take_data["expect"],first_branch_info)
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_branch_use,self.manage_branch_pwd)
        # 进入派单页面
        self.please_order_page.enter_please_order_page()
        # 选择订单
        self.base_page.select_new_order(self.order_number)
        # 点击派单
        self.please_order_page.click_pleaseOrder_btn()
        # 选择派单服务商
        self.please_order_page.please_to_branch()
        self.base_page.sleep(1)
        # 搜索服务商名称
        self.please_order_page.input_search_branch_name(branch_name=open_take_data["BranchName"])
        # 点击搜索
        self.please_order_page.click_search_branch()
        self.base_page.sleep(2)
        # 验证是否有暂停接单字段
        self.assert_mode.assert_el_not_in_page(self.please_order_page.stop_take_order_is_displayed())

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Stop_Open_TakeOrder("test_stop_open_takeOrder001"))
    suit.addTest(Stop_Open_TakeOrder("test_stop_open_takeOrder002"))
    unittest.TextTestRunner().run(suit)
