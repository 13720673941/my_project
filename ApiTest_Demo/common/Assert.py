# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:38

"""
    unittest框架中的断言类二次封装
"""

from common.logConfig import Log
import unittest

class AssertClass():

    def __init__(self):
        self.unit = unittest.TestCase()
        self.log = Log()

    def assert_equal(self,first,second):
        """断言相等"""
        statusCode = 0
        try:
            self.unit.assertEqual(first,second)
            self.log.info("断言：“ {} ” 等于 “ {} ” -> 测试通过！".format(first,second))
        except:
            statusCode = 1
            self.log.error("断言：“ {} ” 不等于 “ {} ” -> 测试失败！！！".format(first,second))
            raise
        finally:
            return statusCode


if __name__ == '__main__':
    a = AssertClass()

    status = a.assert_equal("a","b")
    print(status)