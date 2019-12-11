# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/22 14:48

from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.rwconfig import read_config_data
from public.common import mytest
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest
"""
师傅服务设置功能测试用例：
1、师傅备注设置校验 2、师傅服务类型为空校验 3、师傅服务品类为空校验 4、师傅服务区域为空校验
5、师傅位置为空校验 6、师傅服务设置成功校验
"""
class Master_Server_Set(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 获取测试数据
        cls.test_data = get_test_data()["MasterListPage"]["server_set_fnc"]
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        mytest.start_test()
        # 获取登录的账号密码
        username = read_config_data("西安好家帮家政有限公司","username")
        password = read_config_data("西安好家帮家政有限公司","password")
        # 登录经销商
        cls.login.login_main(username,password)

    def enter_master_server_set_page(self,search_word):
        """师傅列表页面搜索师傅点击设置"""

        # 搜索师傅名字 -固定设置的师傅
        self.master_page.input_keyword_for_search(search_word)
        # 点击搜索
        self.master_page.click_search_btn()
        self.base_page.sleep(1)
        """
        页面改动不需要拖动操作按钮放到上层页面了
        """
        # # 页面宫动到按钮位置
        # self.master_page.roll_right_to_operate_btn()
        # 点击服务设置按钮
        self.master_page.click_server_set_btn()
        self.base_page.sleep(1)

    def search_master(self,search_word):
        """师傅列表搜索师傅"""

        self.base_page.refresh_page()
        self.master_page.input_keyword_for_search(search_word)
        self.master_page.click_search_btn()
        self.base_page.sleep(1)

    def setUp(self):
        # 进入师傅列表页面
        self.master_page.enter_master_list_page()
        # 刷新页面
        self.base_page.refresh_page()

    def test_server_set001(self):
        """师傅备注设置校验"""

        #获取测试数据
        data = self.test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入设置页面
        self.enter_master_server_set_page(search_word=data["MasterAccount"])
        # 输入客户备注信息
        self.master_page.input_master_remark(master_remark=data["Remark"])
        # 保存服务设置
        self.master_page.click_set_server_save()
        self.base_page.sleep(1)
        #搜索师傅
        self.search_master(search_word=data["MasterAccount"])
        # 获取第一行的数据
        first_master_info = self.master_page.get_first_master_info()
        # 断言
        self.assert_mode.assert_in(data["expect"],first_master_info)

    def test_server_set002(self):
        """师傅服务类型为空校验"""

        #获取测试数据
        data = self.test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(search_word=data["MasterAccount"])
        # 清空服务类型配置
        self.master_page.clear_server_type()
        # 点击保存
        self.master_page.click_set_server_save()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set003(self):
        """师傅服务品类为空校验"""

        #获取测试数据
        data = self.test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(search_word=data["MasterAccount"])
        # 清空服务类型配置
        self.master_page.clear_kinds_type()
        # 点击保存
        self.master_page.click_set_server_save()
        self.base_page.sleep(1)
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    """
    师傅服务区域改为可以为空：为空就是没有限制区域
    """
    # def test_server_set004(self):
    #     """师傅服务区域为空校验"""
    #
    #     #获取测试数据
    #     data = self.test_data["TestCase004"]
    #     # 打印测试用例名称
    #     self.base_page.print_case_name(data["CaseName"])
    #     # 进入师傅服务设置页面
    #     self.enter_master_server_set_page(search_word=data["MasterAccount"])
    #     # 清空服务区域配置
    #     self.master_page.clear_master_server_place()
    #     # 点击保存
    #     self.master_page.click_set_server_save()
    #     # 获取系统提示信息
    #     system_message = self.base_page.get_system_msg()
    #     # 断言
    #     self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set005(self):
        """师傅位置为空校验"""

        #获取测试数据
        data = self.test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(search_word=data["MasterAccount"])
        # 清空服务类型配置
        self.master_page.clear_master_location()
        # 点击保存
        self.master_page.click_set_server_save()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set006(self):
        """师傅服务设置成功校验"""

        #获取测试数据
        data = self.test_data["TestCase006"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(search_word=data["MasterAccount"])
        # 清空服务类型配置
        self.master_page.clear_server_type()
        # 清空服务品类
        self.master_page.clear_kinds_type()
        # 清空服务区域
        self.master_page.clear_master_server_place()
        # 设置服务类型
        self.master_page.select_server_type(server_list=data["Server"])
        # 设置品类
        self.master_page.select_kinds_type(kinds_list=data["Kinds"])
        # 设置服务区域
        self.master_page.select_server_province(province_list=data["ServerPlace"])
        # 点击保存
        self.master_page.click_set_server_save()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Server_Set)

    unittest.TextTestRunner(verbosity=2).run(suits)

