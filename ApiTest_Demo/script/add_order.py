# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/7/2 12:42

from common.testApi import Request
from common.assertFunc import AssertClass
from common.writeResult import WriteResult
from common.operateFile import OperateFile
from config.pathConfig import *

import unittest

# 测试用例id编号
caseId = "add_order"

class TestAddRoom(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.request = Request()
        self.assertClass = AssertClass()
        self.writeResult = WriteResult()
        self.operateFile = OperateFile()
        self.data = self.operateFile.read_json(caseId)
        # 读取请求投参数，可根据业务需求进行封装
        self.header = {"authorization":self.operateFile.read_config("GLOBAL_PARAMS","token",GLOBAL_PARAMS_PATH)}

    def test_add_room(self):
        """测试登录接口"""
        self.res = self.request.request(caseId=caseId,headers=self.header,json=self.data)

    def tearDown(self):
        # 协议状态码断言
        status1 = self.assertClass.assert_httpCode(caseId,self.res.status_code)
        # 业务状态码断言
        status2 = self.assertClass.assert_serviceCode(caseId,self.res.json()["Status"])
        # 返回参数断言
        status3 = self.assertClass.assert_resValueEqual(caseId,self.res.json()["Value"])
        # 写入测试结果
        self.writeResult.write_result(caseId,status1+status2+status3)



if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(TestAddRoom)

    unittest.TextTestRunner().run(suits)