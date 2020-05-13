# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:32

from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.masterReturnPage import MasterReturnPage
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.spartPartListPage import SparePartListPage
from public.page.masterReceivePage import MasterReceivePage
from public.common.operateExcel import *
import unittest

class Master_Return(unittest.TestCase):

    """ 【师傅返还备件校验】 """

    # 实例化操作类
    readExcel = Read_Excel("masterReturnSP")

    @classmethod
    def setUpClass(cls):
        # 设置浏览去驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_return = MasterReturnPage(cls.driver)
        cls.company_inventory = SparePartListPage(cls.driver)
        cls.adjust_inventory = InventoryAdjust(cls.driver)
        cls.receive_sparePart = MasterReceivePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"masterReturnSP")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.company_inventory.enter_company_inventory_page()

    def search_spare_part(self,sparePartName):

        # 搜索备件
        self.company_inventory.input_search_sparePart_name(sparePartName)
        # 点击搜索
        self.company_inventory.click_search_button()
        self.base_page.sleep(1)

    def setUp(self):

        # 刷新页面
        self.base_page.refresh_page()
        # 点击师傅返还按钮
        self.master_return.click_master_return_button()
        self.base_page.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_001"),"-跳过不执行该用例")
    def test_master_return001(self):
        """返还备件师傅名称不能为空校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 点击保存按钮
        self.master_return.click_save_button()
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_002"),"-跳过不执行该用例")
    def test_master_return002(self):
        """返还备件名称不能为空校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 点击保存按钮
        self.master_return.click_save_button()
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_004"),"-跳过不执行该用例")
    def test_master_return003(self):
        """按备件条码模糊匹配备件校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_return_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 输入备件条码
        self.master_return.input_spare_part_number(data["备件条码"])
        self.base_page.sleep(1)
        # 获取模糊匹配的备件条码名称
        all_sp_number = self.master_return.get_search_sp_number()
        # 断言
        self.assert_page.assert_equal(data,all_sp_number)

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_005"),"-跳过不执行该用例")
    def test_master_return004(self):
        """按备件名称模糊匹配备件校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_return_005")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 输入备件名称
        self.master_return.input_spare_part_name(data["备件名称"])
        self.base_page.sleep(1)
        # 获取模糊匹配的备件条码名称
        all_sp_number = self.master_return.get_search_sp_name()
        # 断言
        self.assert_page.assert_in(data,all_sp_number)

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_003"),"-跳过不执行该用例")
    def test_master_return005(self):
        """返还备件数量不能为空校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_number(data["备件条码"])
        self.base_page.sleep(1)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        # 点击保存按钮
        self.master_return.click_save_button()
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_006"),"-跳过不执行该用例")
    def test_master_return006(self):
        """返还的备件不能大于师傅库存备件校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_006")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_number(data["备件条码"])
        self.base_page.sleep(2)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        self.base_page.sleep(1)
        # 输入返还数量
        self.master_return.input_sp_return_count(data["返还数量"])
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_not_equal(data,self.master_return.get_input_return_count())

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_007"),"-跳过不执行该用例")
    def test_master_return007(self):
        """成功返还备件网点库存增加校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_007")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        self.base_page.refresh_page()
        # 搜索备件
        self.search_spare_part(data["备件名称"])
        # 获取备件库存数量
        before_count = self.adjust_inventory.get_all_inventory_count()
        self.base_page.refresh_page()
        # 进入师傅库存页面
        self.receive_sparePart.enter_master_inventory_page()
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(data["师傅名称"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(data["备件名称"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(2)
        # 获取师傅库存数量
        global master_before_receive
        # 未搜索到就是 0
        master_before_receive = self.receive_sparePart.get_master_inventory_count()
        # 进入公司库存页面
        self.company_inventory.enter_company_inventory_page()
        # 点击师傅返还
        self.master_return.click_master_return_button()
        self.base_page.sleep(3)
        # 选择返还师傅名称
        self.master_return.select_return_master_name(data["师傅名称"])
        # 输入搜索备件名称
        self.master_return.input_spare_part_number(data["备件条码"])
        self.base_page.sleep(1)
        # 点击模糊匹配的备件
        self.master_return.click_spare_part_name()
        # 输入返还数量
        self.master_return.input_sp_return_count(data["返还数量"])
        # 点击保存
        self.master_return.click_save_button()
        self.base_page.sleep(1)
        # 搜索备件
        self.search_spare_part(data["备件名称"])
        # 获取备件库存数量
        after_count = self.adjust_inventory.get_all_inventory_count()
        # 断言,网点库存增加校验
        self.assert_page.assert_equal(data,str(after_count-before_count))

    @unittest.skipUnless(readExcel.get_isRun_text("master_return_008"),"-跳过不执行该用例")
    def test_master_return008(self):
        """成功返还备件师傅库存减少校验"""

        # 获取测试数据data
        data = self.readExcel.get_dict_data("master_return_008")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入师傅库存页面
        self.receive_sparePart.enter_master_inventory_page()
        self.base_page.refresh_page()
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(data["师傅名称"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(data["备件名称"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(2)
        # 获取成功反件后的师傅库存
        master_after_receive = self.receive_sparePart.get_master_inventory_count()
        # 断言
        self.assert_page.assert_equal(data,str(master_before_receive - master_after_receive))

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Return)

    unittest.TextTestRunner().run(suits)
