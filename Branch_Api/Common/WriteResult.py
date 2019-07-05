# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import time,xlrd,xlwt
from configparser import ConfigParser
from Common.Public import data_dir
from xlutils.copy import copy
from Common import Variable

'''
1、对api测试结果写入config配置文件的封装
2、对api测试结果写入excel中的封装
'''

def write_to_Config(isWrite,run_result,case):

    '''
    :param isWrite: 是否写入测试结果
    :param run_result: 用例运行后的测试结果，一般为fail or pass
    :param case: 测试用例名称信息
    '''
    #总的一个py文件的执行结果
    DataPath = data_dir(data="Log",filename="TestResult.ini")
    tm = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #如果为真写入测试结果
    if isWrite:
        result = "["+tm+"]" + " ->>" + run_result
        cf = ConfigParser()
        cf.read(DataPath,"utf-8")
        cf.set("Test_Result",case,result)
        with open(DataPath,"w") as f:
            cf.write(f)
    else:
        pass

def write_to_Excel(isWrite,row,run_result):

    '''
    :param isWrite:是否写入真为写入
    :param row:用例的行数
    :param run_result:测试结果pass/fail
    '''
    #获取修改文件的路径信息
    excel = xlrd.open_workbook(data_dir(filename="BranchApi.xls"))
    #复制文件
    old_excel = copy(excel)
    ws = old_excel.get_sheet(0)
    tm = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if isWrite:
        #设置单元格颜色fail时选择红色填充
        style = xlwt.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        #判断是否执行成功，如果失败标记红色，通过标记绿色
        #颜色设置0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow
        if run_result.lower() == "pass":
            pattern.pattern_fore_colour = 3
        elif run_result.lower() == "fail":
            pattern.pattern_fore_colour = 2
        else:
            print("没有这个结果类型:{0}".format(run_result))
        style.pattern = pattern
        #设置写入结果的格式类型
        result = tm + " ->>" + "【"+run_result+"】"
        ws.write(row,Variable.get_Result(),result,style)
        #保存到源文件中去
        old_excel.save(data_dir(filename="BranchApi.xls"))
    else:
        pass

write_to_Excel(isWrite=True,row=3,run_result="Pass")
# write_to_Config(isWrite=True,run_result="pass",case="1111")