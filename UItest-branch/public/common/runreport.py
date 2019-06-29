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
    #top_level_dir 必须加上用例的主目录，不然默认为none还是上次的路径，会报错
    #这个top_level_dir会作为self的参数保存下来，这样第二次运行时 top_level_dir实际取的是上一次的路径，直接影响到了下一次的运行
    discover_suites = unittest.defaultTestLoader.discover(case_dir,pattern=CaseName,top_level_dir =testCasePath)
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

# print(get_suits(ChildName='1、注册登录',CaseName='*.py'))
# print(get_suits(ChildName='3、工单管理',CaseName='*.py'))
# print(get_suits(ChildName='2、修改密码',CaseName='*.py'))