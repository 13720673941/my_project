# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 17:34

"""
    excel 文件内容的读取
"""

import xlrd

filePath = "test001.xlsx"

# 读取excel文件
work_book = xlrd.open_workbook(filePath)
# 读取表格
sheet_table = work_book.sheet_by_index(0)

# 读取行列固定字段
print("第一行第一列数据：",sheet_table.cell_value(1,1))
# 读取全部列/行字段
print("整第一列数据：",sheet_table.col_values(0))
print("整第一行数据：",sheet_table.row_values(0))
# 获取总列数/行数
print("总行数：",sheet_table.nrows)
print("总列数：",sheet_table.ncols)