#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/22 11:02

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest,rwconfig
from public.page.loginPage import LoginPage
from public.page.alterPwdPage import AlterPwdPage
import unittest,ddt
"""
网点登录后修改手机号：
1、修改手机-登录密码为空校验 2、修改手机-手机号为空校验 3、修改手机-验证码为空校验 4、修改手机-错误的登陆密码校验
5、修改手机-错误的验证码校验 6、修改手机-已经注册过的手机号校验 7、修改手机-手机号码左边界值校验 8、修改手机-手机号码右边界值校验
9、修改手机-手机号码格式特殊符号校验 10、修改手机-手机号码格式字母校验 11、修改手机-手机号码格式汉字校验
"""
# 获取测试数据
testData = get_test_data()["AlterPwdPage"]["alter_pheNum_fnc"]
ddtData = testData["TestCase006"]

@ddt.ddt
class Alter_PhoneNum(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.alterPwd = AlterPwdPage(cls.driver)
        cls.assert_mode= Assert(cls.driver)
        # 开始脚本
        mytest.start_test()
        # 获取登录的账号密码
        cls.username = rwconfig.read_config_data('西安好家帮家政有限公司','username')
        cls.password = rwconfig.read_config_data('西安好家帮家政有限公司','password')
        # 调用登录主程序登录
        cls.login.login_main(cls.username,cls.password)
        # 进入修改密码页面
        cls.alterPwd.enter_alterPwd_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 点击手机号->修改
        self.alterPwd.click_alter_pheNum()

    def test_alter_phoneNum001(self):
        """登录密码为空校验"""
        # 获取测试数据
        Data = testData["TestCase001"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入手机号码
        self.alterPwd.input_phe_num(phone_num=Data["PhoneNum"])
        # 输入验证码
        self.alterPwd.input_code_number(code_num=Data["CodeNum"])
        # 点击确定
        self.alterPwd.click_confirm_alter()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alterPwd.get_login_pwd_msg())

    def test_alter_phoneNum002(self):
        """手机号为空校验"""
        # 获取测试数据
        Data = testData["TestCase002"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alterPwd.input_login_pwd(login_pwd=self.password)
        # 输入验证码
        self.alterPwd.input_code_number(code_num=Data["CodeNum"])
        # 点击确定
        self.alterPwd.click_confirm_alter()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alterPwd.get_phone_num_msg())

    def test_alter_phoneNum003(self):
        """验证码为空校验"""
        # 获取测试数据
        Data = testData["TestCase003"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alterPwd.input_login_pwd(login_pwd=self.password)
        # 输入手机号
        self.alterPwd.input_phe_num(phone_num=Data["PhoneNum"])
        # 点击确定
        self.alterPwd.click_confirm_alter()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alterPwd.get_code_input_msg())

    def test_alter_phoneNum004(self):
        """错误的登陆密码修改手机校验"""
        # 获取测试数据
        Data = testData["TestCase004"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入登陆密码
        self.alterPwd.input_login_pwd(login_pwd=Data["Pwd"])
        # 输入手机号
        self.alterPwd.input_phe_num(phone_num=Data["PhoneNum"])
        # 输入验证码
        self.alterPwd.input_code_number(code_num=Data["CodeNum"])
        # 点击确定
        self.alterPwd.click_confirm_alter()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.base.get_system_msg())

    def test_alter_phoneNum005(self):
        """错误的验证码修改手机校验"""
        # 获取测试数据
        Data = testData["TestCase005"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alterPwd.input_login_pwd(login_pwd=self.password)
        # 输入手机号
        self.alterPwd.input_phe_num(phone_num=Data["PhoneNum"])
        # 输入验证码
        self.alterPwd.input_code_number(code_num=Data["CodeNum"])
        # 点击确定
        self.alterPwd.click_confirm_alter()
        # 断言
        self.assert_mode.assert_equal(Data["expect"], self.base.get_system_msg())

    @ddt.data(*ddtData)
    def test_alter_phoneNum006(self,ddtData):
        """获取手机验证码逻辑校验"""
        # 打印测试用例名称
        self.base.print_case_name(ddtData["CaseName"])
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alterPwd.input_login_pwd(login_pwd=self.password)
        # 输入手机号
        self.alterPwd.input_phe_num(phone_num=ddtData["PhoneNum"])
        # 点击确定
        self.alterPwd.click_code_button()
        # 断言
        self.assert_mode.assert_equal(ddtData["expect"],self.base.get_system_msg())

    def test_alter_phoneNum007(self):
        """错误的验证码修改手机校验"""
        # 获取测试数据
        Data = testData["TestCase007"]
        # 打印测试用例名称
        self.base.print_case_name(Data["CaseName"])
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alterPwd.input_login_pwd(login_pwd=self.password)
        # 输入手机号
        self.alterPwd.input_phe_num(phone_num=Data["PhoneNum"])
        # 点击确定
        self.alterPwd.click_code_button()
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.alterPwd.get_code_button_att())

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.base.quit_browser()
        # 结束测试
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum001'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum002'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum003'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum004'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum005'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum006'))
    suit.addTest(Alter_PhoneNum('test_alter_phoneNum007'))

    unittest.TextTestRunner().run(suit)