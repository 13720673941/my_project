# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:57

from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.rwconfig import read_config_data
from public.common import mytest
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.masterListPage import MasterListPage
from config.pathconfig import *
import unittest
"""
师傅列表操作功能测试用例：
1、师傅禁止派单功能校验 2、师傅恢复派单功能校验 3、撤销师傅邀请校验
"""
# 获取测试数据路径
test_data = get_test_data()["MasterListPage"]["master_operate_fnc"]

class Master_List_Operate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        # 师傅执行测试用例
        mytest.start_test()
        # 获取网点账号信息
        username = read_config_data("蓝魔科技", "username")
        password = read_config_data("蓝魔科技", "password")
        # 登录网点
        cls.login.login_main(username, password)
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()

    def public_operate(self,search_word):
        """进入师傅列表页->搜索师傅"""

        self.master_page.enter_master_list_page()
        self.base_page.refresh_page()
        self.master_page.input_keyword_for_search(search_word)
        self.master_page.click_search_btn()
        self.base_page.sleep(1)

    def please_operate(self,name):
        """进入派单页面->选择订单->搜索派单师傅"""

        # 进入派单列表
        self.please_order.enter_please_order_page()
        # 选择订单
        self.base_page.select_new_order(self.order_number)
        # 点击派单
        self.please_order.click_pleaseOrder_btn()
        self.base_page.sleep(1)
        # 搜索派单师傅
        self.please_order.input_search_name(name)
        # 点击搜索
        self.please_order.click_search_btn()

    def test_master_list_operate001(self):
        """师傅禁止派单功能校验"""

        # 获取测试数据
        data = test_data["stop_please"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索禁止派单的师傅
        self.public_operate(search_word=data["MasterName"])
        # 点击禁止派单
        self.master_page.click_master_stop_please()
        # 确定禁止派单
        self.master_page.click_confirm_window_operate()
        # 进入派单师傅列表搜索师傅
        self.please_operate(name=data["MasterName"])
        # 等待页面加载
        self.base_page.sleep(1)
        # 断言 判断师傅不存在页面
        self.assert_mode.assert_el_not_in_page(self.please_order.search_branch_is_display())

    def test_master_list_operate002(self):
        """师傅恢复派单功能校验"""

        # 获取测试数据
        data = test_data["open_please"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索恢复派单的师傅
        self.public_operate(search_word=data["MasterName"])
        # 点击恢复派单
        self.master_page.click_master_open_please()
        # 进入派单师傅列表
        self.please_operate(name=data["MasterName"])
        # 等待页面加载
        self.base_page.sleep(1)
        # 断言 判断师傅存在页面
        self.assert_mode.assert_el_in_page(self.please_order.search_branch_is_display())

    def test_master_list_operate003(self):
        """师傅撤销邀请功能校验"""

        # 获取测试数据
        data = test_data["del_visit_master"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索师傅
        self.public_operate(search_word=data["MasterName"])
        # 点击撤销按钮
        self.master_page.click_del_visit_master()
        # 确认撤销
        self.master_page.click_confirm_window_operate()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)


    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls().base_page.quit_browser()
        # 结束脚本
        mytest.end_test()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_List_Operate)
    unittest.TextTestRunner().run(suits)