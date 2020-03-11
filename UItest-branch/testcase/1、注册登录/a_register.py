#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/29 10:25

from public.common import createUser
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.registerPage import RegisterPage
import unittest,ddt

@ddt.ddt
class Register_Branch(unittest.TestCase):

    """ 【PC注册功能测试用例脚本】 """

    # 获取ddt数据的用例id列表
    case_list = [
        "register_001", "register_002", "register_003", "register_004",
        "register_005", "register_006", "register_007", "register_008",
        "register_009", "register_010", "register_011", "register_012",
        "register_013", "register_014"
    ]
    # 实例化excel操作类
    operate = Read_Excel("register")
    # 获取ddt模块测试数据
    ddt_data = operate.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.register = RegisterPage(cls.driver)
        cls.assertMode = Assert(cls.driver,"register")

    def register_function(
            self,username,phone_number,code_number,login_pwd,confirm_pwd):
        self.base.refresh_page()
        # 进入登录页面
        self.register.enter_register_page()
        # 点击立即注册
        self.register.click_free_register()
        # 输入用户名
        self.register.input_username(username)
        # 输入手机号码
        self.register.input_phone_number(phone_number)
        # 输入验证码
        self.register.input_code_number(code_number)
        # 输入登陆密码
        self.register.input_login_pwd(login_pwd)
        # 输入确认登陆密码
        self.register.input_confirm_pwd(confirm_pwd)
        # 点击马上注册
        self.register.click_register_btn()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case # 方法中 判断数据中的isRun字段 为No跳过执行
    def test_register001(self,ddt_data):
        """异常操作注册系统校验"""

        # 获取测试用例名称
        self.base.print_case_name(ddt_data)
        # 输入用户名
        username = ddt_data["用户名"]
        # 输入手机号码
        phone_number = ddt_data["手机号"]
        # 输入验证码
        code_number = ddt_data["验证码"]
        # 输入登陆密码
        login_pwd = ddt_data["登录密码"]
        # 输入确认登陆密码
        confirm_pwd = ddt_data["确认密码"]
        self.register_function(username,phone_number,code_number,login_pwd,confirm_pwd)
        self.base.sleep(2)
        # 获取注册的提示信息
        Msg = self.register.get_system_message()
        # 添加断言
        self.assertMode.assert_equal(ddt_data,Msg)

    # unittest.skipUnless(condition,reason) 方法中 condition 为False跳过执行
    @unittest.skipUnless(operate.get_isRun_text("register_015"),"-跳过不执行该用例")
    def test_register002(self):
        """成功注册系统账号校验"""

        # 获取测试数据
        test_data = self.operate.get_dict_data("register_015")
        # 获取测试用例名称
        self.base.print_case_name(test_data)
        # 输入用户名
        username = createUser.create_username()
        # 输入手机号码
        phone_number = createUser.create_phoneNum()
        # 输入验证码
        code_number = test_data["验证码"]
        # 输入登陆密码
        login_pwd = test_data["登录密码"]
        # 输入确认登陆密码
        confirm_pwd = test_data["确认密码"]
        self.register_function(username,phone_number,code_number,login_pwd,confirm_pwd)
        self.base.sleep(1)
        Msg = self.login.get_system_message()
        # 添加断言
        self.assertMode.assert_equal(test_data,Msg)
        # 获取当前时间
        CreateTime = self.register.get_now_time(Time=True)
        if Msg == '注册成功':
            # 写入新注册的账号密码信息
            with open(regAccountPath,'a') as f:
                f.write('注册时间：%s,新用户名：%s,手机号：%s,密码：%s'
                        %(CreateTime,username,phone_number,test_data["登录密码"])+'\n')
            print(' * Write branch account to txt is success, directory path: {0}'.format(regAccountPath))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Register_Branch)
    unittest.TextTestRunner().run(suit)