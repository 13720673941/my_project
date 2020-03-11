#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/2 11:58

from config.pathConfig import *
from config import HTMLTestRunnerCN
from public.common.rwConfig import write_txt_data
import unittest,time,datetime

"""
1、获取测试用例集 2、生成报告
"""

def get_suits(ChildName,CaseName="*.py"):
    """运行测试套件，批量执行测试用例"""

    # 获取测试用例目录文件默认路径
    case_dir = testCasePath + ChildName + '\\'
    # discover函数遍历指定目录，按条件过滤文件，返回测试套件列表
    # -case_dir:这个是待执行用例的目录
    # -pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本
    # -top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了。
    # 这里第二次调用默认的还是上次取用例的目录，所以必须返回上级目录所以 top_level_dir 参数取上级目录
    discover_suites = unittest.TestLoader().discover(start_dir=case_dir,pattern=CaseName,top_level_dir=testCasePath)
    return discover_suites

# def write_test_result(FileName,test_result):
#     """测试结果写入txt"""
#
#     # ======写入脚本执行结果======
#     # 写入脚本标题
#     date = datetime.datetime.now().date()
#     # 测试结果名称
#     test_result_path = testResultPath+str(date)+'.txt'
#     # 日期只写入一次
#     if "登录注册" in FileName:
#         write_txt_data(test_result_path, '\n')
#         write_txt_data(test_result_path,'********** {0} **********'.format(date) + '\n')
#     write_txt_data(test_result_path,"\n"+"---------- {0} ----------".format(FileName) + "\n")
#     # 获取所有测试用例的个数
#     all_case_number = str(test_result.testsRun)
#     # 写入测试用例个数
#     write_txt_data(test_result_path, "All test case: {0}".format(all_case_number) + '\n')
#     # 获取成功的测试用例个数
#     pass_case_number = str(test_result.success_count)
#     # 写入pass测试用例个数
#     write_txt_data(test_result_path, "Pass test case: {0}".format(pass_case_number) + '\n')
#     # 错误的测试用例个数
#     error_case_number = str(len(test_result.errors))
#     # 写入错误的测试用例数据
#     write_txt_data(test_result_path, "Error test case: {0}".format(error_case_number) + '\n')
#     # 写入错误执行用例id
#     if int(error_case_number) != 0:
#         # 写入执行报错用例的id
#         write_txt_data(test_result_path, "Error test case ID: " + "\n")
#         for case_error,reason_error in test_result.errors:
#             # print(test_result.errors)
#             # 写入失败用例的id 和 reason
#             write_txt_data(test_result_path," * "+case_error.id()+"\n")
#     # 获取失败的用例列表
#     fail_case_number = str(len(test_result.failures))
#     # 写入测试用例个数
#     write_txt_data(test_result_path, "Fail test case: {0}".format(fail_case_number) + '\n')
#     # 如果失败为零不写入
#     if int(fail_case_number) != 0:
#         # 写入失败用例的id
#         write_txt_data(test_result_path, "Fail test case ID: " + "\n")
#         # 循环失败用例列表保存报错信息
#         for case,reason in test_result.failures:
#             # 写入失败用例的id 和 reason
#             write_txt_data(test_result_path," * "+case.id()+"\n")

def run_report(testSuits,ReportName="UI测试报告",title="超级售后PC端UI自动化测试报告",description=""):

    """
    :param FileName:        报告的文件名称
    :param title:           html报告面标题信息
    :param description:     报告描述
    :param case:            用例集合
    :return:
    """

    tm = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
    Report = ReportName + tm + '.html'
    ReportPath = reportSavePath + Report
    with open(ReportPath,'wb') as f:
        HTMLTestRunnerCN.HTMLTestRunner(
            verbosity=2,
            stream=f,
            title=title,
            description=description
        ).run(testSuits)
    print(' ** Create test report success, report path: {0}.'.format(ReportPath))

    # return result

def run_fail_case(result):
    """这里逻辑解析失败用例字符串中的数据重新获取测试用例中的全部数据重新运行一遍"""

    # 失败用例集合
    failCaseList = []
    if len(result.failures) != 0:
        for case, reason in result.failures:
            # 截取字段中用例路径字段
            failCaseList.append(case.id().split("_")[0])
    if len(result.errors) != 0:
        # 异常用例集合
        for case_error, reason_error in result.errors:
            failCaseList.append(case_error.id().split("_")[0])
    print(list(set(failCaseList)))
    # 建立测试套件
    failCaseSuits = unittest.TestSuite()
    # 解析失败用例id
    for caseName in list(set(failCaseList)):
        fileName = caseName.split(".")[0]
        pyName = caseName.split(".")[1]
        # 重新获取失败的测试用例
        suits = get_suits(ChildName=fileName,CaseName=pyName+"*.py")
        failCaseSuits.addTests(suits)
    # 运行失败用例
    tm = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    Report = "异常失败用例重测报告" + tm + '.html'
    ReportPath = reportSavePath + Report
    with open(ReportPath, 'wb') as f:
        HTMLTestRunnerCN.HTMLTestRunner(
            verbosity=2,
            stream=f,
            title="超级售后PC端UI自动化测试报告",
            description=""
        ).run(failCaseSuits)

