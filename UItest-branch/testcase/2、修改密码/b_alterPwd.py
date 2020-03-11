#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/18 11:07

from public.common import rwConfig
from public.common.operateExcel import *
from public.common import myDecorator
from public.common import getNewPwd
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.alterPwdPage import AlterPwdPage
import unittest,ddt

@ddt.ddt
class Alter_Password(unittest.TestCase):

    """" 【修改密码功能测试用例脚本】 """

    # 需要加入ddt的测试用例编号列表
    case_id_1 = [
        "alter_pwd_004","alter_pwd_005","alter_pwd_006",
        "alter_pwd_007","alter_pwd_008","alter_pwd_009"
    ]
    case_id_2 = [
        "alter_pwd_010","alter_pwd_011"
    ]
    # 获取ddt数据
    read_operate = Read_Excel("alterPwd")
    ddt_data_1 = read_operate.get_ddt_data(case_id_1)
    ddt_data_2 = read_operate.get_ddt_data(case_id_2)

    @classmethod
    def setUpClass(cls):
        # 实例化断言类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.alter_pwd = AlterPwdPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"alterPwd")
        # 获取新旧密码
        cls.old_pwd,cls.new_pwd = getNewPwd.get_new_pwd()
        # 赋值
        cls.ddt_data_1[-1]["原密码"] = cls.old_pwd
        cls.ddt_data_1[-1]["新密码"] = cls.new_pwd
        cls.ddt_data_1[-1]["确认密码"] = cls.new_pwd
        # 调用登录主程序登录
        cls.login.login_main("T西安好家帮家政有限公司")

    def setUp(self):
        self.base.refresh_page()

    @unittest.skipUnless(read_operate.get_isRun_text("alter_pwd_001"),"-跳过不执行该用例")
    def test_alterPwd001(self):
        """登陆密码为空校验"""

        # 获取测试数据
        data = self.read_operate.get_dict_data("alter_pwd_001")
        self.base.print_case_name(data)
        # 进入修改密码页面
        self.alter_pwd.enter_alterPwd_page()
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入新密码
        self.alter_pwd.input_new_pwd(data["新密码"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(data["确认密码"])
        self.base.sleep(1)
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(data,self.alter_pwd.get_old_pwd_msg)

    @unittest.skipUnless(read_operate.get_isRun_text("alter_pwd_002"),"-跳过不执行该用例")
    def test_alterPwd002(self):
        """新密码为空校验"""

        # 获取测试数据
        data = self.read_operate.get_dict_data("alter_pwd_002")
        self.base.print_case_name(data)
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入登陆密码
        self.alter_pwd.input_old_pwd(data["原密码"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(data["确认密码"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(data,self.alter_pwd.get_new_pwd_msg)

    @unittest.skipUnless(read_operate.get_isRun_text("alter_pwd_003"),"-跳过不执行该用例")
    def test_alterPwd003(self):
        """确认密码为空校验"""

        # 获取测试数据
        data = self.read_operate.get_dict_data("alter_pwd_003")
        self.base.print_case_name(data)
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入登陆密码
        self.alter_pwd.input_old_pwd(data["原密码"])
        # 输入新密码
        self.alter_pwd.input_new_pwd(data["新密码"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(data,self.alter_pwd.get_confirm_pwd_msg)

    @ddt.data(*ddt_data_1)
    @myDecorator.skipped_case
    def test_alterPwd004(self,ddt_data_1):
        """修改密码逻辑/密码格式校验"""

        # 打印用例名称
        self.base.print_case_name(ddt_data_1)
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入旧密码
        self.alter_pwd.input_old_pwd(ddt_data_1["原密码"])
        # 输入新密码
        self.alter_pwd.input_new_pwd(ddt_data_1["新密码"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(ddt_data_1["确认密码"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        self.base.sleep(2)
        # 获取系统提示
        msg = self.login.get_system_msg()
        # 写入新改的密码
        if msg == '修改成功':
            rwConfig.write_config_data("T西安好家帮家政有限公司","password",self.new_pwd)
        # 断言
        self.assert_mode.assert_equal(ddt_data_1,msg)

    @ddt.data(*ddt_data_2)
    @myDecorator.skipped_case
    def test_alterPwd005(self,ddt_data_2):
        """修改密码后登录逻辑校验"""

        # 获取测试用例名称
        self.base.print_case_name(ddt_data_2)
        self.ddt_data_2[0]["密码"] = self.old_pwd
        self.ddt_data_2[1]["密码"] = self.new_pwd
        # 刷新页面
        self.base.refresh_page()
        # 调用登录
        self.login.enter_login_page()
        self.login.input_username(username=ddt_data_2["用户名"])
        self.login.input_password(password=ddt_data_2["密码"])
        self.login.click_login_button()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddt_data_2,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':


    suit = unittest.TestLoader().loadTestsFromTestCase(Alter_Password)

    unittest.TextTestRunner().run(suit)
