#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/2 11:58

from config.pathconfig import *
from config import HTMLTestRunnerCN
from public.common.rwconfig import write_txt_data
import unittest,time,datetime
"""
1、获取测试用例集 2、生成报告
"""
def get_suits(ChildName,CaseName):
    """运行测试套件，批量执行测试用例"""

    # 获取测试用例目录文件默认路径
    case_dir = testCasePath + ChildName + '\\'
    # discover函数遍历指定目录，按条件过滤文件，返回测试套件列表
    # top_level_dir 必须加上用例的主目录，不然默认为none还是上次的路径，会报错
    # 这个top_level_dir会作为self的参数保存下来，这样第二次运行时 top_level_dir实际取的是上一次的路径，直接影响到了下一次的运行
    discover_suites = unittest.TestLoader().discover(start_dir=case_dir,
                                                     pattern=CaseName,
                                                     top_level_dir=testCasePath
                                                     )
    return discover_suites

    # # 加载读取测试用例类下的test测试用例
    #
    # suits = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    # return suits

def write_test_result(FileName,test_result):
    """测试结果写入txt"""

    # ======写入脚本执行结果======
    # 写入脚本标题
    date = datetime.datetime.now().date()
    # 测试结果名称
    test_result_path = testResultPath+str(date)+'.txt'
    # 日期只写入一次
    if "登录注册" in FileName:
        write_txt_data(test_result_path, '\n')
        write_txt_data(test_result_path,'********** {0} **********'.format(date) + '\n')
    write_txt_data(test_result_path,"\n"+"---------- {0} ----------".format(FileName) + "\n")
    # 获取所有测试用例的个数
    all_case_number = str(test_result.testsRun)
    # 写入测试用例个数
    write_txt_data(test_result_path, "All test case: {0}".format(all_case_number) + '\n')
    # 获取成功的测试用例个数
    pass_case_number = str(test_result.success_count)
    # 写入pass测试用例个数
    write_txt_data(test_result_path, "Pass test case: {0}".format(pass_case_number) + '\n')
    # 错误的测试用例个数
    error_case_number = str(len(test_result.errors))
    # 写入错误的测试用例数据
    write_txt_data(test_result_path, "Error test case: {0}".format(error_case_number) + '\n')
    # 写入错误执行用例id
    if int(error_case_number) != 0:
        # 写入执行报错用例的id
        write_txt_data(test_result_path, "Error test case ID: " + "\n")
        for case_error,reason_error in test_result.errors:
            # print(test_result.errors)
            # 写入失败用例的id 和 reason
            write_txt_data(test_result_path," * "+case_error.id()+"\n")
    # 获取失败的用例列表
    fail_case_number = str(len(test_result.failures))
    # 写入测试用例个数
    write_txt_data(test_result_path, "Fail test case: {0}".format(fail_case_number) + '\n')
    # 如果失败为零不写入
    if int(fail_case_number) != 0:
        # 写入失败用例的id
        write_txt_data(test_result_path, "Fail test case ID: " + "\n")
        # 循环失败用例列表保存报错信息
        for case,reason in test_result.failures:
            # 写入失败用例的id 和 reason
            write_txt_data(test_result_path," * "+case.id()+"\n")

def run_report(ReportName,FileName,title,description,case):

    """
    :param FileName:        报告的文件名称
    :param title:           html报告页面标题信息
    :param description:     报告描述
    :param case:            用例集合
    :return:
    """

    tm = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
    Report = ReportName + tm + '.html'
    ReportPath = reportSavePath + FileName + '\\' + Report
    with open(ReportPath,'wb') as f:
        test_result = HTMLTestRunnerCN.HTMLTestRunner(
                                               verbosity=2,
                                               stream=f,
                                               title=title,
                                               description=description
                                               )\
            .run(case)
    print(' ** Create test report success, report path: {0}.'.format(ReportPath))

    # 写入测试结果
    write_test_result(FileName=FileName,test_result=test_result)





