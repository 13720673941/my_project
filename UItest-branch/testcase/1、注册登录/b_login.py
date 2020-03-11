#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/21 14:59

from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.common.basePage import BasePage
from public.common.rwConfig import *
from public.common import myDecorator
import unittest,ddt

@ddt.ddt
class Login_Branch(unittest.TestCase):

    """ 【PC登录功能测试用例脚本】 """

    # ddt 模式测试数据用例集合
    case_list = [
        "login_001","login_002","login_003",
        "login_004","login_005","login_006"
    ]
    # 获取账号配置文件中的账号密码
    username = read_config_data('T西安好家帮家政有限公司','username')
    password = read_config_data('T西安好家帮家政有限公司','password')
    # 设置excel测试用例中的用户名密码
    Update_Excel.update_test_data("login","login_006",{"用户名":username,"密码":password})
    # 获取ddt数据类型
    ddt_data = Read_Excel("login").get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化断言类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "login")

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case # 方法中 ddt_data["isRun"]为No跳过执行
    def test_login(self,ddt_data):
        """网点用户成功登录校验"""

        # 获取测试用例名称
        self.base.print_case_name(ddt_data)
        # 进入登录页面
        self.login.enter_login_page()
        # 刷新页面清除数据
        self.base.refresh_page()
        # 输入用户名
        self.login.input_username(ddt_data["用户名"])
        # 输入密码
        self.login.input_password(ddt_data["密码"])
        # 点击登陆按钮
        self.login.click_login_button()
        # 等待元素加载
        self.base.sleep(1)
        # 添加断言
        self.assertMode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Login_Branch)

    result = unittest.TextTestRunner().run(suit)

