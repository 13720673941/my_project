# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/7 17:08

from public.common import runReport

def run():

    # 获取登录测试用例集合
    suit = runReport.get_suits(ChildName='1、注册登录')
    # 运行测试集合生成报告
    runReport.run_report(testSuits=suit,ReportName='register_and_login_test_report_', title='Register/Login Test Result',
                         description='register and login case test result.')

if __name__ == '__main__':
    run()