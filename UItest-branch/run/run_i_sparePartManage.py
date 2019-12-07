# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/5 12:04

from public.common import runreport

def run():

    # 获取测试用例集合
    suit = runreport.get_suits(ChildName="8、备件管理",CaseName="*.py")

    # 运行生成报告
    runreport.run_report(ReportName='sparePart_manage_test_report_',FileName='8、备件管理',title='SparePart Manage Module Test Result',
                        description='SparePart manage module case test result.',case=suit)

if __name__ == '__main__':
    run()
