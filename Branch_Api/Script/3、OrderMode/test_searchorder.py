# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/28 10:41

from Common.WriteResult import write_to_Config
from Common.Requests import Method
from Common.Page import Page
from Common.Public import data_dir
from Common import Logger
import unittest,logging,requests

'''
网点订单各种字段订单的搜索：1、订单状态的搜索 2、按订单单号搜索 3、全部订单搜索 3、待预约订单搜索 4、待服务订单搜索 5、服务中订单搜索 
                       6、待收款订单搜索 7、待结算订单搜索 8、已完成订单搜索 9、已取消订单搜索
'''

#默认写入测试结果
isWrite=True
class Search_Order(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Method()
        self.page = Page()
        #默认测试结果Fail
        self.isOk = "Fail"

    def test_search01(self):
        '''查询网点各种状态订单数量信息'''
        #指定日志路径信息
        Logger.setFormatter(logFile=data_dir(data="Log",filename="test_searchorder.txt"))
        r = self.obj.testApi(27)
        self.obj.isContent(r,27,isWrite)

    def test_search02(self):
        '''查询网点各种状态订单的数量信息'''
        r = self.obj.testApi(28)
        self.obj.isContent(r,28,isWrite)

    def test_search03(self):
        '''按订单号搜索订单信息'''
        #固定搜索订单号，每个订单号的sign不一样
        r = self.obj.testApi(29)
        self.obj.isContent(r,29,isWrite)

    def test_search04(self):
        '''获取网点下单的订单详情信息'''
        r = requests.get(url=self.page.canelOrder(row=30),
                         headers=self.obj.apiHeaders(30)
                         )
        self.obj.isContent(r,30,isWrite)

    def test_search05(self):
        '''获取网点订单为空时的展示图片'''
        r = self.obj.testApi(31)
        self.obj.isContent(r,31,isWrite)

    def test_search06(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(32)
        self.obj.isContent(r,32,isWrite)

    def test_search07(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(33)
        self.obj.isContent(r,33,isWrite)

    def test_search08(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(34)
        self.obj.isContent(r,34,isWrite)

    def test_search09(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(35)
        self.obj.isContent(r,35,isWrite)

    def test_search10(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(36)
        self.obj.isContent(r,36,isWrite)

    def test_search11(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(37)
        self.obj.isContent(r,37,isWrite)

    def test_search12(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(38)
        self.obj.isContent(r,38,isWrite)

    def test_search13(self):
        '''获取网点全部订单信息列表'''
        r = self.obj.testApi(39)
        self.obj.isContent(r,39,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        #测试结果pass
        self.isOk="Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_searchorder")

if __name__ == '__main__':
    unittest.main(verbosity=2)