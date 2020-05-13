# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/16 10:37

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.groupSearchPage import GroupSearchPage
from public.page.visitMemberPage import VisitMemberPage
import unittest

class Visit_Send_Member(unittest.TestCase):

    """ 【圈子邀请派单成员功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("visitSendMember")

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.group_search = GroupSearchPage(cls.driver)
        cls.visit_member = VisitMemberPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"visitSendMember")
        # 登录网点
        cls.login.login_main("T西安超级售后有限公司")
        # 进入我的圈子列表页
        cls.group_search.enter_my_group_list_page()

    def setUp(self):
        self.base.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("visit_send_member_001"),"-跳过不执行该用例")
    def test_visit_member001(self):
        """邀请派单搜索-搜索功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_send_member_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击邀请派单
        self.visit_member.click_visit_send_member(data["圈子名称"])
        # 输入成员名称
        self.visit_member.input_member_search(data["客户名称"])
        # 点击搜索
        self.visit_member.click_search_member_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.visit_member.get_search_member_info())

    @unittest.skipUnless(readExcel.get_isRun_text("visit_send_member_002"),"-跳过不执行该用例")
    def test_visit_member002(self):
        """邀请派单成员-邀请成员为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_send_member_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击邀请派单
        self.visit_member.click_visit_send_member(data["圈子名称"])
        # 点击立即邀请
        self.visit_member.click_prompt_visit_btn()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("visit_send_member_003"),"-跳过不执行该用例")
    def test_visit_member003(self):
        """邀请派单成员-月派单量为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_send_member_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击邀请派单
        self.visit_member.click_visit_send_member(data["圈子名称"])
        # 选择派单成员
        self.visit_member.select_visit_member(data["邀请名称"])
        # 点击立即邀请
        self.visit_member.click_prompt_visit_btn()
        # 点击确认
        self.visit_member.click_confirm_visit_btn()
        # 断言
        self.assert_mode.assert_equal(data, self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("visit_send_member_004"),"-跳过不执行该用例")
    def test_visit_member004(self):
        """邀请派单成员-邀请派单成员成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_send_member_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击邀请派单
        self.visit_member.click_visit_send_member(data["圈子名称"])
        # 选择派单成员
        self.visit_member.select_visit_member(data["邀请名称"])
        # 点击立即邀请
        self.visit_member.click_prompt_visit_btn()
        # 输入月派单量
        self.visit_member.input_send_count_of_month(data["月派单量"])
        # 点击确认
        self.visit_member.click_confirm_visit_btn()
        self.base.sleep(2)
        # 刷新页面
        self.base.refresh_page()
        # 获取详情页中派单方列表
        senderMemberList = self.visit_member.get_send_member_list_names(data["圈子名称"])
        # 断言
        self.assert_mode.assert_in(data,senderMemberList)


    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Visit_Send_Member)

    unittest.TextTestRunner().run(suit)