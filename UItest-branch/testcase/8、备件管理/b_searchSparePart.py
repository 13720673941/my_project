# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/3 20:31

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common import rwconfig
from public.page.loginPage import LoginPage
from public.page.companyInventoryPage import CompanyInventoryPage
import unittest,ddt
"""
公司库存备件搜索功能校验：
1、按备件条码搜索备件校验 2、按备件名称搜索备件校验 3、按备件品牌搜索备件校验 
4、按备件类型搜索备件校验 5、按备件适用品类搜索备件校验
"""
# 获取测试数据信息
ddt_data = get_test_data()["CompanyInventoryPage"]["search_sparePart_fnc"]

@ddt.ddt
class Search_SparePart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览去驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.search_sparePart = CompanyInventoryPage(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("蓝魔科技", "username")
        password = rwconfig.read_config_data("蓝魔科技", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.search_sparePart.enter_company_inventory_page()

    @ddt.data(*ddt_data)
    def test_search_sparePart001(self,ddt_data):
        """备件搜索筛选功能校验"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 输入备件条码
        self.search_sparePart.input_search_sparePart_number(sparePart_number=ddt_data["SP_Num"])
        # 输入备件名称
        self.search_sparePart.input_search_sparePart_name(sparePart_name=ddt_data["SP_Name"])
        # 输人备件品牌
        self.search_sparePart.input_search_sparePart_brand(sparePart_brand=ddt_data["SP_Brand"])
        # 选择备件类型
        self.search_sparePart.select_search_sparePart_type(sparePart_type=ddt_data["SP_Type"])
        # 选择适用品类
        self.search_sparePart.select_search_use_for_kind(use_kind=ddt_data["SP_Kind"])
        # 点击搜索按钮
        self.search_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 获取第一行备件全部信息
        first_row_info = self.search_sparePart.get_first_row_info()
        # 断言
        self.assert_page.assert_in(ddt_data["expect"],first_row_info)


    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Search_SparePart)

    unittest.TextTestRunner().run(suits)