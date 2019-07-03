# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/3 9:12

from public.common import runreport

def run():

    #创建测试套件
    suit = runreport.get_suits(ChildName='4、客户管理',CaseName='*.py')
    #生成报告
    runreport.run_report(ReportName='customer_manage_test_report_',FileName='4、客户管理',title='Customer Manage Module Test Result',
                        description='customer manage module case test result.',case=suit)

if __name__ == '__main__':
    run()