#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 16:36

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.dealerPage import DealerPage
import unittest,ddt

class Dealer_Set(unittest.TestCase):

    """ 【经销商服务设置功能】 """

    # 实例化类
    readExcel = Read_Excel("dealerSet")
    # 获取测试经销商的名称
    dealerName = rwConfig.read_config_data("T西安好家帮家政有限公司","manage_branch")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.manage_branch = DealerPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "dealerSet")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入邀请经销商页面
        cls.manage_branch.enter_dealer_page()

    def setUp(self):
        self.base.refresh_page()
        # 搜索经销商
        self.manage_branch.input_search_message(self.dealerName)
        self.manage_branch.click_search()
        # 点击设置服务
        self.base.sleep(4)
        self.manage_branch.click_set_server()

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_set_001"),"-跳过不执行该用例")
    def test_dealer_set001(self):
        """设置经销商的备注校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dealer_set_001")
        # 打印测试名称
        self.base.print_case_name(data)
        # 清除输入框
        self.manage_branch.clear_branch_remark()
        # 输入备注
        self.manage_branch.input_branch_remark(data["备注名称"])
        # 点击确定
        self.manage_branch.click_server_set_confirm()
        self.base.sleep(1)
        # 输出第一行的所有数据字段
        first_branch_info = self.manage_branch.get_first_branch_info()
        # 断言
        self.assertMode.assert_in(data,first_branch_info)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_set_002"),"-跳过不执行该用例")
    def test_dealer_set002(self):
        """经销商服务设置合作类型不能编辑"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dealer_set_002")
        # 打印测试名称
        self.base.print_case_name(data)
        # 获取合作类型选择属性
        teamwork_attribute = self.manage_branch.get_teamwork_type_attribute()
        # 断言
        self.assertMode.assert_equal(data,teamwork_attribute)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_set_003"),"-跳过不执行该用例")
    def test_dealer_set003(self):
        """经销商服务设置服务类型不能编辑"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dealer_set_003")
        # 打印测试名称
        self.base.print_case_name(data)
        # 获取合作类型选择属性
        server_type_attribute = self.manage_branch.get_server_type_attribute()
        # 断言
        self.assertMode.assert_equal(data,server_type_attribute)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_set_004"),"-跳过不执行该用例")
    def test_dealer_set004(self):
        """经销商服务设置服务品牌不能编辑"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dealer_set_004")
        # 打印测试名称
        self.base.print_case_name(data)
        # 获取合作类型选择属性
        server_brands_attribute = self.manage_branch.get_brands_type_attribute()
        # 断言
        self.assertMode.assert_equal(data,server_brands_attribute)

    @unittest.skipUnless(readExcel.get_isRun_text("dealer_set_005"),"-跳过不执行该用例")
    def test_dealer_set005(self):
        """经销商服务设置服务品类不能编辑"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dealer_set_005")
        # 打印测试名称
        self.base.print_case_name(data)
        # 获取合作类型选择属性
        server_kinds_attribute = self.manage_branch.get_kinds_type_attribute()
        # 断言
        self.assertMode.assert_equal(data,server_kinds_attribute)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Dealer_Set)

    unittest.TextTestRunner().run(suit)