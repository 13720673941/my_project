# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/4 14:19

from public.common.operateExcel import WriteResult
from public.common import basePages
from public.common.logConfig import Log
import unittest
log = Log()
"""
unittest 框架中断言方法的二次封装
该断言方法依赖于 operateExcel->get_all_data / get_ddt_data 方法获取的参数中的 Expectation 值
"""

class AssertMode(basePages.Page):

    def __init__(self,driver):
        basePages.Page.__init__(self,driver)
        self.driver = driver
        self.writeResult = WriteResult()
        # 固定通过/失败字段 write_result写入测试结果只能用 pass/fail判断
        self.Pass = "Pass"
        self.Fail = "Fail"
        # 初始化是否通过字段
        self.isPass = None

    def assert_equal(self,testData,faction):
        """判断字段相等"""

        # 测试数据中的期望值
        expectation = testData["Expectation"]
        try:
            unittest.TestCase().assertEqual(expectation,faction)
            log.info("断言：期望值“ {} ” 等于 实际值“ {} ” -> 测试通过 ！".format(expectation,faction))
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：期望值“ {} ” 不等于 实际值“ {} ” -> 测试失败 ！".format(expectation,faction))
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])

    def assert_not_equal(self,testData,faction):
        """判断字段不相等"""

        # 测试数据中的期望值
        expectation = testData["Expectation"]
        try:
            unittest.TestCase().assertNotEqual(expectation,faction)
            log.info("断言：期望值“ {} ” 不等于 实际值“ {} ” -> 测试通过 ！".format(expectation,faction))
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：期望值“ {} ” 等于 实际值“ {} ” -> 测试失败 ！".format(expectation,faction))
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])

    def assert_in(self,testData,faction):
        """判断字段1在字段2中"""

        expectation = testData["Expectation"]
        try:
            unittest.TestCase().assertIn(expectation,faction)
            log.info("断言：期望值“ {} ” 在 实际值“ {} ” 中 -> 测试通过 ！".format(expectation,faction))
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：期望值“ {} ” 不在 实际值“ {} ” 中 -> 测试失败 ！".format(expectation,faction))
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])

    def assert_not_in(self,testData,faction):
        """判断字段1不在字段2中"""

        expectation = testData["Expectation"]
        try:
            unittest.TestCase().assertNotIn(expectation,faction)
            log.info("断言：期望值“ {} ” 不在 实际值“ {} ” 中 -> 测试通过 ！".format(expectation,faction))
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：期望值“ {} ” 在 实际值“ {} ” 中 -> 测试失败 ！".format(expectation,faction))
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])

    def assert_is_true(self,faction,testData):
        """判断页面存在某元素 isDisplay() 方法返回True"""

        try:
            unittest.TestCase().assertTrue(faction)
            log.info("断言：该元素返回结果为 True -> 测试通过 ！")
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：该元素返回结果为 False -> 测试失败 ！")
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])

    def assert_is_false(self,faction,testData):
        """判断页面不存在某元素 isDisplay() 方法返回False"""

        try:
            unittest.TestCase().assertFalse(faction)
            log.info("断言：该元素返回结果为 False -> 测试通过 ！")
            self.isPass = self.Pass
        except:
            self.isPass = self.Fail
            self.driver.screen_shot()
            log.error("断言：该元素返回结果为 True -> 测试失败 ！")
            raise
        finally:
            self.writeResult.write_result(result=self.isPass,caseId=testData["CaseId"])


# if __name__ == '__main__':
#
#     a = AssertMode()
#     a.assert_equal({"Expectation":"aaa","CaseId":"baidu_search_001"},"nnn")




