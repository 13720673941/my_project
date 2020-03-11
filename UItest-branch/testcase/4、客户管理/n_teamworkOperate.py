# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 15:59

from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.teamworkNewsPage import TeamWorkNewsPage
import unittest

class Teamwork_Apply_Operate(unittest.TestCase):
    """ 【拒绝、撤销、二次申请功能】 """

    # 实例化类
    readExcel = Read_Excel("teamworkOperate")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.teamwork_apply = TeamWorkNewsPage(cls.driver)
        cls.assertMode = Assert(cls.driver,"teamworkOperate")

    def public_operate(self,searchWord):
        """搜索网点"""
        self.teamwork_apply.input_customer_name_phone(searchWord)
        self.teamwork_apply.click_search_btn()
        self.base.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("teamwork_operate_001"),"-跳过不执行用例")
    def test_teamwork_operate001(self):
        """拒绝合作申请校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("teamwork_operate_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 登录该网点
        self.login.login_main(data["发出申请网点"])
        # 进入合作申请页面-收到的申请
        self.teamwork_apply.enter_teamwork_news_page()
        # 搜索申请的网点
        self.public_operate(data["收到申请网点"])
        # 拒绝成为该网点服务商的申请
        self.teamwork_apply.click_refuse_btn()
        self.base.sleep(1)
        # 退出登录
        self.login.click_logout_button()
        # 登录该账号
        self.login.login_main(data["收到申请网点"])
        # 进入合作申请页面-收到的申请
        self.teamwork_apply.enter_teamwork_news_page()
        # 切换发出的申请
        self.teamwork_apply.click_table_send_visit()
        # 搜索申请的网点
        self.public_operate(data["发出申请网点"])
        # 断言
        self.assertMode.assert_equal(data,self.teamwork_apply.get_refuse_text())

    @unittest.skipUnless(readExcel.get_isRun_text("teamwork_operate_002"),"-跳过不执行用例")
    def test_teamwork_operate002(self):
        """再次申请合作校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("teamwork_operate_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 切换table
        self.teamwork_apply.click_table_send_visit()
        # 搜索网点
        self.public_operate(data["发出申请网点"])
        # 点击再次邀请,成为服务商
        self.teamwork_apply.click_again_visit_teamwork()
        self.base.sleep(1)
        # 断言
        self.assertMode.assert_equal(data,self.teamwork_apply.get_refuse_text())

    @unittest.skipUnless(readExcel.get_isRun_text("teamwork_operate_003"),"-跳过不执行用例")
    def test_teamwork_operate003(self):
        """取消合作申请校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("teamwork_operate_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 切换table
        self.teamwork_apply.click_table_send_visit()
        # 搜索网点
        self.public_operate(data["发出申请网点"])
        # 点击两条邀请的撤销
        self.teamwork_apply.click_del_teamwork_visit()
        # 刷新页面
        self.base.refresh_page()
        self.public_operate(data["发出申请网点"])
        # 断言
        self.assertMode.assert_el_not_in_page(data,self.teamwork_apply.get_first_row_isDisplayed())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Teamwork_Apply_Operate)

    unittest.TextTestRunner().run(suits)