# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/29 12:03

from Common import Requests
from Common.Public import data_dir
from Common.WriteResult import write_to_Config
from Common import Logger
from Common.Page import Page
import unittest,logging

'''
网点订单模块鉴定订单：1、网点提交鉴定订单 2、待鉴定单查询 3、已鉴定单查询
'''
#默认写入测试结果信息
isWrite=True
class JDOrder(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Requests.Method()
        self.page = Page()
        self.isOk = "Fail"

    def test_JD01(self):
        '''网点添加鉴定订单'''
        Logger.setFormatter(logFile=data_dir(data="Log", filename="test_JDorder.txt"))
        r = self.obj.testApi(62)
        self.obj.isContent(r,62,isWrite)

    def test_JD02(self):
        '''获取网点待鉴定和已鉴定单数'''
        r = self.obj.testApi(63)
        self.obj.isContent(r,63,isWrite)

    def test_JD03(self):
        '''获取网点待鉴定订单信息'''
        r = self.obj.test_Api(64,data=self.page.JDorder(row=64,keyword="待鉴定"))
        self.obj.isContent(r,64,isWrite)

    def test_JD04(self):
        '''获取网点已鉴定订单信息'''
        r = self.obj.test_Api(65,data=self.page.JDorder(row=65,keyword="已鉴定"))
        self.obj.isContent(r,65,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk = "Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_JDorder")



if __name__ == '__main__':
    unittest.main(verbosity=2)