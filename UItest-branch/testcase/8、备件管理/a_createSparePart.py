# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/3 15:26

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
创建备件功能校验：
1、备件名称为空校验 2、备件类型为空校验 3、计量单位为空校验 4、备件条码为空校验 5、备件品牌为空校验
6、备件来源为空校验 7、备件型号为空校验 8、适用品类为空校验 9、备件图片为空校验 10、入库价格为空校验
11、零售价格为空校验 12、成功添加备件功能校验 13、修改备件功能校验
"""
# 获取测试数据
ddt_data = get_test_data()["CompanyInventoryPage"]["add_sparePart_fnc"]
data = get_test_data()["CompanyInventoryPage"]

@ddt.ddt
class Create_Spare_Part(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_sparePart = CompanyInventoryPage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("西安好家帮家政有限公司","username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入公司库存页面
        cls.create_sparePart.enter_company_inventory_page()

    def setUp(self):

        # 刷新页面
        self.base_page.refresh_page()

    @ddt.data(*ddt_data)
    def test_create_sparePart001(self,ddt_data):
        """创建备件功能"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 点击新增备件按钮
        self.create_sparePart.click_add_new_sparePart()
        # 等待加载
        self.base_page.sleep(1)
        # 输入备件名称
        self.create_sparePart.input_add_sparePart_name(sparePart_name=ddt_data["SP_Name"])
        # 选择备件类型
        self.create_sparePart.select_add_sparePart_type(sparePart_type=ddt_data["SP_Type"])
        # 选择计量单位
        self.create_sparePart.select_measuring_unit(measuring_unit=ddt_data["Measure_Unit"])
        # 输入备件条码
        self.create_sparePart.input_add_sparePart_number(sparePart_number=ddt_data["SP_Num"])
        # 输入备件品牌
        self.create_sparePart.input_add_sparePart_brand(sparePart_brand=ddt_data["SP_Brand"])
        # 选择备件来源
        self.create_sparePart.select_sparePart_from(sparePart_from=ddt_data["SP_From"])
        # 输人备件型号
        self.create_sparePart.input_sparePart_type_number(type_number=ddt_data["SP_xh"])
        # 选择适用品类
        self.create_sparePart.select_use_kind(is_select=ddt_data["SP_Kind"])
        # 上传备件图片
        self.create_sparePart.operate_up_loading_picture(loading_up=ddt_data["LoadUp"])
        # 输入入库价格
        self.create_sparePart.input_into_inventory_price(into_store_price=ddt_data["Price1"])
        # 输入零售价
        self.create_sparePart.input_user_buy_price(use_buy_price=ddt_data["Price2"])
        # 点击保存按钮
        self.create_sparePart.click_add_save_btn()
        self.base_page.sleep(1)
        # 获取系统提示信息
        system_msg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(ddt_data["expect"],system_msg)

    def test_create_sparePart002(self):
        """编辑备件功能校验"""

        # 获取测试数据信息
        test_data = data["alter_sparePart_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(test_data["CaseName"])
        # 输入搜索备件名称
        self.create_sparePart.input_search_sparePart_name(sparePart_name=test_data["SP_Name1"])
        # 点击搜索备件
        self.create_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 点击第一个备件的修改按钮
        self.create_sparePart.click_alter_button()
        self.base_page.sleep(1)
        # 输入新备件名称
        self.create_sparePart.input_alter_sparePart_name(sparePart_name=test_data["SP_Name2"])
        # 点击保存
        self.create_sparePart.click_alter_save_btn()
        self.base_page.sleep(1)
        # 刷新页面重新搜索
        self.base_page.refresh_page()
        # 输入搜索备件名称
        self.create_sparePart.input_search_sparePart_name(sparePart_name=test_data["SP_Name2"])
        # 点击搜索备件
        self.create_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 获取第一行备件的所有信息
        first_row_info = self.create_sparePart.get_first_row_info()
        # 断言
        self.assert_page.assert_in(test_data["expect"],first_row_info)


    @classmethod
    def tearDownClass(cls):

        cls().assert_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Create_Spare_Part)

    unittest.TextTestRunner().run(suits)