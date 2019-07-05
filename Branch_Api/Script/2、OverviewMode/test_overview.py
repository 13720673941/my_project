# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

from Common import Logger
from Common import Public
import unittest
from Common.Requests import Method
from Common import WriteResult

'''
网点首页模块的api
1、获取主页菜单信息 2、获取后台设置的主页所有按钮信息 3、获取全部的省市区 4、获取网点公司信息
5、获取网点授权服务商信息 6、获取网点左侧菜单栏信息 7、获取网点首页收入、待结算、已结算金额信息
8、查询网点上月账单信息 9、获取网点用户评价数据分析 10、获取网点系统消息 11、获取网点服务信息
12、获取网点IM消息 13、获取网点讨论组订单信息
'''
#默认写入测试结果
isWrite=True
class OverviewMode(unittest.TestCase):

    def setUp(self):
        '''实例化method模块'''
        self.obj = Method()
        self.isOk = "Fail"

    def test_overview01(self):
        '''获取主页所有菜单信息'''
        #设置日志路径
        Logger.setFormatter(logFile=Public.data_dir(data="Log", filename="test_overview.txt"))

        r = self.obj.testApi(6)
        self.obj.isContent(r,6,isWrite)

    def test_overview02(self):
        '''获取后台概览页按钮'''
        r = self.obj.testApi(7)
        self.obj.isContent(r,7,isWrite)

    def test_overview03(self):
        '''CDN获取省市区'''
        r = self.obj.testApi(8)
        self.obj.isContent(r,8,isWrite)

    def test_overview04(self):
        '''获取网点公司信息'''
        r = self.obj.testApi(9)
        self.obj.isContent(r,9,isWrite)

    def test_overview05(self):
        '''获取网点授权服务商信息'''
        r = self.obj.testApi(10)
        self.obj.isContent(r,10,isWrite)

    def test_overview06(self):
        '''获取网点左侧菜单信息'''
        r = self.obj.testApi(11)
        self.obj.isContent(r,11,isWrite)

    def test_overview07(self):
        '''获取网点首页收入信息'''
        r = self.obj.testApi(12)
        self.obj.isContent(r,12,isWrite)

    def test_overview08(self):
        '''查询网点上月账单信息'''
        r = self.obj.testApi(13)
        self.obj.isContent(r,13,isWrite)

    def test_overview09(self):
        '''获取首页网点用户评价数据信息'''
        r = self.obj.testApi(14)
        self.obj.isContent(r,14,isWrite)

    def test_overview10(self):
        '''获取网点系统消息'''
        r = self.obj.testApi(15)
        self.obj.isContent(r,15,isWrite)

    def test_overview11(self):
        '''获取网点服务信息'''
        r = self.obj.testApi(16)
        self.obj.isContent(r,16,isWrite)

    def test_overview12(self):
        '''获取网点IM信息'''
        r = self.obj.testApi(17)
        self.obj.isContent(r,17,isWrite)

    def test_overview13(self):
        '''获取网点讨论组订单信息'''
        r = self.obj.testApi(18)
        self.obj.isContent(r,18,isWrite)
    def test_overview14(self):
        '''获取网点首页备件信息'''
        r = self.obj.testApi(19)
        self.obj.isContent(r,19,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk = "Pass"
        WriteResult.write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_overview")

if __name__ == '__main__':
    unittest.main(verbosity=2)
