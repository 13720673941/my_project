#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/10 15:44

from public.common.rwconfig import read_config_data
from public.common import mytest
from public.common import driver,getdata
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.searchOrderPage import SearchOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest
"""
网点回访工单
"""
# 获取网点回访订单参数信息
VisitData = getdata.get_test_data()["VisitOrderPage"]
ddtData = VisitData["visit_order_fnc"]

class Visit_Order(unittest.TestCase):

    def setUp(self):
        # 设置浏览器驱动
        self.dr = driver.browser_driver()
        # 实例化
        self.basePage = BasePage(self.dr)
        self.pleaseOrderPage = PleaseOrderPage(self.dr)
        self.addOrderPage = AddOrderPage(self.dr)
        self.loginPage = LoginPage(self.dr)
        self.finishOrder = FinishOrder(self.dr)
        self.visitOrder = VisitOrderPage(self.dr)
        self.search_order = SearchOrderPage(self.dr)
        self.assert_mode = Assert(self.dr)
        # 获取网点登录数据
        UserName = read_config_data('蓝魔科技','username')
        PassWord = read_config_data('蓝魔科技','password')
        # 网点登录
        self.loginPage.login_main(UserName,PassWord)
        #  经销商下单程序下单
        self.addOrderPage.create_not_return_order()
        #  获取单号
        self.OrderNumber = self.basePage.get_order_number()
        # 获取派单数据
        Master = read_config_data('蓝魔科技','master001')
        # 派单
        self.pleaseOrderPage.please_order_main(self.OrderNumber,Master)
        # 完成服务
        self.finishOrder.finish_order_main(self.OrderNumber)
        # 进入回访页面
        self.visitOrder.enter_visit_order_page()

    def test_visitOrder001(self):
        """订单回访功能校验"""
        # 用例名称
        self.basePage.print_case_name(ddtData["CaseName"])
        # 刷新页面
        self.basePage.refresh_page()
        self.basePage.sleep(1)
        # 搜索订单
        # 输入工单编号
        self.search_order.input_order_Nnumber(orderNum=self.OrderNumber)
        # 点击搜索
        self.search_order.click_search_btn()
        # 选择完成的工单
        self.basePage.select_new_order(OrderNumber=self.OrderNumber)
        # 点击回访
        self.visitOrder.click_visit_btn()
        # 选择服务态度
        self.visitOrder.select_server_status(serverStatus=ddtData["ServerStatus"])
        # 选择安全评价
        self.visitOrder.select_safety_assess(safetyAssess=ddtData["SafetyAssess"])
        # 输入回访总额
        self.visitOrder.input_visit_money()
        # 选择回访结果
        self.visitOrder.select_visit_result(visitResult=ddtData["visitResult"])
        # 输入回访反馈
        self.visitOrder.input_visit_remark()
        # 选择奖惩
        self.visitOrder.select_reward_punish()
        # 输入奖惩金额
        self.visitOrder.input_reward_punish_money()
        # 输入奖惩备注
        self.visitOrder.input_reward_punish_remark()
        # 点击提交按钮
        self.visitOrder.click_confirm_btn()
        self.basePage.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddtData["expect"],self.basePage.get_system_msg())

    def tearDown(self):
        self.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Visit_Order('test_visitOrder001'))
    unittest.TextTestRunner().run(suit)