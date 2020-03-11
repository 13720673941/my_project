# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/4 22:57

from public.common.logConfig import Log
log = Log()

# 传入一个功能测试用例，判断ddt数据中每条数据的信息
def skipped_case(func):
    """
        该装饰器为：跳过用例的执行，在ddt模式中不能使用 unittest 框架中的方法
        使用unit中的方法会直接跳过该用例，ddt类型测试数据中的数据不能全部判断
        Usage:
        @skipped_case
        def test_001(self,ddt_data):
            xxx
    """
    def inner(self,ddt_data):
        # 这里ddt_data在用例的excel中isRun字段为No的不执行测试函数
        if ddt_data["isRun"].lower() == "yes":
            func(self,ddt_data)
        else:
            log.warning(
                "Skipped: -跳过不执行该用例 {0}: {1}".format(ddt_data["用例编号"],ddt_data["用例名称"]))
    return inner