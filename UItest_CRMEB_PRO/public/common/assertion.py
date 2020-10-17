# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/9/2 9:19

"""
    unittest 断言模块二次封装，失败截图，写入测试结果
"""

from public.common.logConfig import log
from public.common.writeResult import WriteResult
import unittest

class Assertion():

    def __init__(self):
        # 实例化类
        self.log = log()
        self.writeResult = WriteResult()
        self.unit = unittest.TestCase()
        # 初始化字段
        self.Pass = "Pass"
        self.Fail = "Fail"
        self.isPass = None

    def assert_equal(self,first,dictData):
        """判断两字段相等"""

        # 期望值
        expectationData = dictData["expectation"]
        try:
            self.unit.assertEqual(first,expectationData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’等于期望值‘%s’ >>> 测试通过！"%(first,expectationData))
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’不等于期望值‘%s’ >>> 测试失败！"%(first,expectationData))
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])

    def assert_notEqual(self,first,dictData):
        """判断两个字段不相等"""

        # 期望值
        expectationData = dictData["expectation"]
        try:
            self.unit.assertNotEqual(first,expectationData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’不等于期望值‘%s’ >>> 测试通过！"%(first,expectationData))
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’等于期望值‘%s’ >>> 测试失败！"%(first,expectationData))
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])

    def assert_in(self,first,dictData):
        """判断第一个字段在第二个里面"""

        # 期望值
        expectationData = dictData["expectation"]
        try:
            self.unit.assertIn(first,expectationData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’在期望值‘%s’中 >>> 测试通过！"%(first,expectationData))
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’不在期望值‘%s’中 >>> 测试失败！"%(first,expectationData))
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])

    def assert_notIn(self,first,dictData):
        """判断第一个字段不在第二个里面"""

        # 期望值
        expectationData = dictData["expectation"]
        try:
            self.unit.assertNotIn(first,expectationData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’不在期望值‘%s’中 >>> 测试通过！"%(first,expectationData))
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’在期望值‘%s’中 >>> 测试失败！"%(first,expectationData))
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])

    def assert_true(self,factionData,dictData):
        """判断页面存在该字段"""

        try:
            self.unit.assertTrue(factionData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’存在 >>> 测试通过！"%factionData)
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’不存在 >>> 测试失败！"%factionData)
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])

    def assert_false(self,factionData,dictData):
        """判断页面不存在该字段"""

        try:
            self.unit.assertFalse(factionData)
            self.isPass = self.Pass
            self.log.info("断言：实际值‘%s’不存在 >>> 测试通过！"%factionData)
        except:
            self.isPass = self.Fail
            self.log.error("断言：实际值‘%s’存在 >>> 测试失败！"%factionData)
            """
            加入截图功能
            """
        finally:
            # excel中写入测试结果
            self.writeResult.write_result(self.isPass,dictData["caseId"])


if __name__ == '__main__':
    assertion = Assertion()
    data = {"caseId":"login_001","expectation":True}
    assertion.assert_false(False,data)