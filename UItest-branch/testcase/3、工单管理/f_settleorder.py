# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/10 18:14

from public.common import rwconfig,mytest
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.loginpage import LoginPage
from public.page.pleaseorderpage import PleaseOrderPage
from public.page.finishorderpage import FinishOrder
from public.page.returnpage import ReturnOrderPage
from public.page.settlepage import SettleOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
'''
网点返单结算测试用例：
1、返单结算-厂商结算价格不能编辑校验 2、返单结算-厂商未结算提示信息校验 3、返单结算-按规则结算结算价格不能编辑校验
4、返单结算-按固定金额结算金可以编辑校验 5、返单结算-钱包余额不足支付校验 6、返单结算-线下成功支付校验 7、返单结算-返单未结算系统提示校验
8、返单结算-返单未结算只能选择固定金额校验 9、返单结算-返单结算后系统提示校验 10、返单结算-返单结算123结算方式都能选择校验
11、返单结算-固定金额线下结算成功校验
'''
#获取数据
SettleData = getdata.get_test_data()["SettleReturnPage"]
ReturnOrderData = SettleData["return_settle_fnc"]
#获取005的测试数据
pay_fnc = ReturnOrderData["pay_fnc"]
#默认写入测试结果
isWrite = True
@ddt.ddt
class Settle_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化
        cls.base = BasePage(cls.dr)
        cls.login = LoginPage(cls.dr)
        cls.pleaseOrder = PleaseOrderPage(cls.dr)
        cls.finishOrder = FinishOrder(cls.dr)
        cls.returnOrder = ReturnOrderPage(cls.dr)
        cls.settleOrder = SettleOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        #获取定单订单号
        cls.OrderNumber = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        #登录网点 蓝魔科技
        cls.Use = rwconfig.read_config_data('蓝魔科技',"username")
        cls.Pwd = rwconfig.read_config_data('蓝魔科技',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        #进入订单列表页面
        cls.pleaseOrder.enter_please_order_page()
        cls.base.sleep(1)

    def setUp(self):
        #刷新页面时间加载
        self.base.refresh_page()

    def test_settleOrder001(self):
        '''返单未结算系统提示校验'''
        #获取数据
        Data001 = SettleData["return_not_settle_fnc"]["TestCase001"]
        #用例名称
        self.base.print_case_name(Data001["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        self.base.sleep(2)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data001["expect"],self.settleOrder.get_settle_money_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data001["CaseName"])

    def test_settleOrder002(self):
        '''返单未结算只能选择固定金额校验'''
        #获取数据
        Data002 = SettleData["return_not_settle_fnc"]["TestCase002"]
        #用例名称
        self.base.print_case_name(Data002["CaseName"])
        self.base.sleep(1)
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #获取1、3结算方式的选择属性：不能选择
        Att1 = self.settleOrder.get_settleType1_att()
        Att3 = self.settleOrder.get_settleType3_att()
        #断言 判断两个选择的按钮的属性 不能选择 None
        isSuccess1 = self.assert_mode.assert_att_is_none(Att1)
        isSuccess2 = self.assert_mode.assert_att_is_none(Att3)
        if isSuccess1 and isSuccess2 == 'PASS':
            isSuccess = 'PASS'
        else:
            isSuccess = 'FAIL'
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data002["CaseName"])

    def test_settleOrder003(self):
        '''厂商结算价格不能编辑校验'''
        #返单
        self.base.sleep(2)
        self.returnOrder.return_order_main(self.OrderNumber)
        #退出登录
        self.login.click_logout_button()
        #获取返单网点-- 在最后有修改返单服务商，该网点为最后返单的服务商
        ReturnBranch = getdata.get_test_data()["ReturnOrderPage"]["alter_return_fnc"][-1]["BranchName"]
        #获取返单网点账户
        returnUse = rwconfig.read_config_data(ReturnBranch,"username")
        returnPwd = rwconfig.read_config_data(ReturnBranch,"password")
        #登录返单网点账号
        self.login.login_main(returnUse,returnPwd)
        #进入订单结算列表页面
        self.settleOrder.enter_return_wait_settle()
        #点击订单进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        self.base.sleep(1)
        #点击返单结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #获取001的测试数据
        Data007 = ReturnOrderData["TestCase001"]
        #用力名称
        self.base.print_case_name(Data007["CaseName"])
        #获取厂商结算输入框属性断言
        isSuccess = self.assert_mode.assert_equal(Data007["expect"],self.settleOrder.settle_money_attribute())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data007["CaseName"])

    def test_settleOrder004(self):
        '''厂商未结算提示信息校验'''
        #获取002的测试数据
        Data006 = ReturnOrderData["TestCase002"]
        #用力名称
        self.base.print_case_name(Data006["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        #点击返单结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #断言获取字段校验
        isSuccess = self.assert_mode.assert_equal(Data006["expect"],self.settleOrder.get_settle_money_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data006["CaseName"])

    def test_settleOrder005(self):
        '''按规则结算结算价格不能编辑校验'''
        #获取003的测试数据
        Data007 = ReturnOrderData["TestCase003"]
        #用力名称
        self.base.print_case_name(Data007["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        #点击返单结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #默认按照规则结算不用选择
        #获取结算金额输入属性断言
        isSuccess = self.assert_mode.assert_equal(Data007["expect"],self.settleOrder.settle_money_att())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data007["CaseName"])

    def test_settleOrder006(self):
        '''按固定金额结算金可以编辑校验'''
        #获取004的测试数据
        Data006 = ReturnOrderData["TestCase004"]
        #用力名称
        self.base.print_case_name(Data006["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        #点击返单结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #选择按结算规则结算
        self.settleOrder.select_settle_type(settleType=Data006["SettleType"])
        #输入结算价格
        self.settleOrder.input_settle_money(settleMoney=Data006["SettleMoney"])
        #获取结算金额属性断言
        isSuccess = self.assert_mode.assert_att_is_none(self.settleOrder.settle_money_att()) #返回的是None 不是字符串 是个函数
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data006["CaseName"])

    @ddt.data(*pay_fnc)
    def test_settleOrder007(self,pay_fnc):
        '''钱包余额不足支付校验'''
        #用力名称
        self.base.print_case_name(pay_fnc["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        #点击返单结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #选择按结算规则结算
        self.settleOrder.select_settle_type(settleType=pay_fnc["SettleType"])
        #输入结算价格
        self.settleOrder.input_settle_money(settleMoney=pay_fnc["SettleMoney"])
        #选择线上支付
        self.settleOrder.select_pay_type(payType=pay_fnc["PayType"])
        #点击确定
        self.settleOrder.click_confirm_btn()
        #获取结算金额断言
        isSuccess = self.assert_mode.assert_equal(pay_fnc["expect"],self.base.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',pay_fnc["CaseName"])

    def test_settleOrder008(self):
        '''返单结算后经销商提示信息校验'''
        #退出登录
        self.login.click_logout_button()
        #登录蓝魔账号
        self.login.login_main(self.Use,self.Pwd)
        ##获取数据
        Data008 = SettleData["return_settle_fnc"]["TestCase006"]
        #用例名称
        self.base.print_case_name(Data008["CaseName"])
        #进入订单列表页面
        self.pleaseOrder.enter_please_order_page()
        self.base.sleep(1)
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #断言 判断页面元素是否存在
        isSuccess = self.assert_mode.assert_el_not_in_page(self.settleOrder.settle_msg_isDisplayed())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data008["CaseName"])

    def test_settleOrder009(self):
        '''返单结算123结算方式都能选择校验'''
        #获取数据
        Data009 = SettleData["return_settle_fnc"]["TestCase007"]
        #用例名称
        self.base.print_case_name(Data009["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #获取1、3结算方式的选择属性：不能选择
        Att1 = self.settleOrder.get_settleType1_att()
        Att3 = self.settleOrder.get_settleType3_att()
        #断言 判断两个选择的按钮的属性 不能选择 true
        isSuccess1 = self.assert_mode.assert_att_is_none(Att1)
        isSuccess2 = self.assert_mode.assert_att_is_none(Att3)
        #并列断言
        if isSuccess1 and isSuccess2 == 'PASS':
            isSuccess = 'PASS'
        else:
            isSuccess = 'FAIL'
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data009["CaseName"])

    def test_settleOrder010(self):
        '''提成规则线下结算成功校验'''
        #获取数据
        Data010 = SettleData["return_settle_fnc"]["TestCase008"]
        #用例名称
        self.base.print_case_name(Data010["CaseName"])
        #进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #选择规则结算方式
        self.settleOrder.select_settle_type(settleType=Data010["SettleType"])
        #选择付款类型
        self.settleOrder.select_pay_type(payType=Data010["PayType"])
        #点击确定
        self.settleOrder.click_confirm_btn()
        self.base.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data010["expect"],self.base.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data010["CaseName"])

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.base.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()