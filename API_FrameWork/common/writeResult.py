# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 19:28

"""
    测试结果写入excel中
"""

from config.pathConfig import *
from common.getTestCase import Varible
from xlutils.copy import copy
import xlwt,xlrd,datetime

class WriteResult():

    def write_result(self,caseId,status):
        """
        :param caseId: 用例编号信息
        :param status: 断言结果的状态码，三层断言通过返回都是 0 ，大于 0 就是有一个断言失败
        :return:
        """
        # 复制excel表格
        workBook = xlrd.open_workbook(TEST_CASE_PATH,formatting_info=True)
        table = workBook.sheet_by_name("apiTest")
        # 复制表格
        copyBook = copy(workBook)
        copyTable = copyBook.get_sheet("apiTest")
        # 写入字体颜色样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        style.font = font
        # 获取时间字符串
        timeStr = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if status == 0:
            font.colour_index = 3
            result = timeStr + " -> PASS"
        else:
            font.colour_index = 2
            result = timeStr + " -> FAIL"
        # 获取用例行数
        rowNum = table.col_values(Varible.CaseId).index(caseId)
        # 写入测试结果,字体颜色
        copyTable.write(rowNum,Varible.Result,result,style)
        # 保存结果
        copyBook.save(TEST_CASE_PATH)


if __name__ == '__main__':

    w = WriteResult()
    w.write_result("login_001",1)
