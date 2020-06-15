# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/14 10:13

from config.pathConfig import *
import HTMLTestRunnerCN,unittest,datetime

"""
    运行测试脚本发送邮件
"""
# 报告页面标题及描述信息
REPORT_TITLE = "xxx系统自动化测试报告"
REPORT_DESCRIPTION = "报告描述"

def run():

    # 获取测试用例集合
    suits = unittest.TestLoader().discover(testScriptPath,"test_*.py")
    # 创建测试报告名称
    timeStr = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    reportName = testReportPath+timeStr+".html"
    # 写入报告
    with open(reportName,"wb") as fp:
        HTMLTestRunnerCN.HTMLTestRunner(
            verbosity=3,
            stream=fp,
            title=REPORT_TITLE,
            description=REPORT_DESCRIPTION
        ).run(suits)

if __name__ == '__main__':
    run()