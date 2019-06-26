# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

import time,os
from configparser import ConfigParser
from Common import Pubilc

def WriteResultToConfig(section,case,run_result,isWrite):
    '''
    测试完成是否写入测试结果
    :param case:测试用例名称
    :param run_result:测试结果pass/fail
    :param isWrite:是否写入
    :param newline:最后一个测试要分割线
    :return:
    '''
    #==========【测试结果写入配置文件】==========
    #测试结果写入路径文件夹
    tm = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if isWrite:#为真写入测试结果
        result = tm + " ->" + run_result
        ResultPath = Pubilc.data_dir(filename='TestResult.ini')
        cf = ConfigParser()
        cf.read(ResultPath,encoding='utf-8')
        cf.set(section,case,result)
        with open(ResultPath,"w") as f:
            cf.write(f)
        #cf.write(open(ResultPath,'w',encoding='UTF-8'))
        print('测试结果：{0}\n保存路径：{1}'.format(result,ResultPath))

def WriteResultToTxt(isWrite,case,run_result,NewLine=False):
    #==========【测试结果写入文本】===========
    #txt文件格式
    tm = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #写入文件路径信息
    Path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ResultPath = Path + "\\Log\\RunResult\\"
    LogName = ResultPath + 'RunResult' + tm + '.txt'
    line = '\n-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'+'\n'
    #写入测试结果
    if isWrite:
        #如果用例为集合的最后一个写入分界线
        if NewLine:
            result = case + "->" + run_result + line
        #默认没有分界线
        else:
            result = case + "->" + run_result + '  '
        #打开创建文件夹
        with open(LogName,'a') as f:
            f.write(result)


# WriteResultToTxt(isWrite=True,case='222222',run_result='pass',NewLine=True)