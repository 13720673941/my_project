# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/25 17:39

from public.common import runreport

def run():

    # 创建测试套件
    suit = runreport.get_suits(ChildName='2、修改密码',CaseName='*.py')
    # 生成报告
    runreport.run_report(ReportName='alter_pwd_test_report_', FileName='2、修改密码', title='Alter PassWord Test Result',
                        description='alter/forget password case test result.', case=suit)

if __name__ == '__main__':
    run()