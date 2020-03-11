# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/5 12:04

from public.common import runReport

def run():

    # 获取测试用例集合
    suit = runReport.get_suits(ChildName="8、备件管理")

    # 运行生成报告
    runReport.run_report(testSuits=suit,ReportName='sparePart_manage_test_report_',title='SparePart Manage Module Test Result',
                         description='SparePart manage module case test result.')

if __name__ == '__main__':
    run()
