# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/2 11:58

import HTMLTestRunnerCN
from config.pathconfig import *
import unittest,time
'''
1、获取测试用例集 2、生成报告
'''
def get_suits(ChildName,CaseName):
    '''运行测试套件，批量执行测试用例'''
    #获取测试用例目录文件默认路径
    case_dir = testCasePath + ChildName + '\\'
    #discover函数遍历指定目录，按条件过滤文件，返回测试套件列表
    discover_suites = unittest.defaultTestLoader.discover(case_dir,pattern=''+CaseName+'')
    return discover_suites

def run_report(ReportName,FileName,title,description,case):
    '''
    :param FileName:        报告的文件名称
    :param title:           html报告页面标题信息
    :param description:     报告描述
    :param case:            用例集合
    :return:
    '''
    tm = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
    Report = ReportName + tm + '.html'
    ReportPath = reportSavePath + FileName + '\\' + Report
    with open(ReportPath,'wb') as f:
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=f,
                                               title=title,
                                               description=description
                                               )
        runner.run(case)
        print('*Create test report success, report path: {0}.'.format(ReportPath))


