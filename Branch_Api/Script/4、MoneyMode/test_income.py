# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/30 9:25

from Common import Page
from Common.Public import data_dir
from Common.Requests import Method
from Common.WriteResult import write_to_Config
from Common import Logger
import unittest,logging

'''
网点财务模块网点收入：1、授权品牌上个月账单信息 2、用户付款上个月账单信息 3、市场订单上个月账单信息
                  4、服务订单上个月账单信息 5、网点11月份账单信息
'''

#默认写入测试结果
isWrite=True
class BranchIncome(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Method()
        self.page = Page.Page()
        self.isOk = "Fail"

    def test_income01(self):
        '''获取网点授权品牌商默认月份账单信息'''
        #设置日志输出信息路径
        Logger.setFormatter(logFile=data_dir(data="Log",filename="test_income.txt"))
        r = self.obj.test_Api(76,data=self.page.branchIncome(row=76,billData="2018-12-01"))
        self.obj.isContent(r,76,isWrite)

    def test_income02(self):
        '''获取网点用户付款默认月份账单信息'''
        r = self.obj.test_Api(77,data=self.page.searchIncome(77,queryId="41",billData="2018-01-01",
                                                             startData="2018-12-01",endData="2019-02-01"))
        self.obj.isContent(r,77,isWrite)

    def test_income03(self):
        '''获取网点市场订单默认月份账单信息'''
        r = self.obj.test_Api(78,data=self.page.searchIncome(78,queryId="42",billData="2018-12-01",
                                                             startData="2018-12-01",endData="2019-01-01"))
        self.obj.isContent(r,78,isWrite)

    def test_income04(self):
        '''获取网点服务订单默认月份账单信息'''
        r = self.obj.test_Api(79,data=self.page.searchIncome(79,queryId="87",billData="2018-12-01",
                                                             startData="2018-12-01",endData="2019-01-01"))
        self.obj.isContent(r,79,isWrite)

    def test_iscome05(self):
        '''查询网点某个月品牌商账单信息'''
        r = self.obj.test_Api(80,data=self.page.branchIncome(row=80,billData="2018-11-01"))
        self.obj.isContent(r,80,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk="Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_income")


if __name__ == '__main__':
    unittest.main(verbosity=2)