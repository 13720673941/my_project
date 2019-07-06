# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/25 19:34

from configparser import ConfigParser
from config.pathconfig import *
import time

def write_test_result(isWrite,run_result,section,case):
    '''
    :param isWrite:     是否写入测试结果
    :param run_result:  测试结果一般为PASS OR FAIL
    :param section:     配置文件的section值
    :param case:        用例的名称
    :return:
    '''
    # 测试结果写入配置文件
    # 测试结果写入路径文件夹
    tm = time.strftime('%m-%d %H:%M',time.localtime(time.time()))
    if isWrite:  # 为真写入测试结果
        result = run_result + " " + tm
        ResultPath = testResultPath
        cf = ConfigParser()
        cf.read(ResultPath,encoding='gb18030') # 使用utf-8编码报错，字节超出范围不能写入测试结果，更换gb18030
        cf.set(section,case,result)
        with open(ResultPath,"w") as f:
            cf.write(f)
        # print('测试结果：{0}\n保存路径：{1}'.format(result,ResultPath))