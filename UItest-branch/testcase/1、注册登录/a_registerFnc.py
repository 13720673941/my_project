#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/29 10:25

from public.common import createuser
from public.common.assertmode import Assert
from config.pathconfig import *
from public.common import mytest
from public.common import driver,writetestresult
from public.page.registerPage import RegisterPage
from public.common.basepage import BasePage
from public.common import getdata
import unittest,ddt
'''
网点注册测试用例脚本：
1、注册-用户名为空校验 2、注册-手机号为空校验 3、注册-验证码为空校验 4、注册-新密码为空校验 5、注册-确认密码为空校验
6、注册-已经注册的用户名校验 7、注册-已经注册的手机号校验 8、注册-错误验证码校验 9、注册-两个密码不同校验 10、注册-用户名格式校验
11、注册-手机号格式校验 12、注册-密码特殊字符校验 13、注册-密码上点值校验 14、注册-密码离点值校验 15、注册-数据正确成功注册校验
'''
# 读取注册脚本测试数据
Data = getdata.get_test_data()["RegisterPage"]
# 默认写入测试结果
isWrite=True
@ddt.ddt
class Register_Branch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #  # 随机生成手机号用户名
        #  cls.username = createuser.create_username()
        #  cls.phoneNum = createuser.create_phoneNum()
        #  # 替换注册数据中成功注册的数据的手机号和用户名
        #  Data[-1]["username"] = cls.username
        #  Data[-1]["PhoneNum"] = cls.phoneNum
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化类
        cls.basePage = BasePage(cls.dr)
        cls.registerPage = RegisterPage(cls.dr)
        cls.assertMode = Assert(cls.dr)
        # 打开网点登录页面
        mytest.start_test()
        cls.registerPage.enter_register_page()

    @ddt.data(*Data)
    def test_registerBranch(self,Data):
        '''网点注册测试用例'''
        # 获取测试用例名称
        self.basePage.print_case_name(Data["CaseName"])
        # 刷新页面信息
        self.basePage.refresh_page()
        # 点击免费注册
        self.registerPage.click_free_register()
        # 输入用户名
        self.registerPage.input_username(UserName=Data["username"])
        # 输入手机号码
        self.basePage.sleep(2)
        self.registerPage.input_phoneNum(PhoneNum=Data["PhoneNum"])
        # 输入验证码
        self.registerPage.input_codeNum(CodeNum=Data["CodeNum"])
        # 输入登陆密码
        self.registerPage.input_login_pwd(LoginPwd=Data["NewPwd"])
        # 输入确认登陆密码
        self.registerPage.input_confirm_pwd(ConfirmPwd=Data["ConfirmPwd"])
        # 点击马上注册
        self.registerPage.click_register_btn()
        self.basePage.sleep(2)
        # 获取注册的提示信息
        Msg = self.basePage.get_system_msg()
        # 获取当前时间
        CreateTime = self.basePage.get_now_time(Time=True)
        # 添加断言
        isSuccess = self.assertMode.assert_equal(Data["expect"],Msg)
        if Msg == '注册成功':
            # 写入新注册的账号密码信息
            with open(accountDataPath,'a') as f:
                f.write('注册时间：%s,新用户名：%s,手机号：%s,密码：%s'%(CreateTime,self.username,self.phoneNum,Data["NewPwd"])+'\n')
                print('*Write branch account to txt is success, directory path: {0}'.format(accountDataPath))
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'RegisterBranch',Data["CaseName"])

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Register_Branch('test_registerBranch'))
    unittest.TextTestRunner().run(suit)