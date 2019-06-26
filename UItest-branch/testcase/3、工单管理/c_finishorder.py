# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/5 18:07

from public.common import rwconfig,mytest
from public.common import driver,getdata,writetestresult
from public.common.basepage import BasePage
from public.page.loginpage import LoginPage
from public.page.addorderpage import AddOrderPage
from public.page.pleaseorderpage import PleaseOrderPage
from public.page.finishorderpage import FinishOrder
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
'''
网点完成服务页面功能测试用例：
1、完成工单-师傅预约时间为空校验 2、完成工单-师傅上门时间为空校验 3、完成工单-师傅完工时间为空校验 4、完成工单-师傅上传图片为空校验
5、完成工单-网点完成服务校验
'''
#写入日志
#获取测试数据信息
Data = getdata.get_test_data()["FinishOrder"]
FinishDate = Data["FinishData"]
#写入测试结果
isWrite=True
@ddt.ddt
class Finish_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化
        cls.basePage = BasePage(cls.dr)
        cls.pleaseOrderPage = PleaseOrderPage(cls.dr)
        cls.addOrderPage = AddOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.finishOrder = FinishOrder(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        #获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        cls.loginPage.login_main(UserName,PassWord)
        # #添加订单默认为需返单订单，便于测试
        # OrderData = getData.GetTestData()["CreateOrder"][-1]
        # #获取添加订单数据信息
        # cls.OpenUrl = getData.GetTestData()["AddOrderUrl"]
        # cls.Name = OrderData["username"]
        # cls.PhoneNum = OrderData["PhoneNum"]
        # cls.ServerAdd = OrderData["ServerAddress"]
        # cls.Collage = OrderData["Collage"]
        # cls.OrderType = OrderData["OrderType"]
        # cls.BranchName = OrderData["Branch"]
        # cls.ServerType = OrderData["ServerType"]
        # cls.Brands = OrderData["Brands"]
        # cls.Kinds = OrderData["Kinds"]
        # cls.Expect = OrderData["expect"]
        # #添加订单
        # cls.addOrderPage.AddOrderMain(cls.OpenUrl,cls.Name,cls.PhoneNum,cls.ServerAdd,cls.Collage,cls.OrderType,cls.BranchName,
        #                               cls.ServerType,cls.Brands,cls.Kinds,cls.Expect)
        #获取创建成功的订单单号
        cls.OrderNumber = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        # #获取派单数据
        # Master = getData.GetTestData()["PleaseOrder"]["ToMaster"][-1]["MasterName"]
        # #进入派单页面
        # cls.basePage.OpenUrl(getData.GetTestData()["PleaseOrder"]["PleaseUrl"])
        # #派单
        # cls.pleaseOrderPage.PleaseOrderMain(cls.OrderNumber,Master)
        #进入服务中全部工单列表页面
        cls.finishOrder.enter_finish_order_page()

    @ddt.data(*FinishDate)
    def test_finishOrder001(self,FinishDate):
        '''网点完成工单功能校验'''
        #设置参数信息
        for key,value in FinishDate.items():
            if value == '当前时间':
                FinishDate[key] = self.basePage.get_now_time()
        #用例名称
        self.basePage.print_case_name(FinishDate["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        self.basePage.sleep(1)
        #选择完成的工单
        self.basePage.select_new_order(OrderNumber=self.OrderNumber)
        #点击完成工单按钮
        self.finishOrder.click_finish_btn()
        #输入故障类型
        self.finishOrder.input_break_type()
        #输入师傅预约时间
        self.finishOrder.input_master_orderTime(orderTime=FinishDate["OrderTime"])
        #输入师傅上门时间
        self.finishOrder.input_master_doorTime(doorTime=FinishDate["DoorTime"])
        #输入师傅完成服务时间
        self.finishOrder.input_master_finishTime(finishTime=FinishDate["FinishTime"])
        self.basePage.sleep(1)
        #上传图片
        self.finishOrder.up_finish_picture(upLoading=FinishDate["UpLoading"])
        #点击提交信息
        self.finishOrder.click_submit_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(FinishDate["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'FinishOrder',FinishDate["CaseName"])

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Finish_Order('test_finishOrder001'))
    unittest.TextTestRunner().run(suit)