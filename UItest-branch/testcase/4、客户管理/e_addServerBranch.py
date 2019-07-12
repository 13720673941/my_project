# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:26

from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.serverBranchPage import ServerBranchPage
import unittest,ddt
"""
添加服务商测试用例脚本：
1、输入客户手机号自动带出服务商名称校验 2、客户主账号为空校验 3、客户备注为空校验 4、客户手机号左边界值校验 
5、客户手机号右边界值校验 6、客户手机号特殊字符格式校验 7、合作工单类型空校验 8、不能重复邀请校验 9、成功邀请服务商校验
"""
# 获取测试数据
server_branch_data = get_test_data()["AddServerPage"]
add_branch_data = server_branch_data["add_branch_fnc"]

@ddt.ddt
class Add_Server_Branch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.server_branch = ServerBranchPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        # 开始脚本
        mytest.start_test()
        # 获取网点登录账号密码
        cls.username = read_config_data("蓝魔科技","username")
        cls.password = read_config_data("蓝魔科技","password")
        # 登录网点
        cls.login.login_main(cls.username,cls.password)
        # 进入客户列表页面
        cls.server_branch.enter_customer_list_page()
        cls.base_page.sleep(1)

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 点击添加服务商按钮
        self.server_branch.click_add_server_branch()
        # 时间加载
        self.base_page.sleep(1)

    def test_add_serverBranch001(self):
        """输入客户手机号自动带出服务商名称校验"""

        # 获取测试数据
        data = server_branch_data["auto_name_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 输入客户手机号
        self.server_branch.input_customer_phone_num(phone_num=data["PhoneNum"])
        self.base_page.sleep(1)
        # 获取自动带出的客户名字
        branch_name = self.server_branch.get_customer_auto_name()
        # 断言
        self.assert_mode.assert_equal(data["expect"],branch_name)

    @ddt.data(*add_branch_data)
    def test_add_serverBranch002(self,add_branch_data):
        """添加服务商功能测试用例"""

        # 输出测试用例名称
        self.base_page.print_case_name(add_branch_data["CaseName"])
        # 输入客户手机号
        self.server_branch.input_customer_phone_num(phone_num=add_branch_data["PhoneNum"])
        self.base_page.sleep(1)
        # 清除自动带出的名称
        self.server_branch.clear_customer_name()
        # 输入客户名称备注
        self.server_branch.input_customer_name(customer_name=add_branch_data["BranchName"])
        # 选择合作工单类型
        self.server_branch.select_please_to_someone(is_select=add_branch_data["IsSelect"])
        # 点击确定
        self.server_branch.click_confirm_add_branch()
        # 获取系统提示信息
        system_msg = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(add_branch_data["expect"],system_msg)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Add_Server_Branch("test_add_serverBranch001"))
    suit.addTest(Add_Server_Branch("test_add_serverBranch002"))

    unittest.TextTestRunner().run(suit)

