# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/25 17:39

from public.common import runReport

def run():

    # 创建测试套件
    suit = runReport.get_suits(ChildName='2、修改密码')
    # 生成报告
    runReport.run_report(ReportName='alter_pwd_test_report_', FileName='2、修改密码', title='Alter PassWord Test Result',
                         description='alter/forget password case test result.', case=suit)

if __name__ == '__main__':
    run()