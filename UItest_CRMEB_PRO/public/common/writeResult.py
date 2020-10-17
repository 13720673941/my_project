# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/23 13:38

"""
测试结果写入 UItest_data.xlsx文件中
"""

from xlutils.copy import copy
from config.pathConfig import *
from public.common.getTestData import Varible,GetTestData
import xlwt,xlrd,datetime


class WriteResult():

    def __init__(self):
        # 读取excel文件数据
        self.workBook = xlrd.open_workbook(filename=TEST_DATA_PATH,formatting_info=True)
        self.table = self.workBook.sheet_by_index(0)
        self.getData = GetTestData()

    def write_result(self,result,id):
        """写入测试用例结果"""

        # 复制excel表格
        copyExcel = copy(self.workBook)
        # 获取表格
        copyTable = copyExcel.get_sheet("Sheet1")
        # 设置写入字段样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        # 设置字段颜色
        if result.lower() == "pass":
            font.colour_index = 3
        elif result.lower() == "fail":
            font.colour_index = 2
        else:
            raise NameError("测试结果传入字段不正确，允许字段：pass、fail .")
        # 添加样式
        style.font = font
        # 获取当前时间
        resultText = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" -> "+result
        # 写入测试结果
        copyTable.write(self.getData.get_row(id),Varible.Result,resultText,style)
        # 保存原文件路径覆盖原文件
        copyExcel.save(TEST_DATA_PATH)



if __name__ == '__main__':

    write = WriteResult()
    write.write_result("fail","login001")