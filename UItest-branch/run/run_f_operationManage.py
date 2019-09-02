# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 11:14

from public.common import runreport

def run():

    # 获取测试用例集合
    suit = runreport.get_suits(ChildName="6、运营管理",CaseName="*.py")

    # 运行生成报告
    runreport.run_report(ReportName='operation_manage_test_report_',FileName='6、运营管理',title='Operation Manage Module Test Result',
                        description='Operation manage module case test result.',case=suit)

if __name__ == '__main__':
    run()