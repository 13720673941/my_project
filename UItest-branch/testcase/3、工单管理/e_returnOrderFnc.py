# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/12 16:31

from public.common import rwconfig,mytest
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.returnOrderPage import ReturnOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
'''
网点返单功能测试用例脚本：
1、返单-修改返单服务商为空校验 2、返单-修改返单服务商成功校验 
3、返单-返单成功校验 4、返单-撤销返单校验 5、添加代结单服务商校验
'''
#获取返单测试数据
ReturnData = getdata.get_test_data()["ReturnOrderPage"]
ddtData = ReturnData["alter_return_fnc"]
#默认写入测试结果
isWrite=True
@ddt.ddt
class Return_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化
        cls.basePage = BasePage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.returnOrder = ReturnOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        #获取订单单号数据
        cls.OrderNumber = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        #获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        #网点登录
        cls.loginPage.login_main(UserName,PassWord)

    def setUp(self):
        #进入待返单页面
        self.returnOrder.enter_return_order_page()

    @ddt.data(*ddtData)
    def test_returnOrder001(self,ddtData):
        '''修改返单服务商功能测试用例'''
        #刷新页面
        self.basePage.print_case_name(ddtData["CaseName"])
        self.basePage.refresh_page()
        #选择返单订单
        self.basePage.select_new_order(self.OrderNumber)
        #点击修改返单服务商
        self.returnOrder.click_alter_return_branch()
        #选择服务商
        self.returnOrder.select_branch_name(branchName=ddtData["BranchName"])
        #点击确定
        self.returnOrder.click_confirm_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(ddtData["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ReturnOrder',ddtData["CaseName"])

    def test_returnOrder002(self):
        '''网点成功返单校验'''
        #获取用例数据
        Data = ReturnData["return_order_fnc"]
        #刷新页面
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.refresh_page()
        #选择返单订单
        self.basePage.select_new_order(self.OrderNumber)
        #点击返单按钮
        self.returnOrder.click_return_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ReturnOrder',Data["CaseName"])

    def test_returnOrder003(self):
        '''返单页面点击添加代结单服务商校验'''
        #获取用例数据
        Data = ReturnData["add_branch_btn_fnc"]
        #刷新页面
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.refresh_page()
        #点击添加服务商
        self.returnOrder.click_add_branch()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_el_in_page(self.returnOrder.turn_title_isDisplayed())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ReturnOrder',Data["CaseName"])

    def test_returnOrder004(self):
        '''撤销返单校验'''
        #进入撤销返单页面
        self.returnOrder.enter_finish_return_page()
        #获取用例数据
        Data = ReturnData["del_return_fnc"]
        #刷新页面
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.refresh_page()
        #选择返单订单
        self.basePage.select_new_order(self.OrderNumber)
        #点击撤销返单按钮
        self.returnOrder.click_del_return()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'ReturnOrder',Data["CaseName"])

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Return_Order('test_returnOrder001'))
    suit.addTest(Return_Order('test_returnOrder002'))
    suit.addTest(Return_Order('test_returnOrder003'))
    suit.addTest(Return_Order('test_returnOrder004'))
    unittest.TextTestRunner().run(suit)
