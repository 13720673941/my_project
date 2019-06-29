# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/25 18:41

from public.common import runreport

def run():

    #创建测试套件
    suit = runreport.get_suits(ChildName='3、工单管理',CaseName='*.py')
    #生成报告
    runreport.run_report(ReportName='order_manage_test_report_',FileName='3、工单管理',title='Order Manage Module Test Result',
                        description='order manage module case test result.',case=suit)

if __name__ == '__main__':
    run()