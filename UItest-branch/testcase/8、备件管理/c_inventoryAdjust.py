# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/14 15:37

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.spartPartListPage import SparePartListPage
import unittest

class Inventory_Adjust(unittest.TestCase):

    """ 【网点库存调整功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("inventoryAdjust")

    @classmethod
    def setUpClass(cls):

        """ 【网点备件库存调整功能校验】 """

        # 浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        cls.search_sparePart = SparePartListPage(cls.driver)
        cls.assert_page = Assert(cls.driver,"inventoryAdjust")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.search_sparePart.enter_company_inventory_page()

    def search_spare_part(self,sparePartName):
        """工共操作搜索备件"""

        # 输入备件名称
        self.search_sparePart.input_search_sparePart_name(sparePartName)
        # 点击搜索按钮
        self.search_sparePart.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        self.base_page.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("inventory_adjust_001"),"-跳过不执行")
    def test_inventory_adjust001(self):
        """调整原因不能为空校验"""

        # 获取测试i数据
        data = self.readExcel.get_dict_data("inventory_adjust_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索调整库存的备件
        self.search_spare_part(data["备件名称"])
        # 点击调整库存
        self.inventory_adjust.click_inventory_adjust()
        self.base_page.sleep(1)
        # 输入备件调整后的数量
        self.inventory_adjust.input_after_adjust_inventory(data["调整数量"])
        # 点击保存
        self.inventory_adjust.click_confirm_adjust()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("inventory_adjust_002"),"-跳过不执行")
    def test_inventory_adjust002(self):
        """成功调整备件库存校验"""

        # 获取测试i数据
        data = self.readExcel.get_dict_data("inventory_adjust_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索调整库存的备件
        self.search_spare_part(data["备件名称"])
        # 点击调整库存
        self.inventory_adjust.click_inventory_adjust()
        self.base_page.sleep(1)
        # 输入备件调整后的数量
        self.inventory_adjust.input_after_adjust_inventory(data["调整数量"])
        # 输入原因
        self.inventory_adjust.input_adjust_reason(data["调整原因"])
        # 点击保存
        self.inventory_adjust.click_confirm_adjust()
        self.base_page.sleep(1)
        self.base_page.refresh_page()
        # 搜索调整库存的备件
        self.search_spare_part(data["备件名称"])
        # 获取备件总库存数量
        all_inventory_count = self.inventory_adjust.get_all_inventory_count()
        # 断言
        self.assert_page.assert_equal(data,str(all_inventory_count))

    @unittest.skipUnless(readExcel.get_isRun_text("inventory_adjust_003"),"-跳过不执行")
    def test_inventory_adjust003(self):
        """调整库存后生成库存调整记录校验"""

        # 获取测试i数据
        data = self.readExcel.get_dict_data("inventory_adjust_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入库存记录页面
        self.inventory_adjust.enter_inventory_adjust_log_page()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(data,self.inventory_adjust.get_first_log_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Inventory_Adjust)

    unittest.TextTestRunner().run(suits)