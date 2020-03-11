# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:26

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.facilitatorPage import FacilitatorPage
import unittest,ddt

@ddt.ddt
class Visit_Facilitator(unittest.TestCase):

    """ 【添加服务商功能】 """

    # 实例化类
    readExcel = Read_Excel("visitFacilitator")
    # ddt 测试用例集合
    case_list = [
        "add_facilitator_002","add_facilitator_003","add_facilitator_004",
        "add_facilitator_005","add_facilitator_006","add_facilitator_007",
        "add_facilitator_008","add_facilitator_009"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.server_branch = FacilitatorPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "visitFacilitator")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入客户列表页面
        cls.server_branch.enter_customer_list_page()
        cls.base.sleep(1)

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 点击添加服务商按钮
        self.server_branch.click_add_server_branch()
        # 时间加载
        self.base.sleep(1)

    @unittest.skipUnless(readExcel.get_isRun_text("add_facilitator_001"),"-跳过不执行该用例")
    def test_add_facilitator001(self):
        """输入客户手机号自动带出服务商名称校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("add_facilitator_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 输入客户手机号
        self.server_branch.input_customer_phone_num(data["手机号码"])
        self.base.sleep(1)
        # 获取自动带出的客户名字
        branch_name = self.server_branch.get_customer_auto_name()
        # 断言
        self.assertMode.assert_equal(data,branch_name)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_add_facilitator002(self,ddt_data):
        """添加服务商功能测试用例"""

        # 输出测试用例名称
        self.base.print_case_name(ddt_data)
        # 输入客户手机号
        self.server_branch.input_customer_phone_num(ddt_data["手机号码"])
        self.base.sleep(1)
        # 清除自动带出的名称
        self.server_branch.clear_customer_name()
        # 输入客户名称备注
        self.server_branch.input_customer_name(ddt_data["客户备注"])
        # 选择合作工单类型
        self.server_branch.select_send_to_someone(ddt_data["合作类型"])
        # 点击确定
        self.server_branch.click_confirm_add_branch()
        # 断言
        self.assertMode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Visit_Facilitator)

    unittest.TextTestRunner().run(suit)

