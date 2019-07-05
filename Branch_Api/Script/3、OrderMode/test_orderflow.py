# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 11:22

import unittest,json,logging,time,requests
from Common import Requests
from Common import Public
from Common import WriteResult
from Common.OperationConfig import operationConfig
from Common.OperationJson import operationJson
from Common import Logger
from Common.Page import Page

'''
网点自营订单流程：1、网点添加订单->2、派单到师傅->3、网点记录反馈->4、网点预约用户->5、网点改约用户->6、网点取消订单
'''
#默认写入测试结果
isWrite=True
class OrderFlow(unittest.TestCase):

    def setUp(self):
        '''实例化模块'''
        self.obj = Requests.Method()
        self.config = operationConfig()
        self.opJson = operationJson()
        self.page = Page()
        #默认执行结果失败
        self.isOK = "Fail"

    def test_flow01(self):
        '''网点添加自营订单'''
        #设置日志路径信息
        Logger.setFormatter(logFile=Public.data_dir(data="Log", filename="test_orderflow.txt"))
        r = self.obj.testApi(20)
        self.obj.isContent(r,20,isWrite)

    def test_flow02(self):
        '''获取待派单中新建订单的单号信息'''
        time.sleep(2)
        r = self.obj.testApi(21)
        self.obj.isContent(r,21,isWrite)
        #获取订单列表中第一个新建订单数据存入文档后面调用
        AddTradePkId = r.json()["result"]["rows"][0]["TradeProductType"]["TradePkId"]
        AddTradeId = r.json()["result"]["rows"][0]["TradeId"]
        #写入配置文件添加订单信息中去后面关联调用该信息
        self.config.writeConfig(section="AddOrder",option="AddTradePkId",value=AddTradePkId)
        self.config.writeConfig(section="AddOrder",option="AddTradeId",value=AddTradeId)

    def test_flow03(self):
        '''网点派单到固定师傅'''
        r = self.obj.test_Api(22,data=self.page.setPleaseOrder())
        self.obj.isContent(r,22,isWrite)

    def test_flow04(self):
        '''网点订单记录反馈'''
        r = self.obj.test_Api(23,data=self.page.submitFK())
        self.obj.isContent(r,23,isWrite)

    def test_flow05(self):
        '''网点预约用户'''
        r = self.obj.test_Api(24,data=self.page.reserveOrder())
        self.obj.isContent(r,24,isWrite)

    def test_flow06(self):
        '''网点改约用户'''
        r = self.obj.test_Api(25,data=self.page.reserverOrder2())
        self.obj.isContent(r,25,isWrite)

    def test_flow07(self):
        '''网点取消订单'''
        r = requests.post(url=self.page.canelOrder(),
                          data=self.opJson.get_jsonData(26),
                          headers=self.obj.apiHeaders(26))
        self.obj.isContent(r,26,isWrite)
        Logger.removeHandler()

    def tearDown(self):

        self.isOK="Pass"
        WriteResult.write_to_Config(isWrite=isWrite,run_result=self.isOK,case="test_orderflow")

if __name__ == '__main__':
    unittest.main(verbosity=2)
