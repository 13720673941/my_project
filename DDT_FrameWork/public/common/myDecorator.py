# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/4 13:46

from public.common.logConfig import Log
log = Log()

"""
该装饰器为：跳过用例的执行，在ddt模式中不能使用 unittest 框架中的方法
使用unit中的方法会直接跳过该用例，ddt类型测试数据中的数据不能全部判断
Usage:
@skipped_case
def test_001(self,ddt_data):
    xxx
"""

def skip_case(func):

    def inner(self,testData):
        # 测试数据获取后会把isRun字段改为布尔类型: public->common->operateExcel->get_run_data
        if testData['IsRun']:
            func(self,testData)
        else:
            log.warning("-Skip: {} 此用例跳过不执行！".format(testData['CaseId']))
    return inner