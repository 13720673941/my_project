# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/5 11:56

from common import variable
from common import filePath
from xlutils.copy import copy
import xlrd,datetime,xlwt

class OperateExcel():

    """
    获取excel单元格中的数据，使用对应的行列获取对应数据
    """

    def __init__(self,Sheet):

        # 读取数据excel文档# 参数说明: formatting_info=True 保留原excel格式
        self.excel = xlrd.open_workbook(filePath.branchApi_path,formatting_info=True)
        # 读取表格
        self.table = self.excel.sheet_by_name(Sheet)

    def get_row_number(self,id):
        """获取excel中数据行数,以id为索引返回行数"""

        first_col_info = self.table.col_values(variable.get_col_id())
        # 返回行数
        return first_col_info.index(id)

    def get_id(self,id):
        """获取id信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_id())

    def get_case(self,id):
        """获取case信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_case())

    def get_url(self,id):
        """获取url信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_url())

    def get_method(self,id):
        """获取method信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_method())

    def get_headers(self,id):
        """获取headers信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_headers())

    def get_body(self,id):
        """获取body信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_body())

    def get_httpCode(self,id):
        """获取httpCode信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_httpCode())

    def get_responseCode(self,id):
        """获取responseCode信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_responseCode())

    def get_exception(self,id):
        """获取exception信息"""

        return self.table.cell_value(self.get_row_number(id),variable.get_col_exception())

    def write_result(self,result,id):
        """写入测试结果"""

        # 复制表格
        workbook = copy(self.excel)
        ws = workbook.get_sheet(0)
        # 日期
        date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        # 设置结果字段样式
        result_txt = str(date) + " -> " + result
        # 设置颜色
        if result == "PASS":
            style_colour = xlwt.easyxf('pattern: pattern solid, fore_colour green;')
        else:
            style_colour = xlwt.easyxf('pattern: pattern solid, fore_colour red;')
        # 写入测试结果,行、列、结果、样式
        ws.write(self.get_row_number(id),variable.get_col_result(),result_txt,style_colour)
        # 保存结果
        workbook.save(filePath.branchApi_path)



# import requests
#
# a = OperateExcel(id_name="login_001")
# a.write_result(result="PASS")
# a = OperateExcel(id_name="login_002")
# a.write_result(result="PASS")
