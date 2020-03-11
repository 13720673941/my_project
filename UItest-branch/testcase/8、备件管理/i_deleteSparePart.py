# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/5 11:20

from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common import myDecorator
from public.common.operateExcel import *
from public.page.loginPage import LoginPage
from public.page.spartPartListPage import SparePartListPage
from public.page.inventoryAdjustPage import InventoryAdjust
import unittest,ddt

@ddt.ddt
class Del_Spare_Part(unittest.TestCase):

    """ 【删除备件功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("delSparePart")
    # 用例集合
    caseList = [
        "del_sparePart_001","del_sparePart_002"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.del_sparePart = SparePartListPage(cls.driver)
        cls.adjust_inventory = InventoryAdjust(cls.driver)
        cls.assert_page = Assert(cls.driver,"delSparePart")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.del_sparePart.enter_company_inventory_page()
        """
            ----- 前置条件调整备件库存为0 -----
        """
        cls.del_sparePart.input_search_sparePart_name("自动化测试备件")
        cls.del_sparePart.click_search_button()
        cls.base_page.sleep(1)
        # 调整库存
        cls.adjust_inventory.click_inventory_adjust()
        cls.base_page.sleep(1)
        cls.adjust_inventory.input_after_adjust_inventory("0")
        cls.adjust_inventory.input_adjust_reason("000")
        cls.base_page.sleep(1)
        cls.adjust_inventory.click_confirm_adjust()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_del_sparePart001(self,ddt_data):
        """删除备件功能测试用例"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data)
        # 刷新页面
        self.base_page.refresh_page()
        # 选择第一个备件
        self.del_sparePart.select_first_sparePart(ddt_data["备件名称"])
        # 点击删除按钮
        self.del_sparePart.click_del_sparePart_btn()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Del_Spare_Part)

    unittest.TextTestRunner().run(suits)