# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:56

from public.common.operateExcel import *
from public.common import myDecorator
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.masterListPage import MasterListPage
import unittest,ddt

@ddt.ddt
class Visit_Master(unittest.TestCase):

    """ 【添加师傅功能】 """

    # 实例化类
    readExcel = Read_Excel("visitMaster")
    # ddt 数据类型测试用例编码
    case_list = [
        "visit_master_005","visit_master_006",
        "visit_master_007","visit_master_008"
    ]
    # 获取测试数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.visit_master = MasterListPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"visitMaster")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入师傅列表页面
        cls.visit_master.enter_master_list_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 点击添加师傅
        self.visit_master.click_add_master_btn()
    
    @unittest.skipUnless(readExcel.get_isRun_text("visit_master_001"),"-跳过不执行该用例")
    def test_visit_master001(self):
        """自动带出师傅名称校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_master_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 输入师傅手机号
        self.visit_master.input_master_phone_num(data["手机号码"])
        # 点击师傅名称输入框
        self.visit_master.click_master_name_input()
        self.base.sleep(1)
        # 获取带出的师傅名字
        master_name = self.visit_master.get_master_name_input_value()
        # 断言
        self.assert_mode.assert_equal(data,master_name)

    @unittest.skipUnless(readExcel.get_isRun_text("visit_master_002"),"-跳过不执行该用例")
    def test_visit_master002(self):
        """未注册的师傅邀请提示发送短信校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_master_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 输入师傅手机号
        self.visit_master.input_master_phone_num(data["手机号码"])
        # 点击师傅名称输入框
        self.visit_master.click_master_name_input()
        self.base.sleep(1)
        # 获取未注册师傅提示字段
        send_message_text = self.visit_master.get_msg_of_master_no_reg()
        # 断言
        self.assert_mode.assert_equal(data,send_message_text)

    @unittest.skipUnless(readExcel.get_isRun_text("visit_master_003"),"-跳过不执行该用例")
    def test_visit_master003(self):
        """师傅手机号为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_master_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 输入师傅名字
        self.visit_master.input_master_name(data["师傅备注"])
        # 点击确定
        self.visit_master.click_confirm_add_master()
        # 获取师傅手机号输入框的属性
        phe_input_att = self.visit_master.get_master_phe_input_att()
        # 断言
        self.assert_mode.assert_in(data,phe_input_att)

    @unittest.skipUnless(readExcel.get_isRun_text("visit_master_004"),"-跳过不执行该用例")
    def test_visit_master004(self):
        """师傅名字为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("visit_master_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 输入师傅手机号
        self.visit_master.input_master_phone_num(data["手机号码"])
        # 点击确定
        self.visit_master.click_confirm_add_master()
        # 获取师傅手机号输入框的属性
        name_input_att = self.visit_master.get_master_name_input_att()
        # 断言
        self.assert_mode.assert_in(data,name_input_att)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_visit_master005(self,ddt_data):
        """添加师傅逻辑校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 输入师傅手机号
        self.visit_master.input_master_phone_num(ddt_data["手机号码"])
        # 输入师傅名称
        self.visit_master.click_master_name_input()
        self.base.sleep(1)
        self.visit_master.input_master_name(ddt_data["师傅备注"])
        # 点击确定添加
        self.visit_master.click_confirm_add_master()
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Visit_Master)
    unittest.TextTestRunner().run(suits)