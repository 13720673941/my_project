# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:33

from public.common import mytest
from public.common.assertmode import Assert
from public.common.getdata import get_test_data
from public.common.rwconfig import read_config_data
from public.common import driver
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.companyInventoryPage import CompanyInventoryPage
from public.page.newReturnFactoryPage import NewReturnFactoryPage
from public.page.inventoryAdjustPage import InventoryAdjust
import unittest
"""
网点备件新件返厂功能校验：
1、新件返厂数量不能为空校验  2、新件返厂备件数量不能大于库存校验  3、新件返厂成功校验
4、新件返厂生成日志记录校验  5、新件返厂生成待返厂校验           6、批量确认返厂校验
7、单个备件确认返厂校验
"""
# 获取测试数据
test_data = get_test_data()["ReturnFactoryPage"]

class New_SP_return(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = driver.browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.company_inventory =  CompanyInventoryPage(cls.driver)
        cls.return_factory = NewReturnFactoryPage(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        mytest.start_test()
        # 获取测试账号信息
        username = read_config_data("西安好家帮家政有限公司", "username")
        password = read_config_data("西安好家帮家政有限公司", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.company_inventory.enter_company_inventory_page()

    def search_spare_part(self,sparePart_name):
        """搜索备件"""
        self.company_inventory.input_search_sparePart_name(sparePart_name)
        self.company_inventory.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        self.base_page.refresh_page()

    def test_return_factory001(self):
        """新件返厂数量不能为空校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 选择备件
        self.company_inventory.select_first_sparePart()
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 点击保存
        self.return_factory.click_save_return()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_return_factory002(self):
        """新件返厂备件数量不能大于库存校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 选择备件
        self.company_inventory.select_first_sparePart()
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 输入备件数量
        self.return_factory.input_return_count(sp_count=data["SP_Count"])
        # 获取输入框的备件数量信息
        count_number = self.return_factory.get_count_number()
        # 断言，输入的100会自动变成备件的最大数量不等于100
        self.assert_mode.assert_not_equal(data["expect"],count_number)

    def test_return_factory003(self):
        """新件返厂成功校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 选择备件
        self.company_inventory.select_first_sparePart()
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 输入备件数量
        self.return_factory.input_return_count(sp_count=data["SP_Count"])
        # 点击保存
        self.return_factory.click_save_return()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"], system_message)

    def test_return_factory004(self):
        """新件返厂生成日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入库存调整页面
        self.inventory_adjust.enter_inventory_adjust_log_page()
        self.base_page.sleep(1)
        # 获取第一行库存调整日志记录所有信息
        first_info = self.inventory_adjust.get_first_log_info()
        # 断言
        self.assert_mode.assert_in(data["expect"],first_info)

    def test_return_factory005(self):
        """新件返厂生成待返厂校验"""

        # 获取测试数据
        data = test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 获取第一行备件的所有信息
        first_info = self.return_factory.get_first_row_log_info()
        # 断言备件名称
        self.assert_mode.assert_in(data["expect"],first_info)
        # 断言日期当天
        self.assert_mode.assert_in(self.base_page.get_now_time(),first_info)

    def test_return_factory006(self):
        """批量确认返厂校验"""

        # 获取测试数据
        data = test_data["TestCase006"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 勾选所有备件
        self.return_factory.select_all_return_sp()
        # 点击批量确认
        self.return_factory.click_batch_return_btn()
        # 输入批量返厂备注
        self.return_factory.input_batch_return_remark(return_remark=data["return_remark"])
        # 点击保存
        self.return_factory.click_confirm_batch_return()
        self.base_page.sleep(1)
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)
        # 进入已返厂列表页
        self.return_factory.enter_already_return_page()
        self.base_page.sleep(1)
        # 获取第一条已返厂信息
        already_return_info = self.return_factory.get_first_row_log_info()
        # 断言
        self.assert_mode.assert_in(data["expect1"],already_return_info)

    def test_return_factory007(self):
        """单个备件确认返厂校验"""

        # 获取测试数据
        data = test_data["TestCase007"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        self.company_inventory.enter_company_inventory_page()
        # 再次返厂剩下的5个备件
        self.test_return_factory003()
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 点击确认返厂
        self.return_factory.click_confirm_return_btn()
        # 输入批量返厂备注
        self.return_factory.input_batch_return_remark(return_remark=data["return_remark"])
        # 点击保存
        self.return_factory.click_confirm_batch_return()
        self.base_page.sleep(1)
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)
        # 进入已返厂列表页
        self.return_factory.enter_already_return_page()
        self.base_page.sleep(1)
        # 获取第一条已返厂信息
        already_return_info = self.return_factory.get_first_row_log_info()
        # 断言
        self.assert_mode.assert_in(data["expect1"], already_return_info)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(New_SP_return)

    unittest.TextTestRunner().run(suits)

