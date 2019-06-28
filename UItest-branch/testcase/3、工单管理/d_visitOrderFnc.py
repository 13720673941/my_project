# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/10 15:44

from public.common import rwconfig,mytest
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest
'''
网点回访工单
'''
#获取网点回访订单参数信息
VisitData = getdata.get_test_data()["VisitOrderPage"]
ddtData = VisitData["visit_order_fnc"]
#默认写入测试结果
isWrite=True
class Visit_Order(unittest.TestCase):

    def setUp(self):
        #设置浏览器驱动
        self.dr = driver.browser_driver()
        #实例化
        self.basePage = BasePage(self.dr)
        self.pleaseOrderPage = PleaseOrderPage(self.dr)
        self.addOrderPage = AddOrderPage(self.dr)
        self.loginPage = LoginPage(self.dr)
        self.finishOrder = FinishOrder(self.dr)
        self.visitOrder = VisitOrderPage(self.dr)
        self.assert_mode = Assert(self.dr)
        #获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        #网点登录
        self.loginPage.login_main(UserName,PassWord)
        # #添加订单默认为需返单订单，便于测试
        # OrderData = getData.GetTestData()["CreateOrder"][-1]
        # #获取添加订单数据信息
        # self.OpenUrl = getData.GetTestData()["AddOrderUrl"]
        # self.Name = OrderData["username"]
        # self.PhoneNum = OrderData["PhoneNum"]
        # self.ServerAdd = OrderData["ServerAddress"]
        # self.Collage = OrderData["Collage"]
        # self.OrderType = OrderData["OrderType"]
        # self.BranchName = OrderData["Branch"]
        # self.ServerType = OrderData["ServerType"]
        # self.Brands = OrderData["Brands"]
        # self.Kinds = OrderData["Kinds"]
        # self.Expect = OrderData["expect"]
        # #添加订单
        # self.addOrderPage.AddOrderMain(self.OpenUrl,self.Name,self.PhoneNum,self.ServerAdd,self.Collage,self.OrderType,self.BranchName,
        #                               self.ServerType,self.Brands,self.Kinds,self.Expect)
        # #获取创建成功的订单单号
        # self.OrderNumber = self.basePage.GetNewOrderNum()
        # #获取派单数据
        # Master = getData.GetTestData()["PleaseOrder"]["ToMaster"][-1]["MasterName"]
        # #派单
        # self.pleaseOrderPage.PleaseOrderMain(self.OrderNumber,Master)
        # #完成服务
        # self.finishOrder.FinishOrderMain(FinishUrl,self.OrderNumber)
        #获取工单单号
        self.OrderNumber = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        #进入回访页面
        self.visitOrder.enter_visit_order_page()

    def test_visitOrder001(self):
        '''订单回访功能校验'''
        #用例名称
        self.basePage.print_case_name(ddtData["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        self.basePage.sleep(1)
        #选择完成的工单
        self.basePage.select_new_order(OrderNumber=self.OrderNumber)
        #点击回访
        self.visitOrder.click_visit_btn()
        #选择服务态度
        self.visitOrder.select_server_status(serverStatus=ddtData["ServerStatus"])
        #选择安全评价
        self.visitOrder.select_safety_assess(safetyAssess=ddtData["SafetyAssess"])
        #输入回访总额
        self.visitOrder.input_visit_money()
        #选择回访结果
        self.visitOrder.select_visit_result(visitResult=ddtData["visitResult"])
        #输入回访反馈
        self.visitOrder.input_visit_remark()
        #选择奖惩
        self.visitOrder.select_reward_punish()
        #输入奖惩金额
        self.visitOrder.input_reward_punish_money()
        #输入奖惩备注
        self.visitOrder.input_reward_punish_remark()
        #点击提交按钮
        self.visitOrder.click_confirm_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(ddtData["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'VisitOrder',ddtData["CaseName"])

    def tearDown(self):
        self.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Visit_Order('test_visitOrder001'))
    unittest.TextTestRunner().run(suit)