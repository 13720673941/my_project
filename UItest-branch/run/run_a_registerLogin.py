# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/7 17:08

from public.common import runreport

def run():

    # 获取登录测试用例集合
    suit = runreport.get_suits(ChildName='1、注册登录',CaseName='*.py')
    # 运行测试集合生成报告
    runreport.run_report(ReportName='register_and_login_test_report_', FileName='1、登录注册', title='Register/Login Test Result',
                         description='register and login case test result.', case=suit)


if __name__ == '__main__':
    run()

