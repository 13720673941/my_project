# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/27 10:44

from public.common import writetestresult
from public.common import driver,getdata,rwconfig
from public.page.forgetPwdPage import ForgetPwd
from public.page.loginPage import LoginPage
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common import mytest
import unittest,ddt
'''
网点忘记密码功能测试用例脚本：
1、手机号为空校验 2、验证码为空校验 3、新密码为空校验 4、确认密码为空校验 5、未注册手机号校验
6、验证码不正确校验 7、新密码长度上点值校验 8、新密码长度离点值校验 9、新密码特殊字符校验
10、新密码与确认密码不同校验 11、修改密码成功校验 12、获取验证码-手机号为空校验 13、获取验证码-手机号未注册校验
14、获取验证码-正确发送验证码校验 15、修改成功的密码可以登录 16、旧密码不能成功登陆
'''
#获取修改密码测试数据
Data = getdata.get_test_data()["ForgetPwdPage"]["forget_pwd_fnc"]
Data1 = getdata.get_test_data()["ForgetPwdPage"]["get_code_fnc"]
Data3 = getdata.get_test_data()["ForgetPwdPage"]["logic_test"]
#默认写入测试结果
isWrite=True
@ddt.ddt
class Forget_Pwd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化类
        cls.basePage = BasePage(cls.dr)
        cls.forgetPwd = ForgetPwd(cls.dr)
        cls.login = LoginPage(cls.dr)
        cls.assertMode = Assert(cls.dr)
        #获取旧密码
        cls.old_pwd = rwconfig.read_config_data('蓝魔科技','password')
        #旧密码替换 15 测试用例的密码
        Data3[0]["password"] = cls.old_pwd
        #获取新密码
        for pwd in getdata.get_test_data()["ForgetPwdPage"]["PwdList"]:
            if  pwd != cls.old_pwd:
                cls.new_pwd = pwd
        #新密码写入到修改成功的密码参数中
        Data[-1]["NewPwd"] = cls.new_pwd
        Data[-1]["ConfirmPwd"] = cls.new_pwd
        Data3[1]["password"] = cls.new_pwd
        #打开登录页面
        mytest.start_test()
        cls.login.enter_login_page()

    @ddt.data(*Data)
    def test_forgetPwd001(self,Data):
        '''忘记密码功能测试用例脚本'''
        #获取测试用例名称
        self.basePage.print_case_name(Data["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #点击忘记密码按钮
        self.forgetPwd.click_forgetPwd_btn()
        #输入手机号
        self.forgetPwd.input_phoneNum(PhoneNum=Data["PhoneNum"])
        #输入验证码
        self.forgetPwd.input_codeNum(CodeNum=Data["CodeNum"])
        #输入新密码
        self.forgetPwd.input_new_pwd(NewPwd=Data["NewPwd"])
        #输入确认密码
        self.forgetPwd.input_confirm_pwd(ConfirmPwd=Data["ConfirmPwd"])
        #点击重置密码按钮
        self.forgetPwd.click_reset_pwd_btn()
        #时间加载等待
        self.basePage.sleep(2)
        #获取系统系统提示信息
        Msg = self.basePage.get_system_msg()
        #断言
        isSuccess = self.assertMode.assert_equal(Data["expect"],Msg)
        if Msg == '密码修改成功':
            #把修改的密码写入配置文件中
            rwconfig.write_config_data('蓝魔科技','password',self.new_pwd)
            print('New password: {0}'.format(self.new_pwd))
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ForgetPwd',Data['CaseName'])

    @ddt.data(*Data1)
    def test_forgetPwd002(self,Data1):
        '''获取验证码功能校验'''
        #默认执行结果为Fail
        success='FAIL'
        #获取测试用例名称
        self.basePage.print_case_name(Data1["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #点击忘记密码按钮
        self.forgetPwd.click_forgetPwd_btn()
        #输入手机号
        self.forgetPwd.input_phoneNum(PhoneNum=Data1["PhoneNum"])
        #点击获取验证码按钮
        self.forgetPwd.click_getCode_btn()
        #时间等待元素加载
        self.basePage.sleep(1)
        #获取系统提示字段
        Msg = self.basePage.get_system_msg()
        #断言结果
        isSuccess = self.assertMode.assert_equal(Data1["expect"],Msg)
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ForgetPwd',Data1['CaseName'])

    def test_forgetPwd003(self):
        '''发送成功验证码'''
        #获取测试数据
        Data2 = getdata.get_test_data()["ForgetPwdPage"]["send_code_success"]
        #获取测试用例名称
        self.basePage.print_case_name(Data2["CaseName"])
        self.basePage.refresh_page()
        #点击忘记密码按钮
        self.basePage.sleep(1)
        self.forgetPwd.click_forgetPwd_btn()
        #输入手机号
        self.forgetPwd.input_phoneNum(PhoneNum=Data2["PhoneNum"])
        #点击获取验证码按钮
        self.forgetPwd.click_getCode_btn()
        #时间等待元素加载
        self.basePage.sleep(1)
        #获取发送成功后按钮元素属性
        Attribute = self.forgetPwd.get_codeBtn_attribute(AttrName='class')
        #断言
        isSuccess = self.assertMode.assert_equal(Data2["expect"],Attribute)
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ForgetPwd',Data2['CaseName'])

    @ddt.data(*Data3)
    def test_forgetPwd004(self,Data3):
        '''修改密码后逻辑校验'''
        #获取测试用例名称
        self.basePage.print_case_name(Data3["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #调用登录
        self.login.enter_login_page()
        self.login.input_username(UserName=Data3["username"])
        self.login.input_password(PassWord=Data3["password"])
        self.login.click_login_button()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assertMode.assert_equal(Data3["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ForgetPwd',Data3['CaseName'])

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.basePage.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Forget_Pwd('test_forgetPwd'))
    suit.addTest(Forget_Pwd('test_getCodeNum'))
    suit.addTest(Forget_Pwd('test_sendSuccess'))
    unittest.TextTestRunner().run(suit)

