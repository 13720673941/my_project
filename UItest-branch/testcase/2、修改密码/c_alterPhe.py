#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/22 11:02

from public.common.assertMode import Assert
from public.common import getNewPwd
from public.common import myDecorator
from public.common.operateExcel import Read_Excel
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.alterPwdPage import AlterPwdPage
import unittest,ddt

@ddt.ddt
class Alter_PhoneNum(unittest.TestCase):

    """"【修改手机号功能测试用例脚本】"""

    # 获取ddt测试数据用例编号
    case_list = [
        "alter_phe_006","alter_phe_007","alter_phe_008",
        "alter_phe_009","alter_phe_010","alter_phe_011"
    ]
    # 获取数据
    operate = Read_Excel("alterPhe")
    ddt_data = operate.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化断言类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.alter_pwd = AlterPwdPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"alterPhe")
        # 获取新旧密码
        cls.old_pwd, cls.new_pwd = getNewPwd.get_new_pwd()
        # 调用登录主程序登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入修改密码页面
        cls.alter_pwd.enter_alterPwd_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_001"),"-跳过不执行该用例")
    def test_alter_phoneNum001(self):
        """登录密码为空校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入手机号码
        self.alter_pwd.input_phe_num(data["手机号"])
        # 输入验证码
        self.alter_pwd.input_code_number(data["验证码"])
        # 点击确定
        self.alter_pwd.click_confirm_alter()
        Msg = self.alter_pwd.get_login_pwd_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_002"), "-跳过不执行该用例")
    def test_alter_phoneNum002(self):
        """手机号为空校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(data["登录密码"])
        # 输入验证码
        self.alter_pwd.input_code_number(data["验证码"])
        # 点击确定
        self.alter_pwd.click_confirm_alter()
        # 获取提示信息
        Msg = self.alter_pwd.get_phone_num_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_003"), "-跳过不执行该用例")
    def test_alter_phoneNum003(self):
        """验证码为空校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(data["登录密码"])
        # 输入手机号
        self.alter_pwd.input_phe_num(data["手机号"])
        # 点击确定
        self.alter_pwd.click_confirm_alter()
        Msg = self.alter_pwd.get_code_input_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_004"),"-跳过不执行该用例")
    def test_alter_phoneNum004(self):
        """错误的登陆密码校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(data["登录密码"])
        # 输入手机号
        self.alter_pwd.input_phe_num(data["手机号"])
        # 输入验证码
        self.alter_pwd.input_code_number(data["验证码"])
        # 点击确定
        self.alter_pwd.click_confirm_alter()
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_005"), "-跳过不执行该用例")
    def test_alter_phoneNum005(self):
        """验证码不正确校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_005")
        # 赋值
        data["登录密码"] = self.old_pwd
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(data["登录密码"])
        # 输入手机号
        self.alter_pwd.input_phe_num(data["手机号"])
        # 输入验证码
        self.alter_pwd.input_code_number(data["验证码"])
        # 点击确定
        self.alter_pwd.click_confirm_alter()
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data, Msg)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_alter_phoneNum006(self,ddt_data):
        """获取手机验证码逻辑校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(ddt_data["登录密码"])
        # 输入手机号
        self.alter_pwd.input_phe_num(ddt_data["手机号"])
        # 点击确定
        self.alter_pwd.click_code_button()
        # 获取提示信息
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(ddt_data,Msg)

    @unittest.skipUnless(operate.get_isRun_text("alter_phe_012"), "-跳过不执行该用例")
    def test_alter_phoneNum007(self):
        """正确手机号发送验证码校验"""

        # 获取测试数据
        data = self.operate.get_dict_data("alter_phe_012")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击手机号->修改
        self.alter_pwd.click_alter_pheNum()
        # 输入登陆密码/获取配置文件里面的密码，上个脚本会修改密码
        self.alter_pwd.input_login_pwd(data["登录密码"])
        # 输入手机号
        self.alter_pwd.input_phe_num(data["手机号"])
        # 点击确定
        self.alter_pwd.click_code_button()
        # 获取发送成后的按钮属性
        self.base.sleep(1)
        att_text = self.alter_pwd.get_code_button_att()
        # 断言
        self.assert_mode.assert_equal(data,att_text)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Alter_PhoneNum)

    unittest.TextTestRunner().run(suit)