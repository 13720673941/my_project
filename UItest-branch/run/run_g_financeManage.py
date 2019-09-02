# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 11:15

from public.common import runreport

def run():

    # 获取测试用例集合
    suit = runreport.get_suits(ChildName="7、财务管理",CaseName="*.py")

    # 运行生成报告
    runreport.run_report(ReportName='finance_manage_test_report_',FileName='7、财务管理',title='Finance Manage Module Test Result',
                        description='Finance manage module case test result.',case=suit)

if __name__ == '__main__':
    run()
