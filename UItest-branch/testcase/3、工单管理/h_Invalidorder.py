# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/4 10:29

from public.common import rwconfig,mytest
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.pleaseorderpage import PleaseOrderPage
from public.page.addorderpage import AddOrderPage
from public.page.loginpage import LoginPage
from public.page.invalidpage import InvalidOrder
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,logging,ddt
'''
网点设置无效工单测试用例脚本：
1、无效工单类型为空校验 2、设置无效工单校验校验 3、服务商待派不能设置无效校验 4、已结算订单不能设置无效校验
'''
#获取无效工单测试数据
Data = getdata.get_test_data()["InvalidOrderPage"]
ddtData = Data["set_invalid_fnc"]
#默认写入测试结果
isWrite=True
@ddt.ddt
class Set_InvalidOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化
        cls.basePage = BasePage(cls.dr)
        cls.pleaseOrderPage = PleaseOrderPage(cls.dr)
        cls.addOrderPage = AddOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.setInvalid = InvalidOrder(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        #获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        #网点登录
        cls.loginPage.login_main(UserName,PassWord)
        #添加订单默认为需返单订单，便于测试
        OrderData = getdata.get_test_data()["CreateOrderPage"]["create_order_fnc"][-1]
        #获取添加订单数据信息
        cls.Name = OrderData["username"]
        cls.PhoneNum = OrderData["PhoneNum"]
        cls.ServerAdd = OrderData["ServerAddress"]
        cls.Collage = OrderData["Collage"]
        cls.OrderType = OrderData["OrderType"]
        cls.BranchName = OrderData["Branch"]
        cls.ServerType = OrderData["ServerType"]
        cls.Brands = OrderData["Brands"]
        cls.Kinds = OrderData["Kinds"]
        cls.Expect = OrderData["expect"]
        #添加订单
        cls.addOrderPage.create_order_main(cls.Name,cls.PhoneNum,cls.ServerAdd,cls.Collage,cls.OrderType,cls.BranchName,
                                           cls.ServerType,cls.Brands,cls.Kinds)
        #获取创建成功的订单单号
        cls.OrderNumber = cls.basePage.get_order_number()

    @ddt.data(*ddtData)
    def test_setInvalid001(self,ddtData):
        '''网点设置无效工单测试用例'''
        #打印测试用力名称
        self.basePage.print_case_name(ddtData["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #选择新建工单
        self.basePage.select_new_order(OrderNumber=self.OrderNumber)
        #点击无效工单
        self.setInvalid.click_invalid_btn()
        #选择无效工单类型
        self.setInvalid.select_invalid_type(invalidType=ddtData["InvalidType"])
        #输入无效工单原因
        self.setInvalid.input_invalid_reason()
        #点击确定
        self.setInvalid.click_confirm_btn()
        #断言
        isSuccess = self.assert_mode.assert_equal(ddtData["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SetInvalidOrder',ddtData["CaseName"])

    def test_setInvalid002(self):
        '''待服务商派单订单不能设置无效工单校验'''
        #获取派单数据
        BranchName = rwconfig.read_config_data('蓝魔科技','branch002')
        InvalidData = Data["TestCase001"]
        self.basePage.print_case_name(InvalidData["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #选择派单服务商
        self.pleaseOrderPage.please_order_main(self.OrderNumber,BranchName,please_to_branch=True)
        self.basePage.refresh_page()
        #选择新建订单
        self.basePage.select_new_order(self.OrderNumber)
        #点击无效工单
        self.setInvalid.click_invalid_btn()
        #断言
        isSuccess = self.assert_mode.assert_equal(InvalidData["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SetInvalidOrder',InvalidData["CaseName"])

    def test_setInvalid003(self):
        '''已结算的订单设置无效工单校验'''
        #获取数据
        InvalidData = Data["TestCase002"]
        self.basePage.print_case_name(InvalidData["CaseName"])
        #获取已结算订单单号
        OrderNum = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        #刷新页面
        self.basePage.refresh_page()
        #选择结算订单
        self.basePage.select_new_order(OrderNum)
        #点击无效工单
        self.setInvalid.click_invalid_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(InvalidData["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SetInvalidOrder',InvalidData["CaseName"])

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Set_InvalidOrder('test_setInvalid001'))
    suit.addTest(Set_InvalidOrder('test_setInvalid002'))
    suit.addTest(Set_InvalidOrder('test_setInvalid003'))
    unittest.TextTestRunner(verbosity=2).run(suit)