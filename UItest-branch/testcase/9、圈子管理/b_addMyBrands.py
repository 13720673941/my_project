# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/11 14:25

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createGroupPage import CreateGroupPage
import unittest,ddt

@ddt.ddt
class Add_My_Brands(unittest.TestCase):

    """ 【创建圈子页面添加品牌功能】 """

    # 实例化操作类
    readExcel = Read_Excel("addMyBrands")

    @classmethod
    def setUpClass(cls):
        # 实例化页面类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_group = CreateGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"addMyBrands")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入我的圈子列表页面
        cls.create_group.enter_my_group_list_page()

    @unittest.skipUnless(readExcel.get_isRun_text("add_my_brands_001"),"跳过不执行该用例")
    def test_add_my_brands001(self):
        """添加品牌-品牌名称不能为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("add_my_brands_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 清除页面数据
        self.base.refresh_page()
        # 点击创建圈子按钮
        self.create_group.click_create_group_btn()
        # 点击添加品牌
        self.create_group.click_add_brands_btn()
        # 输入品牌名称
        self.create_group.input_new_brands_name(data["品牌名称"])
        # 点击确定
        self.create_group.click_confirm_add_button()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("add_my_brands_002"),"跳过不执行该用例")
    def test_add_my_brands002(self):
        """添加品牌-成功添加品牌校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("add_my_brands_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 清除页面数据
        self.base.refresh_page()
        # 点击创建圈子按钮
        self.create_group.click_create_group_btn()
        # 点击添加品牌
        self.create_group.click_add_brands_btn()
        # 输入品牌名称
        self.create_group.input_new_brands_name(data["品牌名称"])
        # 点击确定
        self.create_group.click_confirm_add_button()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.create_group.get_all_service_brands())

    @unittest.skipUnless(readExcel.get_isRun_text("add_my_brands_003"),"跳过不执行该用例")
    def test_add_my_brands003(self):
        """添加品牌-品牌名称不能为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("add_my_brands_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击添加品牌
        self.create_group.click_add_brands_btn()
        # 输入品牌名称
        self.create_group.input_new_brands_name(data["品牌名称"])
        # 点击确定
        self.create_group.click_confirm_add_button()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Add_My_Brands)

    unittest.TextTestRunner().run(suits)

