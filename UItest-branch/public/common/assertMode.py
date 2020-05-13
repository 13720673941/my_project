#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/18 14:09

from public.common.basePage import BasePage
from public.common.operateExcel import Write_Excel
import unittest

class Assert(BasePage,Write_Excel):
    """
        封装断言函数
    """

    def __init__(self,driver,sheet_name):
        BasePage.__init__(self,driver)
        self.sheet_name = sheet_name

    def assert_in(self,test_data,fact):
        """
        判断1是在2中返回
        """
        expect = test_data["期望值"]
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertIn(expect,fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: {0} in Faction: {1}, test -> PASS.'.format(expect,fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if expect not in fact:
                raise AssertionError('Expect: {0} not in Faction: {1}, test -> FAIL.'.format(expect,fact))

    def assert_not_in(self,test_data,fact):
        """
        判断1不在2里面
        :return:
        """
        expect = test_data["期望值"]
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertNotIn(expect,fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: {0} not in Faction: {1}, test -> PASS.'.format(expect,fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if expect in fact:
                raise AssertionError('Expect: {0} in Faction: {1}, test -> FAIL.'.format(expect,fact))

    def assert_equal(self,test_data,fact):
        """
        判断两个字段相等
        """
        expect = test_data["期望值"]
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertEqual(expect,fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: {0} equal Faction: {1}, test -> PASS.'.format(expect,fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if expect != fact:
                raise AssertionError('Expect: {0} not equal Faction: {1}, test -> FAIL.'.format(expect,fact))

    def assert_not_equal(self,test_data,fact):
        """
        判断两个字段相等
        """
        expect = test_data["期望值"]
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertNotEqual(expect,fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: {0} not equal Faction: {1}, test -> PASS.'.format(expect,fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if expect == fact:
                raise AssertionError('Expect: {0} equal Faction: {1}, test -> FAIL.'.format(expect,fact))

    def assert_more_str_in(self,test_data,fact):
        """
        针对多条件搜索结果的判断
        """
        Id = test_data["用例编号"]
        # DictData = {"a":"","b":"000","c":"333"}
        flag = False
        # 遍历字典的value值，循环判断是否在获取的字段中
        for key,value in test_data.items():
            # 字段数据中第一个CaseName 用例名称不在获取的页面信息中去掉不判断
            if key not in ["用例编号","用例名称","期望值","isRun"]:
                try:
                    unittest.TestCase().assertIn(value,fact)
                    flag = True
                except AssertionError:
                    self.write_result(self.sheet_name,"测试失败",Id)
                    self.take_screen_shot()
                    if value not in fact:
                        raise AssertionError('Expect all value not in string of get in page, test -> FAIL.')
        # 断言
        if flag:
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect all value in string of get in page, test -> PASS.')

    def assert_el_in_page(self,test_data,fact):
        """
        判断页面元素存在
        """
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertTrue(fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: True, Faction: {0}, test -> PASS.'.format(fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if fact == False:
                raise AssertionError('Expect: True, Faction: {0}, test -> FAIL.'.format(fact))

    def assert_el_not_in_page(self,test_data,fact):
        """
        判断页面元素不存在
        """
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertFalse(fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: False, Faction: {0}, test -> PASS.'.format(fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试失败",Id)
            self.take_screen_shot()
            if fact:
                raise AssertionError('Expect: False, Faction: {0}, test -> FAIL.'.format(fact))
    
    def assert_att_is_none(self,test_data,att_fact):
        """
        判断获取元素属性为空
        """
        Id = test_data["用例编号"]
        try:
            unittest.TestCase().assertIsNone(att_fact)
            self.write_result(self.sheet_name,"测试通过",Id)
            self.log.info('Expect: is None, Faction: {0} is None, test -> PASS.'.format( att_fact))
        except AssertionError:
            self.write_result(self.sheet_name,"测试通过",Id)
            self.take_screen_shot()
            if att_fact is not None:
                raise AssertionError(' Expect: is None, Faction: is not None, test -> FAIL.')