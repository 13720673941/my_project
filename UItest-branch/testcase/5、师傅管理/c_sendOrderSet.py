# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/20 11:57

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.masterListPage import MasterListPage
from public.common.operateExcel import *
import unittest

class Send_Order_Set(unittest.TestCase):

    """ 【合作师傅派单设置功能】 """

    # 实例化
    readExcel = Read_Excel("masterSendOrderSet")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.master_page = MasterListPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"masterSendOrderSet")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()

    def public_operate(self,searchWord):
        """进入师傅列表页->搜索师傅"""

        self.master_page.enter_master_list_page()
        self.base.refresh_page()
        self.master_page.input_keyword_for_search(searchWord)
        self.master_page.click_search_btn()
        self.base.sleep(1)

    def send_order_to_master(self,masterName):
        """进入派单页面->选择订单->搜索派单师傅"""

        # 进入派单列表
        self.send_order.enter_send_order_page()
        self.base.refresh_page()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        self.base.sleep(1)
        # 搜索派单师傅
        self.send_order.input_search_name(masterName)
        # 点击搜索
        self.send_order.click_search_btn()

    @unittest.skipUnless(readExcel.get_isRun_text("send_order_set_001"),"-跳过不执行")
    def test_master_send_set001(self):
        """师傅禁止派单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_set_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 搜索禁止派单的师傅
        self.public_operate(searchWord=data["师傅名称"])
        # 点击禁止派单
        self.master_page.click_stop_send_order()
        # 进入派单师傅列表搜索师傅
        self.send_order_to_master(masterName=data["师傅名称"])
        # 等待页面加载
        self.base.sleep(1)
        # 断言 判断师傅不存在页面
        self.assert_mode.assert_el_not_in_page(data,self.send_order.search_branch_is_display())

    @unittest.skipUnless(readExcel.get_isRun_text("send_order_set_002"),"-跳过不执行")
    def test_master_send_set002(self):
        """师傅恢复派单功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_set_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 搜索恢复派单的师傅
        self.public_operate(searchWord=data["师傅名称"])
        # 点击恢复派单
        self.master_page.click_open_send_order()
        # 进入派单师傅列表
        self.send_order_to_master(masterName=data["师傅名称"])
        # 等待页面加载
        self.base.sleep(1)
        # 断言 判断师傅存在页面
        self.assert_mode.assert_el_in_page(data,self.send_order.search_branch_is_display())

    @unittest.skipUnless(readExcel.get_isRun_text("send_order_set_003"),"-跳过不执行")
    def test_master_send_set003(self):
        """师傅撤销邀请功能校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_set_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 搜索师傅
        self.public_operate(searchWord=data["师傅名称"])
        # 点击撤销按钮
        self.master_page.click_del_visit_master()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Send_Order_Set)
    unittest.TextTestRunner().run(suits)