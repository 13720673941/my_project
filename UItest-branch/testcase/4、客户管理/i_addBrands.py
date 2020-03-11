# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 17:35

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.brandsPage import BrandsPage
import unittest,ddt

@ddt.ddt
class Add_Brands(unittest.TestCase):
    """ 【添加厂商账号功能】 """

    # 实例化类
    readExcel = Read_Excel("addBrands")
    # 获取测试用例id
    case_list = [
        "add_brands_001","add_brands_002","add_brands_003",
        "add_brands_004"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.add_brands = BrandsPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "addBrands")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入客户列表页面
        cls.add_brands.enter_customer_list_page()

    def setUp(self):

        # 初始化刷新页面
        self.base.refresh_page()
        # 切换table
        self.add_brands.click_brands_table_btn()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_add_brands001(self,ddt_data):
        """添加厂商系统账号测试用例"""

        # 打印用例名称
        self.base.print_case_name(ddt_data)
        # 点击添加厂商账号
        self.add_brands.click_add_brands_account()
        # 等待
        self.base.sleep(1)
        # 选择厂商系统
        self.add_brands.select_brands_system(ddt_data["品牌商名称"])
        # 输入登录账号
        self.add_brands.input_login_username(ddt_data["登录账号"])
        # 输入登录密码
        self.add_brands.input_login_password(ddt_data["登录密码"])
        # 确定添加
        self.add_brands.click_confirm_add_brands()
        # 断言
        self.assertMode.assert_equal(ddt_data,self.login.get_system_msg())

    """
    取消了厂商账号的删除功能
    """
    # @unittest.skipUnless(readExcel.get_isRun_text("add_brands_004"),"-跳过不执行该用例")
    # def test_add_brands002(self):
    #     """删除添加的账号测试"""
    #
    #     # 获取测试数据
    #     data = self.readExcel.get_dict_data("add_brands_005")
    #     # 打印用例名称
    #     self.base_page.print_case_name(data)
    #     # 点击删除
    #     self.add_brands.click_delete_brands(data["品牌商名称"])
    #     # 确认删除
    #     self.add_brands.click_confirm_del_brands()
    #     # 断言
    #     self.assertMode.assert_equal(data,self.base_page.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Add_Brands)

    unittest.TextTestRunner().run(suits)