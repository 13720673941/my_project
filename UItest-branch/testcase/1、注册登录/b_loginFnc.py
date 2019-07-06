#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/21 14:59

from public.common import writetestresult
from public.common import driver,rwconfig
from public.common import mytest
from public.common.assertmode import Assert
from public.page.loginPage import LoginPage
from public.common.basepage import BasePage
from public.common import getdata
import unittest,ddt
'''
网点登录测试用例脚本：
1、正确用户名密码登录 2、用户名密码为空登录 3、用户名为空密码不为空登录
4、用户名不为空密码为空登录 5、用户名不正确密码正确登录 6、用户名正确密码不正确登录
'''
# 获取登录数据信息
loginData = getdata.get_test_data()["LoginPage"]
# 默认写入测试结果
isWrite=True
@ddt.ddt
class Branch_Login(unittest.TestCase):
    # setUpClass类方法，加装饰器@classmethod值调用一次
    @classmethod
    def setUpClass(cls):
        # 浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.loginPage = LoginPage(cls.dr)
        cls.basePage = BasePage(cls.dr)
        cls.assertMode = Assert(cls.dr)
        # 开始执行用例
        mytest.start_test()
        cls.loginPage.enter_login_page()
        # 获取登陆新密码
        cls.new_pwd = rwconfig.read_config_data('蓝魔科技','password')
        # 设置登陆成功的密码
        loginData[-1]["password"] = cls.new_pwd

    @ddt.data(*loginData)
    def test_login(self,loginData):
        # 获取测试用例名称
        self.basePage.print_case_name(loginData["CaseName"])
        # 刷新页面
        self.basePage.refresh_page()
        # 输入用户名
        self.loginPage.input_username(UserName=loginData["username"])
        # 输入密码
        self.loginPage.input_password(PassWord=loginData["password"])
        # 点击登陆按钮
        self.loginPage.click_login_button()
        # 等待元素加载
        self.basePage.sleep(1)
        # 获取系统提示信息
        Msg = self.loginPage.get_system_msg()
        # 添加断言,封装的AssertIn判断是否在预期的字段相等
        isSuccess = self.assertMode.assert_equal(loginData["expect"],Msg)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'BranchLogin',loginData["CaseName"])

    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Branch_Login("test_login"))
    unittest.TextTestRunner().run(suit)