# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 17:49

import xlrd,xlwt
from xlutils.copy import copy

# 读取 excel 表格
filePath = "test001.xlsx"

# 读取excel文件 formatting_info: 复制样式
work_book = xlrd.open_workbook(filePath,formatting_info=True)
# 复制原来excel表格
copy_excel = copy(work_book)
# 获取table页
ws = copy_excel.get_sheet("Sheet1")
# 写入字段
ws.write(2,1,"王思聪")

# 实例化样式
style = xlwt.XFStyle()
font = xlwt.Font()
font.colour_index = 2
style.font = font

# 写入 坐标 字段 样式
ws.write(3,1,"李丝丝",style)
# 保存覆盖原文件
copy_excel.save(filePath)

