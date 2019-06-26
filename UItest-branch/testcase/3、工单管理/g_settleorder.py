# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/15 10:42

from public.common import mytest,rwconfig
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.loginpage import LoginPage
from public.page.pleaseorderpage import PleaseOrderPage
from public.page.finishorderpage import FinishOrder
from public.page.settlepage import SettleOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
'''
经销商工单结算测试用例：
1、经销商工单结算-未结算提示信息校验 2、经销商工单结算-1/3结算方式可以选择校验 3、经销商工单结算-设置结算价格不能修改校验
4、经销商工单结算-钱包结算余额不足校验 5、经销商工单结算-线下结算成功校验 6、经销商工单结算-结算后提示信息校验
7、经销商工单结算-钱包结算余额不足校验 8、经销商工单结算-线下结算成功校验
'''
#获取数据
SettleData = getdata.get_test_data()["SettleManagePage"]
ddtData1 = SettleData["TestCase004"]
ddtData2 = SettleData["TestCase006"]
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
        cls.settleOrder = SettleOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        #获取定单订单号
        cls.OrderNum = rwconfig.read_config_data('NotReturnOrder','id',orderNumPath)
        #登录网点 蓝魔科技
        cls.Use = rwconfig.read_config_data('蓝魔科技',"username")
        cls.Pwd = rwconfig.read_config_data('蓝魔科技',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        #获取派单到服务商数据 关联派单数据中的信息
        BranchName = rwconfig.read_config_data('蓝魔科技','branch002')
        #派单到服务商
        cls.pleaseOrder.please_order_main(cls.OrderNum,BranchName,please_to_branch=True)
        #退出登录
        cls.login.click_logout_button()
        #获取服务商账号密码
        cls.Use1 = rwconfig.read_config_data(BranchName,'username')
        cls.Pwd1 = rwconfig.read_config_data(BranchName,'password')
        #登录派单服务商
        cls.login.login_main(cls.Use1,cls.Pwd1)
        #获取派单师傅
        MasterName = rwconfig.read_config_data(BranchName,'master001')
        #服务商派单到师傅
        cls.pleaseOrder.please_order_main(cls.OrderNum,MasterName)
        #网点完成服务
        cls.finishOrder.finish_order_main(cls.OrderNum)
        #进入全部订单列表页
        cls.pleaseOrder.enter_please_order_page()

    def setUp(self):
        #刷新页面时间加载
        self.base.refresh_page()

    def test_settleOrder001(self):
        '''经销商工单结算-未结算提示信息校验'''
        #获取001测试数据
        Data001 = SettleData["TestCase001"]
        #测试用例名称
        self.base.print_case_name(Data001["CaseName"])
        self.base.sleep(1)
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        #断言
        isSuccess = self.assert_mode.assert_equal(Data001["expect"],self.settleOrder.get_settle_money_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data001["CaseName"])

    def test_settleOrder002(self):
        '''经销商工单结算-1/3结算方式可以选择校验'''
        #获取002测试数据
        Data002 = SettleData["TestCase002"]
        #测试用例名称
        self.base.print_case_name(Data002["CaseName"])
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        #获取1、3结算方式的选择属性：不能选择
        Att1 = self.settleOrder.get_settleType1_att()
        Att3 = self.settleOrder.get_settleType3_att()
        #断言 判断两个选择的按钮的属性 不能选择 true
        isSuccess1 = self.assert_mode.assert_att_is_none(Att1)
        isSuccess2 = self.assert_mode.assert_att_is_none(Att3)
        if isSuccess1 and isSuccess2 == 'PASS':
            isSuccess = 'PASS'
        else:
            isSuccess = 'FAIL'
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data002["CaseName"])

    def test_settleOrder003(self):
        '''经销商工单结算-经商端设置结算价格不能修改校验验'''
        #获取003测试数据
        Data003 = SettleData["TestCase003"]
        #测试用例名称
        self.base.print_case_name(Data003["CaseName"])
        #退出服务商
        self.login.click_logout_button()
        #登录经销商
        self.login.login_main(self.Use,self.Pwd)
        #进入全部订单列表页
        self.pleaseOrder.enter_please_order_page()
        self.base.sleep(1)
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        #获取元素属性
        att = self.settleOrder.brands_settle_money_attribute()
        #获取结算输入框属性断言
        isSuccess = self.assert_mode.assert_equal(Data003["expect"],att)
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data003["CaseName"])

    @ddt.data(*ddtData1)
    def test_settleOrder004(self,ddtData1):
        '''经销商工单结算-经销商端订单结算校验'''
        #测试用例名称
        self.base.print_case_name(ddtData1["CaseName"])
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        self.base.sleep(1)
        #点击结算
        self.settleOrder.click_settle_btn()
        #选择支付方式
        self.settleOrder.select_pay_type(payType=ddtData1["PayType"])
        #点击确定
        self.settleOrder.click_confirm_btn()
        #断言
        isSuccess = self.assert_mode.assert_equal(ddtData1["expect"],self.base.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',ddtData1["CaseName"])

    def test_settleOrder005(self):
        '''经销商工单结算-结算后提示信息校验'''
        #获取005测试数据
        Data005 = SettleData["TestCase005"]
        #测试用例名称
        self.base.print_case_name(Data005["CaseName"])
        #退出经销商账号
        self.login.click_logout_button()
        #登录服务商账号
        self.login.login_main(self.Use1,self.Pwd1)
        #进入全部订单列表页
        self.base.open_url(getdata.get_test_data()["PleaseOrder"]["PleaseUrl"])
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        #点击结算
        self.settleOrder.click_settle_btn()
        #断言 判断页面元素是否存在
        isSuccess = self.assert_mode.assert_el_not_in_page(self.settleOrder.settle_msg_isDisplayed())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',Data005["CaseName"])

    @ddt.data(*ddtData2)
    def test_settleOrder006(self,ddtData2):
        '''经销商工单结算-服务商端订单结算校验'''
        #测试用例名称
        self.base.print_case_name(ddtData2["CaseName"])
        #进入订单详情页面
        self.base.open_order_message(self.OrderNum)
        #点击结算
        self.settleOrder.click_settle_btn()
        #选择结算方式
        self.settleOrder.select_settle_type(settleType=ddtData2["SettleType"])
        #选择结算比例
        self.settleOrder.select_settle_proportion(arriveTxt=ddtData2["BranchNum"])
        #选择支付方式
        self.settleOrder.select_pay_type(payType=ddtData2["PayType"])
        #点击确定
        self.settleOrder.click_confirm_btn()
        self.base.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(ddtData2["expect"],self.base.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'SettleOrder',ddtData2["CaseName"])

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.base.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()


