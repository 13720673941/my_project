# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 15:59

from public.common.driver import browser_driver
from public.common.rwconfig import read_config_data
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.teamworkNewsPage import TeamWorkNewsPage
import unittest
"""
申请合作消息操作功能测试用例：
1、拒绝合作申请校验  2、撤销合作申请校验 3、再次邀请合作校验
"""
# 获取测试数据
test_data = get_test_data()["TeamWorkPage"]

class Teamwork_Visit_Operate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.teamwork_visit = TeamWorkNewsPage(cls.driver)
        # 开始执行
        mytest.start_test()

    def public_operate(self,search_word):
        """搜索网点"""
        self.teamwork_visit.input_customer_name_phone(search_word)
        self.teamwork_visit.click_search_btn()
        self.base_page.sleep(1)

    def test_teamwork_visit001(self):
        """拒绝合作申请校验"""

        # 获取测试数据
        data = test_data["refuse_teamwork_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取被邀请的账号信息
        it_username = read_config_data("自动化测试网点04","username")
        it_password = read_config_data("自动化测试网点04","password")
        # 登录该网点
        self.login.login_main(it_username,it_password)
        # 进入合作申请页面-收到的申请
        self.teamwork_visit.enter_teamwork_news_page()
        # 搜索申请的网点
        self.public_operate(search_word=data["keyword"])
        # 拒绝成为该网点服务商的申请
        self.teamwork_visit.click_refuse_btn()
        # 点击确定拒绝
        self.teamwork_visit.click_confirm_refuse()
        self.base_page.sleep(1)
        # 获取拒绝信息字段-他方
        refuse_text = self.teamwork_visit.get_refuse_it_text()
        # 断言
        self.assert_mode.assert_equal(data["expect"], refuse_text)
        # 退出登录
        self.login.click_logout_button()
        # 获取我方登录账号
        my_username = read_config_data("蓝魔科技","username")
        my_password = read_config_data("蓝魔科技","password")
        # 登录该账号
        self.login.login_main(my_username,my_password)
        # 进入合作申请页面-收到的申请
        self.teamwork_visit.enter_teamwork_news_page()
        # 切换发出的申请
        self.teamwork_visit.click_table_send_visit()
        # 搜索申请的网点
        self.public_operate(search_word=data["keyword1"])
        # 获取拒绝信息字段-我方
        refuse_text = self.teamwork_visit.get_refuse_my_text()
        # 断言
        self.assert_mode.assert_equal(data["expect"],refuse_text)

    def test_teamwork_visit002(self):
        """再次申请合作校验"""

        # 获取测试数据
        data = test_data["again_visit_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 切换table
        self.teamwork_visit.click_table_send_visit()
        # 搜索网点
        self.public_operate(search_word=data["keyword"])
        # 点击再次邀请,成为服务商
        self.teamwork_visit.click_again_visit_teamwork()
        # 确认邀请
        self.teamwork_visit.click_confirm_refuse()
        self.base_page.sleep(2)
        # 获取状态字段
        my_visit_status = self.teamwork_visit.get_refuse_my_text()
        # 断言
        self.assert_mode.assert_equal(data["expect"],my_visit_status)

    def test_teamwork_visit003(self):
        """取消合作申请校验"""

        # 获取测试数据
        data = test_data["del_teamwork_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 切换table
        self.teamwork_visit.click_table_send_visit()
        # 搜索网点
        self.public_operate(search_word=data["keyword"])
        # 点击两条邀请的撤销
        self.teamwork_visit.click_del_teamwork_visit()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Teamwork_Visit_Operate)

    unittest.TextTestRunner().run(suits)