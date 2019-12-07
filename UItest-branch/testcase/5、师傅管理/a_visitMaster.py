# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:56

from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.rwconfig import read_config_data
from public.common import mytest
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest,ddt
"""
师傅列表页添加师傅测试用例：
1、自动带出师傅名称校验 2、未注册的师傅邀请提示发送短信校验 3、师傅手机号为空校验 4、师傅姓名为空校验
5、师傅手机号左边界值校验 6、师傅手机号格式校验 7、成功邀请师傅校验校验 8、重复邀请师傅校验校验
"""
# 获取测试数据
test_data = get_test_data()["MasterListPage"]["visit_master_fnc"]
ddt_data = test_data["TestCase005"]

@ddt.ddt
class Visit_Master(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 师傅执行测试用例
        mytest.start_test()
        # 获取网点账号信息
        username = read_config_data("西安好家帮家政有限公司","username")
        password = read_config_data("西安好家帮家政有限公司","password")
        # 登录网点
        cls.login.login_main(username,password)
        # 进入师傅列表页面
        cls.master_page.enter_master_list_page()

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()
        # 点击添加师傅
        self.master_page.click_add_master_btn()

    def test_visit_master001(self):
        """自动带出师傅名称校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入师傅手机号
        self.master_page.input_master_phone_num(phe_num=data["MasterPhone"])
        # 点击师傅名称输入框
        self.master_page.click_master_name_input()
        self.base_page.sleep(1)
        # 获取带出的师傅名字
        master_name = self.master_page.get_master_name_input_value()
        # 断言
        self.assert_mode.assert_equal(data["expect"],master_name)

    def test_visit_master002(self):
        """未注册的师傅邀请提示发送短信校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入师傅手机号
        self.master_page.input_master_phone_num(phe_num=data["MasterPhone"])
        # 点击师傅名称输入框
        self.master_page.click_master_name_input()
        self.base_page.sleep(1)
        # 获取未注册师傅提示字段
        send_message_text = self.master_page.get_msg_of_master_no_reg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],send_message_text)

    def test_visit_master003(self):
        """师傅手机号为空校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入师傅名字
        self.master_page.input_master_name(master_name=data["MasterName"])
        # 点击确定
        self.master_page.click_confirm_add_master()
        # 获取师傅手机号输入框的属性
        phe_input_att = self.master_page.get_master_phe_input_att()
        # 断言
        self.assert_mode.assert_in(data["expect"],phe_input_att)

    def test_visit_master004(self):
        """师傅名字为空校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入师傅手机号
        self.master_page.input_master_phone_num(phe_num=data["MasterPhone"])
        # 点击确定
        self.master_page.click_confirm_add_master()
        # 获取师傅手机号输入框的属性
        name_input_att = self.master_page.get_master_name_input_att()
        # 断言
        self.assert_mode.assert_in(data["expect"],name_input_att)

    @ddt.data(*ddt_data)
    def test_visit_master005(self,ddt_data):
        """添加师傅逻辑校验"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data["CaseName"])
        # 输入师傅手机号
        self.master_page.input_master_phone_num(phe_num=ddt_data["MasterPhone"])
        # 输入师傅名称
        self.master_page.click_master_name_input()
        self.base_page.sleep(1)
        self.master_page.input_master_name(master_name=ddt_data["MasterName"])
        # 点击确定添加
        self.master_page.click_confirm_add_master()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(ddt_data["expect"],system_message)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Visit_Master)
    unittest.TextTestRunner().run(suits)