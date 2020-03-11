#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/28 10:47

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.dealerPage import DealerPage
import unittest,ddt

@ddt.ddt
class Visit_Dealer(unittest.TestCase):

    """ 【邀请经销商功能】 """

    # 实例化类
    read_excel = Read_Excel("visitDealer")
    # ddt 测试数据 id
    case_list = [
        "visit_dealer_002","visit_dealer_003","visit_dealer_004",
        "visit_dealer_005","visit_dealer_006","visit_dealer_007",
        "visit_dealer_008"
    ]
    # 获取ddt测试数据
    ddt_data = read_excel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.manage_branch = DealerPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "visitDealer")
        # 登录测试网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入添加经销商页面
        cls.manage_branch.enter_dealer_page()

    def setUp(self):
        self.base.refresh_page()
        # 点击添加经销商
        self.manage_branch.click_add_manage_branch()

    @unittest.skipUnless(read_excel.get_isRun_text("visit_dealer_001"),"-跳过不执行该用例")
    def test_add_dealer001(self):
        """已经注册的用户可以自动带出用户名称校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("visit_dealer_001")
        # 打印测试名称
        self.base.print_case_name(data)
        # 输入客户主账号
        self.manage_branch.input_branch_phone_num(data["手机号码"])
        self.base.sleep(1)
        # 获取自动带出的经销商名称
        branch_name = self.manage_branch.get_branch_name()
        # 判断
        self.assert_mode.assert_equal(data,branch_name)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_add_dealer002(self,ddt_data):
        """添加经销商功能校验"""

        # 打印测试名称
        self.base.print_case_name(ddt_data)
        # 输入客户主账号
        self.manage_branch.input_branch_phone_num(ddt_data["手机号码"])
        self.base.sleep(1)
        # 输入客户名称
        self.manage_branch.input_branch_name(ddt_data["名称备注"])
        self.base.sleep(1)
        # 点击确定按钮
        self.manage_branch.click_confirm_add()
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Visit_Dealer)

    unittest.TextTestRunner().run(suits)
