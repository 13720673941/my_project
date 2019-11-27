# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/11 17:08

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common import rwconfig
from public.page.loginPage import LoginPage
from public.page.masterReceivePage import MasterReceivePage
from public.page.companyInventoryPage import CompanyInventoryPage
import unittest

"""
师傅领取备件功能校验：
1、备件领取数量为空校验  2、备件名称为空校验  3、领取备件师傅名称为空校验  
4、师傅成功领取备件校验  5、领取页面删除备件校验
"""
# 获取测试数据
test_data = get_test_data()["MasterReceivePage"]["receive_fnc"]

class Receive_Spare_Part(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.company_sparePart = CompanyInventoryPage(cls.driver)
        cls.receive_sparePart = MasterReceivePage(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("西安好家帮家政有限公司","username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入公司库存页面
        cls.company_sparePart.enter_company_inventory_page()

    def search_receive_sparePart(self,sparePart_name):
        """定义公共搜索备件的操作"""

        # 输入备件名称
        self.company_sparePart.input_search_sparePart_name(sparePart_name)
        # 点击搜索备件
        self.company_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 勾选搜索出来的备件
        self.company_sparePart.select_first_sparePart()

    def setUp(self):

        # 刷新页面
        self.base_page.refresh_page()

    def test_receive_sparePart001(self):
        """备件领取数量为空校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索选择备件
        self.search_receive_sparePart(sparePart_name=data["SP_Name"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(master_name=data["MasterName"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],Msg)

    def test_receive_sparePart002(self):
        """备件名称为空校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(master_name=data["MasterName"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"], Msg)

    def test_receive_sparePart003(self):
        """领取备件师傅名称为空校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索选择备件
        self.search_receive_sparePart(sparePart_name=data["SP_Name"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],Msg)

    def test_receive_sparePart004(self):
        """师傅领取备件页面删除备件校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索选择备件
        self.search_receive_sparePart(sparePart_name=data["SP_Name"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(master_name=data["MasterName"])
        # 点击删除选择的备件
        self.receive_sparePart.click_delete_sparePart()
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],Msg)

    def test_receive_sparePart005(self):
        """师傅成功领取备件校验"""

        # 获取测试数据
        data = test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索选择备件
        self.search_receive_sparePart(sparePart_name=data["SP_Name"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(master_name=data["MasterName"])
        # 输入备件数量
        self.receive_sparePart.input_receive_count(receive_count=data["SP_Count"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],Msg)

    def test_receive_sparePart006(self):
        """师傅领取成功后领取记录中生成日志校验"""

        # 获取测试数据
        data = test_data["TestCase006"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 点击师傅领取记录table页面
        self.receive_sparePart.enter_receive_log_page()
        # 输入领取开始日期搜索领取记录
        self.receive_sparePart.input_receive_start_time(start_date=self.base_page.get_now_time())
        # 输入领取结束日期搜索领取记录
        self.receive_sparePart.input_receive_end_time(end_date=self.base_page.get_now_time())
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(2)
        # 获取第一行备件领取记录所有字段信息
        first_receive_log = self.receive_sparePart.get_first_search_info()
        # 断言备件名称和师傅名称
        self.assert_page.assert_in(data["expect1"],first_receive_log)
        self.assert_page.assert_in(data["expect2"],first_receive_log)

    @classmethod
    def tearDownClass(cls):

        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Receive_Spare_Part)

    unittest.TextTestRunner(verbosity=2).run(suits)