# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/2 17:15

from public.common import runReport

def run():

    # 获取测试用例集合
    suit = runReport.get_suits(ChildName="5、师傅管理", CaseName="*.py")

    # 运行生成报告
    runReport.run_report(ReportName='master_manage_test_report_', FileName='5、师傅管理', title='Master Manage Module Test Result',
                         description='Master manage module case test result.', case=suit)

if __name__ == '__main__':
    run()