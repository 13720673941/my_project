# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/4 10:56

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createGroupPage import CreateGroupPage
import unittest,ddt

@ddt.ddt
class Create_Group(unittest.TestCase):

    """ 【创建圈子功能】 """

    # 实例化操作类
    readExcel = Read_Excel("createGroup")
    # ddt测试用例编号集合
    caseList = [
        "create_group_001","create_group_002","create_group_003",
        "create_group_004","create_group_005","create_group_006",
        "create_group_007","create_group_008","create_group_009"
    ]
    # 组合ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):
        # 实例化页面类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_group = CreateGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"createGroup")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入我的圈子列表页面
        cls.create_group.enter_my_group_list_page()

    def setUp(self):
        # 清除页面数据
        self.base.refresh_page()
        # 点击创建圈子按钮
        self.create_group.click_create_group_btn()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_create_group001(self,ddt_data):
        """创建圈子必填字段校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 输入圈子名称
        self.create_group.input_group_name(ddt_data["圈子名称"])
        # 选择服务区域
        self.create_group.select_service_area(ddt_data["服务区域"])
        # 选择服务类型
        self.create_group.select_service_type(ddt_data["服务类型"])
        # 选择服务品牌
        self.create_group.select_service_brands(ddt_data["服务品牌"])
        # 选择服务品类
        self.create_group.select_service_kinds(ddt_data["服务品类"])
        # 选择收费设置
        self.create_group.select_charge_rule(ddt_data["服务管理费"])
        # 选择收费模式
        self.create_group.select_charge_mode(ddt_data["收费模式"])
        # 输入起手单数
        self.create_group.input_start_charge_count(ddt_data["起收单数"])
        # 输入费用金额
        self.create_group.input_charge_amount(ddt_data["费用金额"])
        # 选择派单方式
        self.create_group.select_send_order_way(ddt_data["派单方式"])
        # 选择结算方式
        self.create_group.select_settle_way(ddt_data["结算方式"])
        # 输入圈子公告
        self.create_group.input_group_notice(ddt_data["圈子公告"])
        self.base.sleep(1)
        # 点击确定创建
        self.create_group.click_confirm_create_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Create_Group)

    unittest.TextTestRunner().run(suits)
