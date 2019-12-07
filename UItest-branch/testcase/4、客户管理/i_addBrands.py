# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 17:35

from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.brandsPage import BrandsPage
import unittest,ddt
"""
签约厂商系统页面功能：
1、厂商系统选择为空校验  2、登录账号为空校验  3、登录密码为空校验  4、登录密码错误校验 
5、厂商系统添加成功校验  6、厂商系统重复校验  7、删除厂商系统账号校验
"""
# 获取测试数据
brands_page_data = get_test_data()["AddBrandsPage"]
ddt_data = brands_page_data["add_brands_fnc"]

@ddt.ddt
class Add_Brands(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.brands_page = BrandsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行脚本
        mytest.start_test()
        # 获取网点登录账号密码
        username = read_config_data("西安好家帮家政有限公司","username")
        password = read_config_data("西安好家帮家政有限公司","password")
        cls.login_page.login_main(username,password)
        # 进入客户列表页面
        cls.brands_page.enter_customer_list_page()

    def setUp(self):

        # 初始化刷新页面
        self.base_page.refresh_page()
        # 切换table
        self.brands_page.click_brands_table_btn()

    @ddt.data(*ddt_data)
    def test_add_brands001(self,ddt_data):
        """添加厂商系统账号测试用例"""

        # 打印用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 点击添加厂商账号
        self.brands_page.click_add_brands_account()
        # 等待
        self.base_page.sleep(1)
        # 选择厂商系统
        self.brands_page.select_brands_system(brands_name=ddt_data["BrandsName"])
        # 输入登录账号
        self.brands_page.input_login_username(brands_username=ddt_data["brandsUser"])
        # 输入登录密码
        self.brands_page.input_login_password(brands_password=ddt_data["brandsPwd"])
        # 确定添加
        self.brands_page.click_confirm_add_brands()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(ddt_data["expect"],system_message)

    """
    取消了厂商账号的删除功能
    """
    # def test_add_brands002(self):
    #     """删除添加的账号测试"""
    #
    #     # 获取测试数据
    #     data = brands_page_data["del_brands_fnc"]
    #     # 打印用例名称
    #     self.base_page.print_case_name(data["CaseName"])
    #     # 点击删除
    #     self.brands_page.click_delete_brands(del_brand_name=data["BrandsName"])
    #     # 确认删除
    #     self.brands_page.click_confirm_del_brands()
    #     # 获取系统提示信息
    #     system_message = self.base_page.get_system_msg()
    #     # 断言
    #     self.assert_mode.assert_equal(data["expect"],system_message)

    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestSuite()
    suits.addTest(Add_Brands("test_add_brands001"))
    # suits.addTest(Add_Brands("test_add_brands001"))

    unittest.TextTestRunner().run(suits)