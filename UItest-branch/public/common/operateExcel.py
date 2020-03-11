# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/28 15:34

from config.pathConfig import *
from xlutils.copy import copy
import xlrd,json,datetime,xlwt

class Variable:
    """
    excel 表格中每一列是固定的所以索引都是定死的
    """

    Id = 0
    CaseName = 1
    TestData = 2
    Expectation = 3
    Result = 4
    IsRun = 5

class Read_Excel:

    def __init__(self,sheet_name):
        """读取 excel 表格"""
        self.excel_data = xlrd.open_workbook(testExcelPath,formatting_info=True)
        self.table = self.excel_data.sheet_by_name(sheet_name)
        self.sheet_name = sheet_name

    def get_row_number(self,case_id):
        """获取第一列全部的数据，返回 Id 的索引信息"""
        Id_list = self.table.col_values(0)
        if case_id not in Id_list:
            raise NameError(" This case id: {0} not in table ! ".format(case_id))
        return Id_list.index(case_id)

    def get_case_name(self,case_id):
        """获取测试用例名称"""
        return self.table.cell_value(self.get_row_number(case_id),Variable.CaseName)

    def get_test_data(self,case_id):
        """获取测试数据信息"""
        read_data = self.table.cell_value(self.get_row_number(case_id),Variable.TestData)
        # 判断测试数据是否为空为空的话json.loads()报错
        if read_data == "":
            # 为空返回空字典
            return {}
        else:
            try:
                # 字符串转化为字典，返回一个字典数据
                return json.loads(read_data)
            except:
                raise TypeError(" {0} test data type is error ! ".format(read_data))

    def get_expectation(self,case_id):
        """获取期望值"""
        return self.table.cell_value(self.get_row_number(case_id),Variable.Expectation)

    def get_isRun_text(self,case_id):
        """
            获取用例是否执行判断字段，该方法只在unittest框架中判断是否执行 @unittest.skipUnless 中的参数值
        """
        is_run = self.table.cell_value(self.get_row_number(case_id),Variable.IsRun)
        if is_run.lower() == "yes":
            return True
        elif is_run.lower() == "no":
            return False
        else:
            raise NameError("{0} is run text type is error ! ".format(is_run))

    def get_dict_data(self,case_id):
        """获取一行的全部数据为字典格式"""

        case_id_dict = {}
        case_id_dict["用例编号"] = case_id
        case_name_dict = {}
        case_name_dict["用例名称"] = self.get_case_name(case_id)
        test_data_dict = self.get_test_data(case_id)
        expectation_dict = {}
        expectation_dict["期望值"] = str(self.get_expectation(case_id))
        is_run = {}
        is_run["isRun"] = self.table.cell_value(self.get_row_number(case_id),Variable.IsRun)
        # 合并所有字典
        one_row_data = {**case_id_dict,**case_name_dict,**test_data_dict,**expectation_dict,**is_run}
        return one_row_data

    def get_ddt_data(self,id_list):
        """
        使用ddt模块测试的数据类型必须是列表套字典
        :param Id_list: 用例id 的列表
        """
        # 定义空列表初始化ddt数据
        ddt_data = []
        for case_id in id_list:
            one_row_data = self.get_dict_data(case_id)
            # 把每个字典添加到列表中
            ddt_data.append(one_row_data)
        return ddt_data

class Write_Excel:

    @staticmethod
    def write_result(sheet_name,result,case_id):
        """写入测试结果"""

        # 读取 excel 表格
        excel_data = xlrd.open_workbook(testExcelPath, formatting_info=True)
        table = excel_data.sheet_by_name(sheet_name)
        # 复制原来excel表格
        copy_excel = copy(excel_data)
        # 获取table页
        ws = copy_excel.get_sheet(sheet_name)
        # 日期
        date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        # 设置结果字段样式
        result_txt = str(date) + " -> " + result
        # 初始化一个样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        # 设置颜色
        if result == "测试通过":
            font.colour_index = 3
        else:
            font.colour_index = 2
        # 添加样式字体颜色
        style.font = font
        # 写入测试结果,行、列、结果、样式
        ws.write(table.col_values(0).index(case_id),Variable.Result,result_txt,style)
        # 保存结果
        copy_excel.save(testExcelPath)

class Update_Excel:

    @staticmethod
    def update_test_data(sheet_name,case_id,dict_data):
        """
        修改excel中测试数据的信息一般修改值
        :param dict_data: 传入字典格式
        """

        # 判断 dict_data 传入的数据类型必须是字典格式
        if type(dict_data).__name__ != "dict":
            raise TypeError(" {0} is not a dict type ! ".format(dict_data))
        read = Read_Excel(sheet_name)
        # 读取 excel 表格
        excel_data = xlrd.open_workbook(testExcelPath, formatting_info=True)
        table = excel_data.sheet_by_name(sheet_name)
        # 获取测试数据是一个字典
        test_data = read.get_test_data(case_id)
        # 字典合并重复的key会重新赋值
        new_data = {**test_data,**dict_data}
        # 字典转化为字符串,字符串里用单引号来标识字符,要不读取报错
        write_data = str(new_data).replace("'",'"')
        # 写入测试数据
        work_book = copy(excel_data)
        ws = work_book.get_sheet(sheet_name)
        # 初始化一个样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        # 写入的数据字体都为蓝色
        font.colour_index = 12
        style.font = font
        ws.write(table.col_values(0).index(case_id),Variable.TestData,write_data,style)
        # 保存文档
        work_book.save(testExcelPath)

    @staticmethod
    def update_expect_data(sheet_name,case_id,write_data):
        """设置期望值字段"""

        # 读取 excel 表格
        excel_data = xlrd.open_workbook(testExcelPath, formatting_info=True)
        table = excel_data.sheet_by_name(sheet_name)
        # 写入测试数据
        work_book = copy(excel_data)
        ws = work_book.get_sheet(sheet_name)
        ws.write(table.col_values(0).index(case_id),Variable.Expectation,str(write_data))
        # 保存文档
        work_book.save(testExcelPath)
