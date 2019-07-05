# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import xlrd,time,json
from Common import Variable
from Common.Public import data_dir
from xlutils.copy import copy

'''
获取Excel表格中的数据信息
'''

class operationExcel(object):

    def __init__(self):
        '''获取excel文件路径'''
        self.excel = xlrd.open_workbook(data_dir(filename="BranchApi.xls"))
        self.table = self.excel.sheet_by_name("Sheet1")

    def getRows(self):
        '''获取总行数'''
        return self.table.nrows

    def get_row_col(self,row,col):
        '''获取单元格内容'''
        return self.table.cell_value(row,col)

    def getId(self,row):
        '''获取用例ID'''
        return self.table.cell_value(row,Variable.get_id())

    def getCase(self,row):
        '''获取用例名称信息'''
        return self.table.cell_value(row,Variable.get_case())

    def getUrl(self,row):
        '''获取测试地址信息'''
        return self.table.cell_value(row,Variable.get_url())

    def getMethod(self,row):
        '''获取请求方式'''
        return self.table.cell_value(row,Variable.get_method())

    def getHeader(self,row):
        '''获取请求头信息读取是字符串，-->>后面关联读取json文件的key值'''
        return self.table.cell_value(row,Variable.get_headers())

    def getBody(self,row):
        '''获取请求参数'''
        return self.table.cell_value(row,Variable.get_body())

    def getHttpCode(self,row):
        '''获取协议状态码'''
        return int(self.table.cell_value(row,Variable.get_httpcode()))

    def getResponseCode(self,row):
        '''获取业务状态码'''
        return self.table.cell_value(row,Variable.get_responsecode())

    def getException(self,row):
        '''获取期望结果'''
        return self.table.cell_value(row,Variable.get_Exception())

    def getResult(self,row):
        '''获取实际结果'''
        return self.table.cell_value(row,Variable.get_Result())

    def getContentType(self,row):
        '''获取数据类型'''
        return self.table.cell_value(row,Variable.get_ContentType())

#
# a = operationExcel()
# print(a.getException(2))