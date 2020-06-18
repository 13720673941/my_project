# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 19:28

"""
    测试结果写入excel中
"""

from config.pathConfig import *
from common.getTestCase import Varible
from common.logConfig import Log
from xlutils.copy import copy
import xlwt,xlrd

class WriteResult():

    def __init__(self):
        # 实例化类
        self.log = Log()
        self.var = Varible()

    def write_result(self,caseId,result):
        """测试结果写入excel中"""
        workBook = xlrd.open_workbook(TEST_CASE_PATH,formatting_info=True)
        # 复制excel
        copyBook = copy(workBook)
        # 打开表格
        copyTable = copyBook.get_sheet("apiTest")
        # 获取用例id在列表中的行号
        caseRowNum = copyTable.col_values(self.var.CaseId).index(caseId)
        print(caseRowNum)
        # 写入结果
        copyTable.write(caseRowNum,self.var.Result,result)
        ws.save(TEST_CASE_PATH)

if __name__ == '__main__':

    w = WriteResult()
    w.write_result("login_001","PASS")
