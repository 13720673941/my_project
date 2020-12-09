# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:22

"""
解析excel测试数据文件，获取文件中测试数据信息
"""

import xlrd
from config.fileConfig import *
from config.varConfig import CaseVariable


class ParseExcel:

    def __init__(self):
        self.workBook = xlrd.open_workbook(filename=TEST_CASE_EXCEL_PATH)

