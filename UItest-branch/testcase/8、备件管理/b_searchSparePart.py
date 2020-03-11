# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/3 20:31

from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common.operateExcel import *
from public.page.loginPage import LoginPage
from public.page.spartPartListPage import SparePartListPage
import unittest,ddt

@ddt.ddt
class Search_SparePart(unittest.TestCase):

    """ 【备件库存列表搜索功能】 """

    # 实例化操作类
    readExcel = Read_Excel("searchSparePart")
    # 测试用例编号集合
    caseList = [
        "search_sparePart_001","search_sparePart_002",
        "search_sparePart_003","search_sparePart_004",
        "search_sparePart_005"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):

        # 设置浏览去驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"searchSparePart")
        cls.login = LoginPage(cls.driver)
        cls.search_sparePart = SparePartListPage(cls.driver)
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.search_sparePart.enter_company_inventory_page()

    @ddt.data(*ddt_data)
    def test_search_sparePart001(self,ddt_data):
        """备件搜索筛选功能校验"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data)
        # 刷新页面
        self.base_page.refresh_page()
        # 输入备件条码
        self.search_sparePart.input_search_sparePart_number(ddt_data["备件条码"])
        # 输入备件名称
        self.search_sparePart.input_search_sparePart_name(ddt_data["备件名称"])
        # 输人备件品牌
        self.search_sparePart.input_search_sparePart_brand(ddt_data["备件品牌"])
        # 选择备件类型
        self.search_sparePart.select_search_sparePart_type(ddt_data["备件类型"])
        # 选择适用品类
        self.search_sparePart.select_search_use_for_kind(ddt_data["适用品类"])
        # 点击搜索按钮
        self.search_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(ddt_data,self.search_sparePart.get_first_row_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Search_SparePart)

    unittest.TextTestRunner().run(suits)