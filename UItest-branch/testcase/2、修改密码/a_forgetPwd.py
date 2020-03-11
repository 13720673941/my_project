#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/27 10:44

from public.common import rwConfig
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.forgetPwdPage import ForgetPwd
from public.common.operateExcel import *
from public.common import getNewPwd
from public.common import myDecorator
import unittest,ddt

@ddt.ddt
class Forget_Pwd(unittest.TestCase):

    """ 【PC忘记密码功能测试用例脚本】 """

    # 需要加入ddt中的测试用例id
    case_list = [
        "forget_pwd_001","forget_pwd_002","forget_pwd_003","forget_pwd_004","forget_pwd_005",
        "forget_pwd_006","forget_pwd_007","forget_pwd_008","forget_pwd_009","forget_pwd_010",
        "forget_pwd_011"
    ]
    # 获取ddt模式测试数据
    read_excel = Read_Excel("forgetPwd")
    ddt_data = read_excel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化断言类
        cls.driver = web_driver()
        cls.login = LoginPage(cls.driver)
        cls.base = BasePage(cls.driver)
        cls.forget_pwd = ForgetPwd(cls.driver)
        cls.assert_mode = Assert(cls.driver, "forgetPwd")
        # 获取新旧密码
        cls.old_pwd,cls.new_pwd = getNewPwd.get_new_pwd()
        # 参数赋值
        cls.ddt_data[-1]["新密码"] = cls.new_pwd
        cls.ddt_data[-1]["确认密码"] = cls.new_pwd

    def setUp(self):
        # 进入登录页面
        self.login.enter_login_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_forgetPwd001(self,ddt_data):
        """忘记密码功能测试用例脚本"""

        # 获取测试用例名称
        self.base.print_case_name(ddt_data)
        # 点击忘记密码按钮
        self.forget_pwd.click_forgetPwd_btn()
        # 输入手机号
        self.forget_pwd.input_phoneNum(ddt_data["手机号"])
        # 输入验证码
        self.forget_pwd.input_codeNum(ddt_data["验证码"])
        # 输入新密码
        self.forget_pwd.input_new_pwd(ddt_data["新密码"])
        # 输入确认密码
        self.forget_pwd.input_confirm_pwd(ddt_data["确认密码"])
        # 点击重置密码按钮
        self.forget_pwd.click_reset_pwd_btn()
        # 时间加载等待
        self.base.sleep(1)
        # 获取系统系统提示信息
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(ddt_data,Msg)
        if Msg == '密码修改成功':
            # 把修改的密码写入配置文件中
            rwConfig.write_config_data('T西安好家帮家政有限公司','password',self.new_pwd)

    @unittest.skipUnless(read_excel.get_isRun_text("forget_pwd_012"),"-跳过不执行该用例")
    def test_forgetPwd002(self):
        """获取验证码手机号为空校验"""

        # 获取测试用例
        test_data = self.read_excel.get_dict_data("forget_pwd_012")
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 刷新清除数据
        self.base.refresh_page()
        # 点击忘记密码按钮
        self.forget_pwd.click_forgetPwd_btn()
        # 输入手机号
        self.forget_pwd.input_phoneNum(test_data["手机号"])
        # 点击获取验证码按钮
        self.forget_pwd.click_getCode_btn()
        # 时间等待元素加载
        self.base.sleep(1)
        # 获取系统提示字段
        Msg = self.login.get_system_msg()
        # 断言结果
        self.assert_mode.assert_equal(test_data,Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("forget_pwd_013"),"-跳过不执行该用例")
    def test_forgetPwd003(self):
        """获取验证码手机号未注册校验"""

        # 获取测试用例
        test_data = self.read_excel.get_dict_data("forget_pwd_013")
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 点击忘记密码按钮
        self.forget_pwd.click_forgetPwd_btn()
        # 输入手机号
        self.forget_pwd.input_phoneNum(test_data["手机号"])
        # 点击获取验证码按钮
        self.forget_pwd.click_getCode_btn()
        # 时间等待元素加载
        self.base.sleep(1)
        # 获取系统提示字段
        Msg = self.login.get_system_msg()
        # 断言结果
        self.assert_mode.assert_equal(test_data,Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("forget_pwd_014"),"-跳过不执行该用例")
    def test_forgetPwd004(self):
        """发送成功验证码校验"""

        # 获取测试数据
        test_data = self.read_excel.get_dict_data("forget_pwd_014")
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 点击忘记密码
        self.forget_pwd.click_forgetPwd_btn()
        # 输入手机号
        self.forget_pwd.input_phoneNum(test_data["手机号"])
        # 点击获取验证码按钮
        self.forget_pwd.click_getCode_btn()
        # 时间等待元素加载
        self.base.sleep(1)
        # 获取发送成功后按钮元素属性
        Attribute = self.forget_pwd.get_codeBtn_attribute()
        # 断言
        self.assert_mode.assert_equal(test_data,Attribute)

    @unittest.skipUnless(read_excel.get_isRun_text("forget_pwd_015"),"-跳过不执行该用例")
    def test_forgetPwd005(self):
        """修改密码后旧密码不能成功登录校验"""

        # 获取测试数据
        test_data = self.read_excel.get_dict_data("forget_pwd_015")
        # 赋值
        test_data["密码"] = self.old_pwd
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 刷新页面
        self.base.refresh_page()
        self.login.input_username(test_data["手机号"])
        self.login.input_password(test_data["密码"])
        self.login.click_login_button()
        self.base.sleep(1)
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(test_data,Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("forget_pwd_016"),"-跳过不执行该用例")
    def test_forgetPwd006(self):
        """修改密码后新密码可以成功登录校验"""

        # 获取测试数据
        test_data = self.read_excel.get_dict_data("forget_pwd_016")
        # 赋值
        test_data["密码"] = self.new_pwd
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 刷新页面
        self.base.refresh_page()
        self.login.input_username(test_data["手机号"])
        self.login.input_password(test_data["密码"])
        self.login.click_login_button()
        self.base.sleep(1)
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(test_data,Msg)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Forget_Pwd)
    unittest.TextTestRunner().run(suit)

