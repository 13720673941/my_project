#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/18 14:09

from public.common.logconfig import Log
from public.common.basepage import BasePage
import unittest
log = Log()
"""
封装断言函数
"""
class Assert(BasePage):

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def assert_in(self,expect,fact):
        """
        判断1是在2中返回
        """
        try:
            unittest.TestCase().assertIn(expect,fact)
            log.info('{0} Expect: {1} in Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
        except AssertionError:
            self.take_screen_shot()
            if expect not in fact:
                raise AssertionError('{0} Expect: {1} not in Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))

    def assert_not_in(self,expect,fact):
        """
        判断1不在2里面
        :return:
        """
        try:
            unittest.TestCase().assertNotIn(expect,fact)
            log.info('{0} Expect: {1} not in Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
        except AssertionError:
            self.take_screen_shot()
            if expect in fact:
                raise AssertionError('{0} Expect: {1} in Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))

    def assert_equal(self,expect,fact):
        """
        判断两个字段相等
        """
        try:
            unittest.TestCase().assertEqual(expect,fact)
            log.info('{0} Expect: {1} equal Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
        except AssertionError:
            self.take_screen_shot()
            if expect != fact:
                raise AssertionError('{0} Expect: {1} not equal Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))

    def assert_not_equal(self,expect,fact):
        """
        判断两个字段相等
        """
        try:
            unittest.TestCase().assertNotEqual(expect,fact)
            log.info('{0} Expect: {1} not equal Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
        except AssertionError:
            self.take_screen_shot()
            if expect == fact:
                raise AssertionError('{0} Expect: {1} equal Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))

    def assert_more_str_in(self,dictData,fact):
        """
        针对多条件搜索结果的判断
        """
        # DictData = {"a":"","b":"000","c":"333"}
        flag = False
        # 遍历字典的value值，循环判断是否在获取的字段中
        for key,value in dictData.items():
            # 字段数据中第一个CaseName 用例名称不在获取的页面信息中去掉不判断
            if key == 'CaseName':
                pass
            else:
                try:
                    unittest.TestCase().assertIn(value,fact)
                    flag = True
                except AssertionError:
                    self.take_screen_shot()
                    if value not in fact:
                        raise AssertionError('{0} Expect all value not in string of get in page, test -> FAIL.'.format(self.fail))
        # 断言
        if flag:
            log.info('{0} Expect all value in string of get in page, test -> PASS.'.format(self.success))

    def assert_el_in_page(self,fact):
        """
        判断页面元素存在
        """
        #  if fact:
        #      log.info('{0} Expect: True, Faction: {1}, test -> PASS.'.format(self.success,fact))
        #      return self.success
        #  else:
        #      log.error('{0} Expect: True, Faction: {1}, test -> FAIL.'.format(self.fail,fact))
        #      self.take_screen_shot()
        #      return self.fail
        try:
            unittest.TestCase().assertTrue(fact)
            log.info('{0} Expect: True, Faction: {1}, test -> PASS.'.format(self.success,fact))
        except AssertionError:
            self.take_screen_shot()
            if fact == False:
                raise AssertionError('{0} Expect: True, Faction: {1}, test -> FAIL.'.format(self.fail,fact))

    def assert_el_not_in_page(self,fact):
        """
        判断页面元素不存在
        """
        #  if fact:
        #      log.error('{0} Expect: False, Faction: {1}, test -> FAIL.'.format(self.fail,fact))
        #      self.take_screen_shot()
        #      return self.fail
        #  else:
        #      log.info('{0} Expect: False, Faction: {1}, test -> PASS.'.format(self.success,fact))
        #      return self.success
        try:
            unittest.TestCase().assertFalse(fact)
            log.info('{0} Expect: False, Faction: {1}, test -> PASS.'.format(self.success,fact))
        except AssertionError:
            self.take_screen_shot()
            if fact:
                raise AssertionError('{0} Expect: False, Faction: {1}, test -> FAIL.'.format(self.fail,fact))
    
    def assert_att_is_none(self,att_fact):
        """
        判断获取元素属性为空
        """
        #  if att_fact is None:
        #      log.info('{0} Expect: is None, Faction: {1} is None, test -> PASS.'.format(self.success,att_fact))
        #      return self.success
        #  else:
        #      log.error('{0} Expect: is None, Faction: {1} is not None, test -> FAIL.'.format(self.fail,att_fact))
        #      self.take_screen_shot()
        #      return self.fail
        try:
            unittest.TestCase().assertIsNone(att_fact)
            log.info('{0} Expect: is None, Faction: {1} is None, test -> PASS.'.format(self.success, att_fact))
        except AssertionError:
            self.take_screen_shot()
            if att_fact is not None:
                raise AssertionError('{0} Expect: is None, Faction: is not None, test -> FAIL.'.format(self.fail))