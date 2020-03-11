# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/22 14:48

from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest

class Master_Server_Set(unittest.TestCase):

    """ 【合作师傅服务设置功能】 """

    # 实例化类
    readExcel = Read_Excel("masterServerSet")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"masterServerSet")
        # 登录经销商
        cls.login.login_main("T西安好家帮家政有限公司")

    def enter_master_server_set_page(self,search_word):
        """师傅列表页面搜索师傅点击设置"""

        # 搜索师傅名字 -固定设置的师傅
        self.master_page.input_keyword_for_search(search_word)
        # 点击搜索
        self.master_page.click_search_btn()
        self.base.sleep(1)
        """
        页面改动不需要拖动操作按钮放到上层页面了
        """
        # # 页面宫动到按钮位置
        # self.master_page.roll_right_to_operate_btn()
        # 点击服务设置按钮
        self.master_page.click_server_set_btn()
        self.base.sleep(1)

    def search_master(self,search_word):
        """师傅列表搜索师傅"""

        self.base.refresh_page()
        self.master_page.input_keyword_for_search(search_word)
        self.master_page.click_search_btn()
        self.base.sleep(1)

    def setUp(self):
        # 进入师傅列表页面
        self.master_page.enter_master_list_page()
        # 刷新页面
        self.base.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("server_set_001"),"-跳过不执行")
    def test_server_set001(self):
        """师傅备注设置校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 输入客户备注信息
        self.master_page.input_master_remark(data["师傅备注"])
        # 保存服务设置
        self.master_page.click_set_server_save()
        self.base.sleep(1)
        #搜索师傅
        self.search_master(data["师傅名称"])
        # 获取第一行的数据
        first_master_info = self.master_page.get_first_master_info()
        # 断言
        self.assert_mode.assert_in(data,first_master_info)

    @unittest.skipUnless(readExcel.get_isRun_text("server_set_002"),"-跳过不执行")
    def test_server_set002(self):
        """师傅服务类型为空校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 清空服务类型配置
        self.master_page.clear_server_type()
        # 点击保存
        self.master_page.click_set_server_save()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("server_set_002"),"-跳过不执行")
    def test_server_set003(self):
        """师傅服务品类为空校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 清空服务类型配置
        self.master_page.clear_kinds_type()
        # 点击保存
        self.master_page.click_set_server_save()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    """
    师傅服务区域改为可以为空：为空就是没有限制区域
    """
    @unittest.skipUnless(readExcel.get_isRun_text("server_set_004"),"-跳过不执行")
    def test_server_set004(self):
        """师傅服务区域为空校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 清空服务区域配置
        self.master_page.clear_master_server_place()
        # 点击保存
        self.master_page.click_set_server_save()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("server_set_005"),"-跳过不执行")
    def test_server_set005(self):
        """师傅位置为空校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_005")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 清空服务类型配置
        self.master_page.clear_master_location()
        # 点击保存
        self.master_page.click_set_server_save()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("server_set_006"),"-跳过不执行")
    def test_server_set006(self):
        """师傅服务设置成功校验"""

        #获取测试数据
        data = self.readExcel.get_dict_data("server_set_006")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入师傅服务设置页面
        self.enter_master_server_set_page(data["师傅名称"])
        # 清空服务类型配置
        self.master_page.clear_server_type()
        # 清空服务品类
        self.master_page.clear_kinds_type()
        # 清空服务区域
        self.master_page.clear_master_server_place()
        # 设置服务类型
        self.master_page.select_server_type(data["服务类型"])
        # 设置品类
        self.master_page.select_kinds_type(data["品类"])
        # 设置服务区域
        self.master_page.select_server_province(data["服务区域"])
        # 点击保存
        self.master_page.click_set_server_save()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Master_Server_Set)

    unittest.TextTestRunner(verbosity=2).run(suits)

