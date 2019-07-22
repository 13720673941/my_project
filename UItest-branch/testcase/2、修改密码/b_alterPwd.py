#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/18 11:07

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest,rwconfig
from public.page.loginPage import LoginPage
from public.page.alterPwdPage import AlterPwdPage
import unittest,ddt
"""
网点登陆后修改密码功能：
1、修改密码-原登录密码为空校验 2、修改密码-新登录密码为空校验 3、修改密码-确认新登录密码为空校验 
4、修改密码-新登录密码格式左边界值校验 5、修改密码-新登录密码格式特殊字符校验 6、修改密码-新登录密码格式汉字密码校验
7、修改密码-原登录密码不正确校验 8、修改密码-新密码和重复密码不同校验 9、修改密码-成功修改密码校验
"""
# 获取测试数据
testData = get_test_data()["AlterPwdPage"]["alter_pwd_fnc"]
ddtData = testData["TestCase004"]
ddtData1 = testData["logic_test"]

@ddt.ddt
class Alter_Password(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.alter_pwd = AlterPwdPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 获取网点账号
        cls.username = rwconfig.read_config_data('蓝魔科技','username')
        cls.password = rwconfig.read_config_data('蓝魔科技','password')
        # 获取新密码
        for pwd in get_test_data()["ForgetPwdPage"]["PwdList"]:
            if  pwd != cls.password:
                cls.new_pwd = pwd
        # 新密码写入到修改成功的密码参数中
        ddtData[-1]["NewPwd"] = cls.new_pwd
        ddtData[-1]["ConfirmPwd"] = cls.new_pwd
        # 新旧密码写入到logic_test登录逻辑校验数据中
        ddtData1[0]["password"] = cls.password
        ddtData1[1]["password"] = cls.new_pwd
        # 登陆网点
        cls.login.login_main(cls.username,cls.password)
        # 进入修改密码页面
        cls.alter_pwd.enter_alterPwd_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()

    def test_alterPwd001(self):
        '''登陆密码为空校验'''
        # 获取测试数据
        Data = testData["TestCase001"]
        self.base.print_case_name(Data["CaseName"])
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入新密码
        self.alter_pwd.input_new_pwd(new_pwd=Data["NewPwd"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(confirm_pwd=Data["ConfirmPwd"])
        self.base.sleep(1)
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alter_pwd.get_old_pwd_msg())

    def test_alterPwd002(self):
        '''新密码为空校验'''
        # 获取测试数据
        Data = testData["TestCase002"]
        self.base.print_case_name(Data["CaseName"])
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入登陆密码
        self.alter_pwd.input_old_pwd(old_pwd=self.password)
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(confirm_pwd=Data["ConfirmPwd"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alter_pwd.get_new_pwd_msg())

    def test_alterPwd003(self):
        '''新密码为空校验'''
        # 获取测试数据
        Data = testData["TestCase003"]
        self.base.print_case_name(Data["CaseName"])
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入登陆密码
        self.alter_pwd.input_old_pwd(old_pwd=self.password)
        # 输入新密码
        self.alter_pwd.input_new_pwd(new_pwd=Data["NewPwd"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alter_pwd.get_confirm_pwd_msg())

    @ddt.data(*ddtData)
    def test_alterPwd004(self,ddtData):
        '''修改密码逻辑/密码格式校验'''
        # 打印用例名称
        self.base.print_case_name(ddtData["CaseName"])
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入旧密码
        self.alter_pwd.input_old_pwd(old_pwd=self.password)
        # 输入新密码
        self.alter_pwd.input_new_pwd(new_pwd=ddtData["NewPwd"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(confirm_pwd=ddtData["ConfirmPwd"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        self.base.sleep(1)
        # 获取系统提示
        msg = self.base.get_system_msg()
        # 写入新改的密码
        if msg == '修改成功':
            rwconfig.write_config_data("蓝魔科技","password",self.new_pwd)
            print("New password: {0}.".format(self.new_pwd))
        # 断言
        self.assert_mode.assert_equal(ddtData["expect"],msg)

    def test_alterPwd005(self):
        '''登陆密码不正确校验'''
        # 获取测试数据
        Data = testData["TestCase005"]
        self.base.print_case_name(Data["CaseName"])
        # 点击密码后面的修改
        self.alter_pwd.click_alter_pwd()
        # 输入登陆密码
        self.alter_pwd.input_old_pwd(old_pwd=Data["OldPwd"])
        # 输入新密码
        self.alter_pwd.input_new_pwd(new_pwd=Data["NewPwd"])
        # 输入确认密码
        self.alter_pwd.input_confirm_pwd(confirm_pwd=Data["ConfirmPwd"])
        # 点击确定
        self.alter_pwd.click_confirm_alterPwd()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.base.get_system_msg())

    @ddt.data(*ddtData1)
    def test_alterPwd006(self,ddtData1):
        """修改密码后登录逻辑校验"""
        # 获取测试用例名称
        self.base.print_case_name(ddtData1["CaseName"])
        # 刷新页面
        self.base.refresh_page()
        # 调用登录
        self.login.enter_login_page()
        self.login.input_username(UserName=ddtData1["username"])
        self.login.input_password(PassWord=ddtData1["password"])
        self.login.click_login_button()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddtData1["expect"],self.base.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 退出驱动
        cls.base.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Alter_Password("test_alterPwd001"))
    suit.addTest(Alter_Password("test_alterPwd002"))
    suit.addTest(Alter_Password("test_alterPwd003"))
    suit.addTest(Alter_Password("test_alterPwd004"))
    suit.addTest(Alter_Password("test_alterPwd005"))
    suit.addTest(Alter_Password("test_alterPwd006"))
    unittest.TextTestRunner().run(suit)
