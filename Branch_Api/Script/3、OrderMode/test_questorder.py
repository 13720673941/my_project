# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/28 17:30

from Common.WriteResult import write_to_Config
from Common.Requests import Method
from Common.Page import Page
from Common.Public import data_dir
import unittest,logging,requests
from Common import Logger

'''
订单模块异常订单查询：1、待处理 2、处理中 3、已处理->差评订单、预约延时、服务延时、上门延时、投诉订单、驳回订单
'''

#默认写入测试结果
isWrite=True
class QuestOrder(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Method()
        self.page = Page()
        self.isOk = "Fail"

    def test_question01(self):
        '''获取网点所有待处理异常订单数'''
        #指定日志文件输出路径
        Logger.setFormatter(logFile=data_dir(data="Log", filename="test_questorder.txt"))
        r = self.obj.test_Api(40,data=self.page.setSeach())
        self.obj.isContent(r,40,isWrite)

    def test_question02(self):
        '''获取网点所有处理中异常订单数'''
        r = self.obj.test_Api(41,data=self.page.setSeach(keyword="处理中"))
        self.obj.isContent(r,41,isWrite)

    def test_question03(self):
        '''获取网点所有已处理异常订单数'''
        r = self.obj.test_Api(42,data=self.page.setSeach(keyword="已处理"))
        self.obj.isContent(r,42,isWrite)

    def test_question04(self):
        '''获取网点已撤销订单'''
        r = self.obj.testApi(43)
        self.obj.isContent(r,43,isWrite)

    def test_question05(self):
        '''获取网点待处理差评订单信息'''
        r = self.obj.test_Api(44,data=self.page.ChaPingOrder(row=44,keyword="待处理"))
        self.obj.isContent(r,44,isWrite)

    def test_question06(self):
        '''获取网点处理中差评订单信息'''
        r = self.obj.test_Api(45,data=self.page.ChaPingOrder(row=45,keyword="处理中"))
        self.obj.isContent(r,45,isWrite)

    def test_question07(self):
        '''获取网点已处理差评订单信息'''
        r = self.obj.test_Api(46,data=self.page.ChaPingOrder(row=46,keyword="已处理"))
        self.obj.isContent(r,46,isWrite)

    def test_question08(self):
        '''获取网点待处理预约延时订单信息'''
        r = self.obj.test_Api(47,data=self.page.ChaPingOrder(row=47,keyword="待处理"))
        self.obj.isContent(r,47,isWrite)

    def test_question09(self):
        '''获取网点待处理预约延时订单信息'''
        r = self.obj.test_Api(48,data=self.page.ChaPingOrder(row=48,keyword="处理中"))
        self.obj.isContent(r,48,isWrite)

    def test_question10(self):
        '''获取网点待处理预约延时订单信息'''
        r = self.obj.test_Api(49,data=self.page.ChaPingOrder(row=49,keyword="已处理"))
        self.obj.isContent(r,49,isWrite)

    def test_question11(self):
        '''获取网点待处理上门延时订单信息'''
        r = self.obj.test_Api(50,data=self.page.ChaPingOrder(row=50,keyword="待处理"))
        self.obj.isContent(r,50,isWrite)

    def test_question12(self):
        '''获取网点待处理上门延时订单信息'''
        r = self.obj.test_Api(51,data=self.page.ChaPingOrder(row=51,keyword="处理中"))
        self.obj.isContent(r,51,isWrite)

    def test_question13(self):
        '''获取网点待处理上门延时订单信息'''
        r = self.obj.test_Api(52,data=self.page.ChaPingOrder(row=52,keyword="已处理"))
        self.obj.isContent(r,52,isWrite)

    def test_question14(self):
        '''获取网点待处理服务延时订单信息'''
        r = self.obj.test_Api(53,data=self.page.ChaPingOrder(row=53,keyword="待处理"))
        self.obj.isContent(r,53,isWrite)

    def test_question15(self):
        '''获取网点待处理服务延时订单信息'''
        r = self.obj.test_Api(54,data=self.page.ChaPingOrder(row=54,keyword="处理中"))
        self.obj.isContent(r,54,isWrite)

    def test_question16(self):
        '''获取网点待处理服务延时订单信息'''
        r = self.obj.test_Api(55,data=self.page.ChaPingOrder(row=55,keyword="已处理"))
        self.obj.isContent(r,55,isWrite)

    def test_question17(self):
        '''获取网点待处理投诉订单信息'''
        r = self.obj.test_Api(56,data=self.page.ChaPingOrder(row=56,keyword="待处理"))
        self.obj.isContent(r,56,isWrite)

    def test_question18(self):
        '''获取网点待处理投诉订单信息'''
        r = self.obj.test_Api(57,data=self.page.ChaPingOrder(row=57,keyword="处理中"))
        self.obj.isContent(r,57,isWrite)

    def test_question19(self):
        '''获取网点待处理投诉订单信息'''
        r = self.obj.test_Api(58,data=self.page.ChaPingOrder(row=58,keyword="已处理"))
        self.obj.isContent(r,58,isWrite)

    def test_question20(self):
        '''获取网点待处理驳回订单信息'''
        r = self.obj.test_Api(59,data=self.page.ChaPingOrder(row=59,keyword="待处理"))
        self.obj.isContent(r,59,isWrite)

    def test_question21(self):
        '''获取网点待处理驳回订单信息'''
        r = self.obj.test_Api(60,data=self.page.ChaPingOrder(row=60,keyword="处理中"))
        self.obj.isContent(r,60,isWrite)

    def test_question22(self):
        '''获取网点待处理驳回订单信息'''
        r = self.obj.test_Api(61,data=self.page.ChaPingOrder(row=61,keyword="已处理"))
        self.obj.isContent(r,61,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk="Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_questorder")

if __name__ == '__main__':
    unittest.main(verbosity=2)
