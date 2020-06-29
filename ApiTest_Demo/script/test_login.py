# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/20 19:23

from common.testApi import Request
from common.getTestCase import ReadTestCase
from common.Assert import AssertClass
from common.writeResult import WriteResult
from common.operateFile import OperateFile
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.request = Request()
        self.readCase = ReadTestCase()
        self.assertClass = AssertClass()
        self.writeResult = WriteResult()
        self.operateFile = OperateFile()
        self.caseId = "login_001"
        self.httpCode = self.readCase.get_http_code(self.caseId)
        self.serverCode = self.readCase.get_service_code(self.caseId)
        self.keyWord = self.readCase.get_response_value(self.caseId)
        self.data = self.operateFile.read_yaml()[self.caseId]

    def test_login_001(self):
        """测试登录接口"""
        self.res = self.request.request(caseId=self.caseId,json=self.data)
        self.status = self.assertClass.assert_equal(self.request.result(self.res)["msg"],self.keyWord)
        self.writeResult.write_result(self.caseId, status=self.status)

    def tearDown(self):
        # 写入测试结果
        pass

if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    unittest.TextTestRunner().run(suits)