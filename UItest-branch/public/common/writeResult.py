# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/9 20:59

from config.pathConfig import *
from xlutils.copy import copy
import xlwt,xlrd

def get_test_result():

    """
        统计测试用例 excel 中的测试用例的测试结果数据
    """
    # 初始所有用例编号列表
    all_case_list = []
    # 初始化通过的用例编号
    pass_case_list = []
    # 初始化失败用例的编号
    fail_case_list = []
    # 初始化异常用例编号
    error_case_list = []
    # 初始化执行用例编号
    run_case_list = []
    # 初始化跳过用例编号
    skip_case_list = []
    # 读取 excel
    work_book = xlrd.open_workbook(testExcelPath,formatting_info=True)
    # 获取所有的表格数量
    all_table = len(work_book.sheets())
    # 循环遍历所有表格中的用例数
    for table_num in range(all_table):
        table = work_book.sheet_by_index(table_num)
        all_case = table.col_values(0)
        # 获取所有用例编号的列表
        for case in all_case:
            if case != "" and case != "Id":
                all_case_list.append(case)
        # 获取所有执行结果添加到列表中
        for row_num in range(1,len(all_case)):
            # 获取用例执行情况编号，是否执行字段为 no 的不添加
            if table.cell_value(row_num,5).lower() == "yes":
                run_case_list.append(table.cell_value(row_num,0))
                if "通过" in table.cell_value(row_num,4):
                    pass_case_list.append(table.cell_value(row_num,0))
                elif "失败" in table.cell_value(row_num,4):
                    fail_case_list.append(table.cell_value(row_num,0))
                else:
                    error_case_list.append(table.cell_value(row_num,0))
            elif table.cell_value(row_num,5).lower() == "no":
                skip_case_list.append(table.cell_value(row_num,0))

    return all_case_list,pass_case_list,fail_case_list,error_case_list,run_case_list,skip_case_list

def write_statistical_result(project_name="超级售后PC端",run_man="邓鹏飞"):

    # 获取测试结果
    all_case_list,pass_case_list,fail_case_list,error_case_list,run_case_list,skip_case_list = get_test_result()
    # print("总共用例列表：{0}".format(all_case_list))
    # print("通过用例列表：{0}".format(pass_case_list))
    # print("失败用例列表：{0}".format(fail_case_list))
    # print("异常用例列表：{0}".format(error_case_list))
    # print("运行用例列表：{0}".format(run_case_list))
    # print("跳过用例列表：{0}".format(skip_case_list))

    all_count = len(all_case_list)
    pass_count = len(pass_case_list)
    fail_count = len(fail_case_list)
    error_count =len(error_case_list)
    run_count = len(run_case_list)
    skip_count = len(skip_case_list)
    success_ = str(round((pass_count/run_count),4)*100)

    txt = "项目："+project_name+", 执行人："+run_man+", 总用例数量：{0}, 总执行用例数：{1}, " \
          "成功用例数：{2}, 失败用例数：{3}, 异常用例数：{4}, 跳过用例数：{5}, 成功率：{6}%"\
        .format(
        str(all_count),str(run_count),str(pass_count),str(fail_count),str(error_count),str(skip_count),success_)

    result_excel_path = r"D:\my_test_script\UItest-branch\result\statistical_result.xls"
    # 读取 excel
    work_book = xlrd.open_workbook(result_excel_path,formatting_info=True)
    ws = copy(work_book)
    table = ws.get_sheet(0)
    # 创建一个样式
    style = xlwt.XFStyle()
    font = xlwt.Alignment()
    # 上下居中样式
    font.vert = 0x01
    # 添加样式
    style.alignment = font
    # 写入测试结果执行情况汇总
    table.write(1,0,txt,style)
    table_1 = work_book.sheet_by_index(0)
    # 清空excel中历史数据
    for col_num in range(0,3):
        case_name_col = table_1.col_values(col_num,5)
        for i in range(5,len(case_name_col)+5):
            if table_1.cell_value(i,col_num) != "":
                table.write(i,col_num,"")
    # 写入失败用例编号
    for i in range(5,fail_count+5):
        table.write(i,0,fail_case_list[i-5])
    # 写入异常用例编号
    for i in range(5,error_count+5):
        table.write(i,1,error_case_list[i-5])
    # 写入跳过用例编号
    for i in range(5,skip_count+5):
        table.write(i,2,skip_case_list[i-5])
    ws.save(result_excel_path)

write_statistical_result()