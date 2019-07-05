# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/30 11:15

from Common.Requests import Method
from Common import Logger
from Common.Page import Page
from Common.Public import data_dir
from Common.WriteResult import write_to_Config
import logging,unittest

'''
网点财务模块网点支出：1、网点当前月份支出金额信息 2、网点近三个月支出金额信息 3、一月份师傅工资信息查询
                  4、师傅年度工资信息查询 5、师傅近三个月费用信息查询 6、师傅当前月份费用信息
                  7、网点年度房租支出查询 8、网点当前月份房租支出查询 9、网点年度备件支出费用信息
                  10、网点当前月份备件费用支出信息 11、获取师傅发放工资列表信息 12、网点添加房租支出费用信息
                  13、网点添加备件支出费用信息 14、网点当前月份服务费账单查询 15、网点当月账单订单奖惩查询
                  16、获取网点当月月度奖惩信息 17、获取网点结算师傅列表 18、获取网点待结算、已结算订单信息
                  19、获取网点奖惩信息列表 20、获取师傅订单提成信息 21、获取师傅月度奖惩信息 22、师傅结算订单信息列表
                  23、师傅费用线下结算
'''

#默认写入测试结果
isWrite=True
class BranchExpend(unittest.TestCase):

    def setUp(self):
        '''实例化'''
        self.obj = Method()
        self.page = Page()
        self.isOk = "Fail"

    def test_expend01(self):
        '''网点当前月份支出金额信息'''
        #设置日志保存路径
        Logger.setFormatter(logFile=data_dir(data="Log",filename="test_expenditure.txt"))
        r = self.obj.test_Api(81,data=self.page.setQueryId(row=81,queryId="137"))
        self.obj.isContent(r,81,isWrite)

    def test_expend02(self):
        '''网点近三个月支出金额信息'''
        r = self.obj.test_Api(82,data=self.page.setQueryId(row=82,queryId="138"))
        self.obj.isContent(r,82,isWrite)

    def test_expend03(self):
        '''一月份师傅工资信息查询'''
        r = self.obj.test_Api(83,data=self.page.setQueryId(row=83,queryId="140"))
        self.obj.isContent(r,83,isWrite)

    def test_expend04(self):
        '''师傅年度工资信息查询'''
        r = self.obj.test_Api(84,data=self.page.setQueryId(row=84,queryId="139"))
        self.obj.isContent(r,84,isWrite)

    def test_expend05(self):
        '''师傅近三个月费用信息查询'''
        r = self.obj.test_Api(85,data=self.page.setQueryId(row=85,queryId="142"))
        self.obj.isContent(r,85,isWrite)

    def test_expend06(self):
        '''师傅当前月份费用信息'''
        r = self.obj.test_Api(86,data=self.page.setQueryId(row=86,queryId="143"))
        self.obj.isContent(r,86,isWrite)

    def test_expend07(self):
        '''网点年度房租支出查询'''
        r = self.obj.test_Api(87,data=self.page.setQueryId(row=87,queryId="144"))
        self.obj.isContent(r,87,isWrite)

    def test_expend08(self):
        '''网点当前月份房租支出查询'''
        r = self.obj.test_Api(88,data=self.page.setQueryId(row=88,queryId="145"))
        self.obj.isContent(r,88,isWrite)

    def test_expend09(self):
        '''网点年度备件支出费用信息'''
        r = self.obj.test_Api(89,data=self.page.setQueryId(row=89,queryId="146"))
        self.obj.isContent(r,89,isWrite)

    def test_expend10(self):
        '''网点当前月份备件费用支出信息'''
        r = self.obj.test_Api(90,data=self.page.setQueryId(row=90,queryId="147"))
        self.obj.isContent(r,90,isWrite)

    def test_expend11(self):
        '''获取师傅发放工资列表信息'''
        r = self.obj.testApi(91)
        self.obj.isContent(r,91,isWrite)

    def test_expend12(self):
        '''网点添加房租支出费用信息'''
        r = self.obj.testApi(92)
        self.obj.isContent(r,92,isWrite)

    def test_expend13(self):
        '''网点添加备件支出费用信息'''
        r = self.obj.testApi(93)
        self.obj.isContent(r,93,isWrite)

    def test_expend14(self):
        '''网点添加备件支出费用信息'''
        r = self.obj.test_Api(94,data=self.page.setQueryId(row=94,queryId="156"))
        self.obj.isContent(r,94,isWrite)

    def test_expend15(self):
        '''网点当月账单订单奖惩查询'''
        r = self.obj.test_Api(95,data=self.page.setQueryId(row=95,queryId="157"))
        self.obj.isContent(r,95,isWrite)

    def test_expend16(self):
        '''获取网点当月月度奖惩信息'''
        r = self.obj.test_Api(96,data=self.page.setQueryId(row=96,queryId="158"))
        self.obj.isContent(r,96,isWrite)

    def test_expend17(self):
        '''获取网点结算师傅列表'''
        r = self.obj.test_Api(97,data=self.page.setQueryId(row=97,queryId="159"))
        self.obj.isContent(r,97,isWrite)

    def test_expend18(self):
        '''获取网点待结算、已结算订单信息'''
        r = self.obj.testApi(98)
        self.obj.isContent(r,98,isWrite)

    def test_expend19(self):
        '''获取网点奖惩信息列表'''
        r = self.obj.testApi(99)
        self.obj.isContent(r,99,isWrite)

    def test_expend20(self):
        '''获取师傅订单提成信息'''
        r = self.obj.test_Api(100,data=self.page.setQueryId(row=100,queryId="151"))
        self.obj.isContent(r,100,isWrite)

    def test_expend21(self):
        '''获取师傅月度奖惩信息'''
        r = self.obj.test_Api(101,data=self.page.setQueryId(row=100,queryId="150"))
        self.obj.isContent(r,101,isWrite)

    def test_expend22(self):
        '''师傅结算订单信息列表'''
        r = self.obj.testApi(102)
        self.obj.isContent(r,102,isWrite)

    def test_expend23(self):
        '''师傅费用线下结算'''
        r = self.obj.testApi(103)
        self.obj.isContent(r,103,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOk="Pass"
        write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_expenditure")

if __name__ == '__main__':
    unittest.main(verbosity=2)
