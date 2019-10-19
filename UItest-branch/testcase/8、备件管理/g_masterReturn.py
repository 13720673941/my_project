# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:32

from public.common import mytest
from public.common import rwconfig
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common.getdata import get_test_data
from public.page.loginPage import LoginPage
from public.page.masterReturnPage import MasterReturnPage
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.companyInventoryPage import CompanyInventoryPage
from config.urlconfig import *
import unittest
"""
师傅返还备件功能测试：
1、返还备件师傅名称不能为空校验    2、返还备件名称不能为空校验      3、返还备件数量不能为空校验
4、按备件条码模糊匹配备件校验      5、按备件名称模糊匹配备件校验    6、返还的备件不能大于师傅库存备件校验
7、成功返还备件校验
"""
# 获取测试数据
test_data = get_test_data()["MasterReturnPage"]

class Master_Return(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览去驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_return = MasterReturnPage(cls.driver)
        cls.company_inventory = CompanyInventoryPage(cls.driver)
        cls.adjust_inventory = InventoryAdjust(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("蓝魔科技", "username")
        password = rwconfig.read_config_data("蓝魔科技", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.base_page.open_url(company_inventory_url)

    def search_spare_part(self,sparePart_name):

        # 搜索备件
        self.company_inventory.input_search_sparePart_name(sparePart_name)
        # 点击搜索
        self.company_inventory.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        # 刷新页面
        self.base_page.refresh_page()
        # 点击师傅返还按钮
        self.master_return.click_master_return_button()
        self.base_page.sleep(1)

    def test_master_return001(self):
        """返还备件师傅名称不能为空校验"""

        # 获取测试数据data
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 点击保存按钮
        self.master_return.click_save_button()
        # 获取系统提示信息
        message_info = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],message_info)

    def test_master_return002(self):
        """返还备件名称不能为空校验"""

        # 获取测试数据data
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 点击保存按钮
        self.master_return.click_save_button()
        # 获取系统提示信息
        message_info = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],message_info)

    def test_master_return003(self):
        """按备件条码模糊匹配备件校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 输入备件条码
        self.master_return.input_spare_part_number(sp_number=data["SP_Number"])
        self.base_page.sleep(1)
        # 获取模糊匹配的备件条码名称
        all_sp_number = self.master_return.get_search_sp_number()
        # 断言
        self.assert_page.assert_equal(data["expect"],all_sp_number)

    def test_master_return004(self):
        """按备件名称模糊匹配备件校验"""

        # 获取测试数据
        data = test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 输入备件名称
        self.master_return.input_spare_part_name(sp_name=data["SP_Name"])
        self.base_page.sleep(1)
        # 获取模糊匹配的备件条码名称
        all_sp_number = self.master_return.get_search_sp_name()
        # 断言
        self.assert_page.assert_in(data["expect"],all_sp_number)

    def test_master_return005(self):
        """返还备件数量不能为空校验"""

        # 获取测试数据data
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_name(sp_name=data["SP_Name"])
        self.base_page.sleep(1)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        # 点击保存按钮
        self.master_return.click_save_button()
        # 获取系统提示信息
        message_info = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],message_info)

    def test_master_return006(self):
        """返还的备件不能大于师傅库存备件校验"""

        # 获取测试数据data
        data = test_data["TestCase006"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_name(sp_name=data["SP_Name"])
        self.base_page.sleep(2)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        self.base_page.sleep(1)
        # 获取师傅库存数量,+1大于师傅库存数
        master_inventory = int(self.master_return.get_master_inventory_count())
        # 输入返还数量
        self.master_return.input_sp_return_count(sp_count=str(master_inventory+1))
        # 获取输入框的备件数量
        input_number = self.master_return.get_input_return_count()
        # 断言
        self.assert_page.assert_equal(str(master_inventory),input_number)

    def test_master_return007(self):
        """成功返还备件校验"""

        # 获取测试数据data
        data = test_data["TestCase007"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        self.base_page.refresh_page()
        # 搜索备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 获取备件库存数量
        before_count = int(self.adjust_inventory.get_all_inventory_count())
        self.base_page.refresh_page()
        # 点击师傅返还
        self.master_return.click_master_return_button()
        self.base_page.sleep(1)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(master_name=data["MasterName"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_name(sp_name=data["SP_Name"])
        self.base_page.sleep(1)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        # 输入返还数量
        self.master_return.input_sp_return_count(sp_count=data["SP_Count"])
        # 点击保存
        self.master_return.click_save_button()
        self.base_page.sleep(1)
        # 搜索备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 获取备件库存数量
        after_count = int(self.adjust_inventory.get_all_inventory_count())
        # 断言,网点库存增加校验
        self.assert_page.assert_equal(data["expect"],after_count-before_count)
        # 断言，师傅库存减少校验

    @classmethod
    def tearDownClass(cls):

        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':



    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Return)

    unittest.TextTestRunner().run(suits)
