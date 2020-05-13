# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/4/8 14:15

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.groupSearchPage import GroupSearchPage
from public.page.editGroupPage import EditGroupPage
import unittest

class Transfer_Group_Manager(unittest.TestCase):

    """ 【圈主转移功能校验】 """

    # 实例化操作类
    readExcel = Read_Excel("dissolvesGroup")

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.search_group = GroupSearchPage(cls.driver)
        cls.edit_group = EditGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"dissolvesGroup")
        # 登录群主网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入圈子列表页面
        cls.edit_group.enter_my_group_list_page()
        cls.base.sleep(2)

    @unittest.skipUnless(readExcel.get_isRun_text("dissolves_group_001"),"-跳过不执行该用例")
    def test_transfer_group_manager_001(self):
        """退出圈子-成员成功退出圈子校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("dissolves_group_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击编辑
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        self.base.sleep(1)
        # 点击解散
        self.edit_group.click_break_up_group()
        # 断言
        self.base.sleep(1)
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Transfer_Group_Manager)

    unittest.TextTestRunner().run(suits)
