# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/29 15:29

from Common import Requests
from Common.Public import data_dir
from Common import Logger
from Common.Page import Page
import unittest,logging
from Common.WriteResult import write_to_Config

'''
网点订单模块整机退换：1、手动添加整机退换订单 2、获取网点各种状态的整机退换数量 3、获取待网点提交订单信息
                  4、获取待品牌商审核订单信息 5、获取待网点出库订单信息 6、获取待品牌商入库订单信息
                  7、获取待品牌商出库订单信息 8、获取待网点入库订单信息 9、获取网点已完成整机退换订单
                  10、获取网点已拒绝状态整机退换订单信息
'''
#默认写入测试结果信息
isWrite=True
class THOrder(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Requests.Method()
        self.page = Page()
        self.isOk="Fail"

    def test_TH01(self):
        '''网点添加整机退换订单'''
        # 配置日志路径信息
        Logger.setFormatter(logFile=data_dir(data="Log", filename="test_THorder.txt"))
        r = self.obj.testApi(66)
        self.obj.isContent(r,66,isWrite)

    def test_TH02(self):
        '''获取网点整机退换所有状态的订单数量信息'''
        r = self.obj.testApi(67)
        self.obj.isContent(r,67,isWrite)

    def test_TH03(self):
        '''获取网点整机退换待网点提交订单信息'''
        r = self.obj.test_Api(68,data=self.page.JDorder(row=68,keyword="待网点提交"))
        self.obj.isContent(r,68,isWrite)

    def test_TH04(self):
        '''获取网点整机退换待品牌商审核订单信息'''
        r = self.obj.test_Api(69,data=self.page.JDorder(row=69,keyword="待品牌商审核"))
        self.obj.isContent(r,69,isWrite)

    def test_TH05(self):
        '''获取网点整机退换待网点出库订单信息'''
        r = self.obj.test_Api(70,data=self.page.JDorder(row=70,keyword="待网点出库"))
        self.obj.isContent(r,70,isWrite)

    def test_TH06(self):
        '''获取网点整机退换待品牌商入库订单信息'''
        r = self.obj.test_Api(71,data=self.page.JDorder(row=71,keyword="待品牌商入库"))
        self.obj.isContent(r,71,isWrite)

    def test_TH07(self):
        '''获取网点整机退换待品牌商出库订单信息'''
        r = self.obj.test_Api(72,data=self.page.JDorder(row=72,keyword="待品牌商出库"))
        self.obj.isContent(r,72,isWrite)

    def test_TH08(self):
        '''获取网点整机退换待网点入库订单信息'''
        r = self.obj.test_Api(73,data=self.page.JDorder(row=73,keyword="待网点入库"))
        self.obj.isContent(r,73,isWrite)

    def test_TH09(self):
        '''获取网点整机退换已完成订单信息'''
        r = self.obj.test_Api(74,data=self.page.JDorder(row=74,keyword="已完成"))
        self.obj.isContent(r,74,isWrite)

    def test_TH10(self):
        '''获取网点整机退换已拒绝订单信息'''
        r = self.obj.test_Api(75,data=self.page.JDorder(row=75,keyword="已拒绝"))
        self.obj.isContent(r,75,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk="Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_THorder")

if __name__ == '__main__':
    unittest.main(verbosity=2)