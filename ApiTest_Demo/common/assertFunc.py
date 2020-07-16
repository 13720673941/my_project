# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:38

"""
    unittest框架中的断言类二次封装
"""

from common.getTestCase import ReadTestCase
from common.logConfig import Log

import unittest

class AssertClass():

    def __init__(self):
        self.unit = unittest.TestCase()
        self.getData = ReadTestCase()
        self.log = Log()

    def assert_httpCode(self,caseId,factionCode):
        """协议状态码的断言"""

        # 获取测试用例文档中的http请求协议状态码
        httpCode = int(self.getData.get_http_code(caseId))
        statusCode = 0
        try:
            self.unit.assertEqual(httpCode,factionCode)
            self.log.info("【协议状态码断言】：期望值{} 等于 实际值{}，测试通过！".format(httpCode,factionCode))
        except:
            statusCode = 1
            self.log.error("【协议状态码断言】：期望值{} 不等于 实际值{}，测试失败！".format(httpCode,factionCode))
            raise
        finally:
            return statusCode

    def assert_serviceCode(self,caseId,factionCode):
        """业务状态码断言"""

        # 获取测试用例文档中的http请求业务状态码
        serviceCode = self.getData.get_service_code(caseId)
        statusCode = 0
        try:
            self.unit.assertEqual(serviceCode,factionCode)
            self.log.info("【业务状态码断言】：期望值{} 等于 实际值{}，测试通过！".format(serviceCode,factionCode))
        except:
            statusCode = 1
            self.log.error("【业务状态码断言】：期望值{} 不等于 实际值{}，测试失败！".format(serviceCode,factionCode))
            raise
        finally:
            return statusCode

    def assert_resValueIn(self,caseId,factionValue):
        """返回参数断言"""

        # 获取测试用例文档中的http请求返回校验值
        serviceCode = self.getData.get_response_value(caseId)
        statusCode = 0
        try:
            self.unit.assertIn(serviceCode,factionValue)
            self.log.info("【返回参数断言】：期望值{} 存在于 实际值{}，测试通过！".format(serviceCode,factionValue))
        except:
            statusCode = 1
            self.log.error("【返回参数断言】：期望值{} 不存在于 实际值{}，测试失败！".format(serviceCode,factionValue))
            raise
        finally:
            return statusCode

    def assert_resValueEqual(self,caseId,factionValue):
        """返回参数断言"""

        # 获取测试用例文档中的http请求返回校验值
        serviceCode = self.getData.get_response_value(caseId)
        statusCode = 0
        try:
            self.unit.assertIn(serviceCode,factionValue)
            self.log.info("【返回参数断言】：期望值{} 等于 实际值{}，测试通过！".format(serviceCode,factionValue))
        except:
            statusCode = 1
            self.log.error("【返回参数断言】：期望值{} 不等于 实际值{}，测试失败！".format(serviceCode,factionValue))
            raise
        finally:
            return statusCode


if __name__ == '__main__':
    a = AssertClass()
    status = a.assert_resValueIn("login_001","王晓华")
    print(status)