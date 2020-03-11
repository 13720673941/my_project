# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:33

from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.spartPartListPage import SparePartListPage
from public.page.newReturnFactoryPage import NewReturnFactoryPage
from public.page.inventoryAdjustPage import InventoryAdjust
import unittest

class New_SP_return(unittest.TestCase):

    """ 【新件返厂功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("returnFactory")

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.company_inventory =  SparePartListPage(cls.driver)
        cls.return_factory = NewReturnFactoryPage(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        cls.assert_mode = Assert(cls.driver,"returnFactory")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.company_inventory.enter_company_inventory_page()

    def search_spare_part(self,sparePart_name):
        """搜索备件"""
        self.company_inventory.input_search_sparePart_name(sparePart_name)
        self.company_inventory.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        self.base_page.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_001"),"-跳过不执行该用例")
    def test_return_factory001(self):
        """新件返厂数量不能为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择备件
        self.company_inventory.select_first_sparePart(data["备件名称"])
        self.base_page.sleep(2)
        # 获取备件库存
        global before_return
        before_return = int(self.inventory_adjust.get_all_inventory_count())
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 点击保存
        self.return_factory.click_save_return()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_002"),"-跳过不执行该用例")
    def test_return_factory002(self):
        """新件返厂备件数量不能大于库存校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择备件
        self.company_inventory.select_first_sparePart(data["备件名称"])
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 输入备件数量
        self.return_factory.input_return_count(data["返厂数量"])
        self.base_page.sleep(1)
        # 断言，输入的100会自动变成备件的最大数量不等于100
        self.assert_mode.assert_not_equal(data,self.return_factory.get_count_number())

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_003"),"-跳过不执行该用例")
    def test_return_factory003(self):
        """新件返厂成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择备件
        self.company_inventory.select_first_sparePart(data["备件名称"])
        # 点击新件返厂
        self.return_factory.click_new_sp_return()
        self.base_page.sleep(1)
        # 输入备件数量
        self.return_factory.input_return_count(data["返厂数量"])
        # 点击保存
        self.return_factory.click_save_return()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_004"),"-跳过不执行该用例")
    def test_return_factory004(self):
        """新件返厂成功公司库存数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索备件
        self.search_spare_part(data["备件名称"])
        # 获取公司库存数量
        self.base_page.sleep(1)
        after_return = int(self.inventory_adjust.get_all_inventory_count())
        # 断言
        self.assert_mode.assert_equal(data,str(before_return-after_return))

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_005"),"-跳过不执行该用例")
    def test_return_factory005(self):
        """新件返厂生成日志记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_005")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入库存调整页面
        self.inventory_adjust.enter_inventory_adjust_log_page()
        self.base_page.sleep(1)
        # 获取第一行库存调整日志记录所有信息
        first_info = self.inventory_adjust.get_first_log_info()
        # 断言
        self.assert_mode.assert_in(data,first_info)

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_006"),"-跳过不执行该用例")
    def test_return_factory006(self):
        """新件返厂生成待返厂校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_006")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 获取第一行备件的所有信息
        first_info = self.return_factory.get_first_row_log_info()
        # 断言备件名称
        self.assert_mode.assert_in(data,first_info)

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_007"),"-跳过不执行该用例")
    def test_return_factory007(self):
        """批量确认返厂校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_007")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 勾选所有备件
        self.return_factory.select_all_return_sp()
        # 点击批量确认
        self.return_factory.click_batch_return_btn()
        # 输入批量返厂备注
        self.return_factory.input_batch_return_remark(data["返厂备注"])
        # 点击保存
        self.return_factory.click_confirm_batch_return()
        self.base_page.sleep(1)
        # 进入已返厂列表页
        self.return_factory.enter_already_return_page()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.return_factory.get_first_row_log_info())

    @unittest.skipUnless(readExcel.get_isRun_text("return_factory_008"),"-跳过不执行该用例")
    def test_return_factory008(self):
        """单个备件确认返厂校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("return_factory_008")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入网点库存页面
        self.company_inventory.enter_company_inventory_page()
        # 再次返厂剩下的5个备件
        self.test_return_factory003()
        # 进入备件返厂管理页面
        self.return_factory.enter_wait_return_page()
        self.return_factory.sleep(1)
        # 点击确认返厂
        self.return_factory.click_confirm_return_btn()
        # 输入批量返厂备注
        self.return_factory.input_batch_return_remark(data["返厂备注"])
        # 点击保存
        self.return_factory.click_confirm_batch_return()
        self.base_page.sleep(1)
        # 进入已返厂列表页
        self.return_factory.enter_already_return_page()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.return_factory.get_first_row_log_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(New_SP_return)

    unittest.TextTestRunner().run(suits)

