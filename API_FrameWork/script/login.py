# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/20 19:23

from common.testApi import Request
from common.assertFunc import AssertClass
from common.writeResult import WriteResult
from common.operateFile import OperateFile
from config.pathConfig import *

import unittest

# 测试用例id编号
caseId = "login"

class TestLogin(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.request = Request()
        self.assertClass = AssertClass()
        self.writeResult = WriteResult()
        self.operateFile = OperateFile()
        self.data = self.operateFile.read_json(caseId)

    def test_login_001(self):
        """测试登录接口"""
        self.res = self.request.request(caseId=caseId,json=self.data)

    def tearDown(self):
        # 协议状态码断言
        status1 = self.assertClass.assert_httpCode(caseId,self.res.status_code)
        # 业务状态码断言
        status2 = self.assertClass.assert_serviceCode(caseId,self.res.json()["Status"])
        # 返回数据校验
        status3 = self.assertClass.assert_resValueEqual(caseId,self.res.json()["Value"]["UserName"])
        # 写入测试结果
        self.writeResult.write_result(caseId,status1+status2+status3)
        # 写入token
        tokenStr = self.res.json()["Value"]["Token"]
        self.operateFile.write_config("GLOBAL_PARAMS","token","Bearer "+tokenStr,GLOBAL_PARAMS_PATH)


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

    unittest.TextTestRunner().run(suits)