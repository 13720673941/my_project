# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import os,logging,time,HTMLTestRunnerCN
from Common.OperationConfig import operationConfig

'''
1、查找文件的路径信息，默认配置文件在Data文件夹
2、获取返回KEY值中的value值
'''

def data_dir(data="Data",filename=None):

    '''
    :param data: 文件夹名字
    :param filename:  文件名字
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)

def runCase(fileName,reportName,titleName,scription,case):

    '''
    :param fileName:文件夹名字
    :param reportName:测试报告名字
    :param titleName:测试报告标题名字
    :param scription:测试报告描述信息
    :param case:测试用例集合
    '''

    tm = time.strftime("%y-%m-%d %H %M %S",time.localtime(time.time()))
    filePath = "../Report/"+fileName+"/"
    report = filePath + reportName + tm + ".html"
    fp = open(report,"wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,
                                             title=""+titleName+"",
                                             description=""+scription+"")
    runner.run(case)
    fp.close()

