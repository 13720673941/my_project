# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/18 14:09

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
        '''
        判断1是否在2中返回
        '''
        if expect in fact or fact in expect:
            log.info('{0} Expect: {1} in Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
            return self.success
        else:
            log.error('{0} Expect: {1} not in Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))
            #错误截图
            self.take_screen_shot()
            return self.fail

    def assert_equal(self,expect,fact):
        '''
        判断两个字段是否相等
        '''
        if expect == fact:
            log.info('{0} Expect: {1} equal Faction: {2}, test -> PASS.'.format(self.success,expect,fact))
            return self.success
        else:
            log.error('{0} Expect: {1} not equal Faction: {2}, test -> FAIL.'.format(self.fail,expect,fact))
            self.take_screen_shot()
            return self.fail

    def assert_more_str_in(self,dictData,fact):
        '''
        针对多条件搜索结果的判断
        '''
        #DictData = {"a":"","b":"000","c":"333"}
        flag = True
        #遍历字典的value值，循环判断是否在获取的字段中
        for key,value in dictData.items():
            #字段数据中第一个CaseName 用例名称不在获取的页面信息中去掉不判断
            if key == 'CaseName':
                pass
            else:
                if value in fact:
                    pass
                else:
                    flag = False
                    break
        #断言
        if flag:
            log.info('{0} Expect all value in string of get in page, test -> PASS.'.format(self.success))
            return self.success
        else:
            log.error('{0} Expect all value not in string of get in page, test -> FAIL.'.format(self.fail))
            self.take_screen_shot()
            return self.fail

    def assert_el_in_page(self,fact):
        """
        判断页面元素是否存在
        """
        if fact:
            log.info('{0} Expect: True, Faction: {1}, test -> PASS.'.format(self.success,fact))
            return self.success
        else:
            log.error('{0} Expect: True, Faction: {1}, test -> FAIL.'.format(self.fail,fact))
            self.take_screen_shot()
            return self.fail

    def assert_el_not_in_page(self,fact):
        """
        判断页面元素不存在
        """
        if fact:
            log.error('{0} Expect: False, Faction: {1}, test -> FAIL.'.format(self.fail,fact))
            self.take_screen_shot()
            return self.fail
        else:
            log.info('{0} Expect: False, Faction: {1}, test -> PASS.'.format(self.success,fact))
            return self.success
    
    def assert_att_is_none(self,att_fact):
        """
        判断获取元素属性为空
        """
        if att_fact is None:
            log.info('{0} Expect: is None, Faction: {1} is None, test -> PASS.'.format(self.success,att_fact))
            return self.success
        else:
            log.error('{0} Expect: is None, Faction: {1} is not None, test -> FAIL.'.format(self.fail,att_fact))
            self.take_screen_shot()
            return self.fail
