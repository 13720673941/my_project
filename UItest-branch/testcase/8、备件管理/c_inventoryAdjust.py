# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/14 15:37

from public.common import mytest
from public.common import rwconfig
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.page.companyInventoryPage import CompanyInventoryPage
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.loginPage import LoginPage
import unittest
"""
网点备件库存调整功能校验：
1、调整原因不能为空校验    2、成功调整备件库存校验    3、调整库存后生成库存调整记录校验
"""
# 获取测试数据
test_data = get_test_data()["InventoryAdjustPage"]["adjust_fnc"]

class Inventory_Adjust(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.company_inventory = CompanyInventoryPage(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("西安好家帮家政有限公司", "username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.company_inventory.enter_company_inventory_page()

    def search_spare_part(self,sparePart_name):
        """工共操作搜索备件"""

        # 输入备件名称
        self.company_inventory.input_search_sparePart_name(sparePart_name)
        # 点击搜索按钮
        self.company_inventory.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        self.base_page.refresh_page()

    def test_inventory_adjust001(self):
        """调整原因不能为空校验"""

        # 获取测试i数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索调整库存的备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 点击调整库存
        self.inventory_adjust.click_inventory_adjust()
        self.base_page.sleep(1)
        # 输入备件调整后的数量
        self.inventory_adjust.input_after_adjust_inventory(after_adjust_number=data["SP_Number"])
        # 点击保存
        self.inventory_adjust.click_confirm_adjust()
        # 获取系统提示信息
        Msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],Msg)

    def test_inventory_adjust002(self):
        """成功调整备件库存校验"""

        # 获取测试i数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索调整库存的备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 点击调整库存
        self.inventory_adjust.click_inventory_adjust()
        self.base_page.sleep(1)
        # 输入备件调整后的数量
        self.inventory_adjust.input_after_adjust_inventory(after_adjust_number=data["SP_Number"])
        # 输入原因
        self.inventory_adjust.input_adjust_reason(adjust_reason=self.base_page.get_now_time())
        # 点击保存
        self.inventory_adjust.click_confirm_adjust()
        self.base_page.sleep(1)
        self.base_page.refresh_page()
        # 搜索调整库存的备件
        self.search_spare_part(sparePart_name=data["SP_Name"])
        # 获取备件总库存数量
        all_inventory_count = int(self.inventory_adjust.get_all_inventory_count())
        # 断言
        self.assert_page.assert_equal(data["expect"],all_inventory_count)

    def test_inventory_adjust003(self):
        """调整库存后生成库存调整记录校验"""

        # 获取测试i数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入库存记录页面
        self.inventory_adjust.enter_inventory_adjust_log_page()
        self.base_page.sleep(1)
        # 获取第一行数据
        first_row_info = self.inventory_adjust.get_first_log_info()
        # 断言
        self.assert_page.assert_in(data["expect"],first_row_info)

    @classmethod
    def tearDownClass(cls):

        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Inventory_Adjust)

    unittest.TextTestRunner().run(suits)