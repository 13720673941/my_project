# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:22

"""
解析excel测试数据文件，获取文件中测试数据信息
"""

from config.filePathConfig import FilePathConfig
from util.logConfig import Logger
from config.varConfig import ExcelVariable as EV

import xlrd

Log = Logger().origin_log


class ParseExcel:

    def __init__(self, sheetName):
        self.sheetName = sheetName
        self.workBook = xlrd.open_workbook(
            filename=FilePathConfig.TEST_CASE_EXCEL_PATH, formatting_info=True)
        Log.info("打开excel数据: {} ...".format(FilePathConfig.TEST_CASE_EXCEL_PATH[:50]))
        self.sheetTable = self.workBook.sheet_by_name(sheetName)
        Log.info("读取表格: {} 数据".format(sheetName))

    # def get_sheet(self, sheetName):
    #     """
    #     获取excel表格
    #     :param sheetName: 表名称
    #     :return: 返回表格
    #     """
    #     self.sheetTable = self.workBook.sheet_by_name(sheetName)
    #     Log.info("读取表格: {} 数据".format(sheetName))
    #     return self.sheetTable

    def get_rows(self) -> int:
        """
        获取表格所有行数
        :return: 表总行数
        """
        return self.sheetTable.nrows

    def get_cols(self) -> int:
        """
        获取表格所有的列数量
        :return: 表总列数
        """
        return self.sheetTable.ncols

    def case_index(self, caseNumber) -> int:
        """
        获取用例索引值
        :param caseName: 用例名称
        :return: 用例行数索引
        """
        # 获取全部用户名称列表
        allCaseName = self.sheetTable.col_values(EV.testCaseNum)
        if caseNumber not in allCaseName:
            raise NameError("表格: {} 中没有找到该用例名称: {} ".format(self.sheetName, caseNumber))
        return allCaseName.index(caseNumber)

    def get_case_name(self, caseNumber):
        """
        获取用例编号
        :param caseName:
        :return: 用例名称
        """
        caseName = self.sheetTable.cell_value(self.case_index(caseNumber), EV.caseDescription)
        Log.info("用例编号: {} 名称: 【{}】 ".format(caseNumber, caseName))

    def get_case_run(self, caseNumber):
        """获取用例是否执行"""
        caseIsRun = self.sheetTable.cell_value(self.case_index(caseNumber), EV.isRun)
        Log.info("用例是否执行字段: {} ".format(caseIsRun))
        return caseIsRun

    def get_step_list(self) -> list:
        """
        获取操作步骤表格所有数据，以键值对的格式添加到列表中
        :return:
        """
        stepListData = []
        for stepRowNum in range(1, self.get_rows()):
            dictData = {}
            for stepColNum in range(self.get_cols()-1): # 最后步骤执行结果不添加到数据中 -1
                keyName = self.sheetTable.cell_value(EV.systemNum, stepColNum)
                dictData[keyName] = self.sheetTable.cell_value(stepRowNum, stepColNum)
            stepListData.append(dictData)
        Log.info("表格: {} 数据解析成功, 测试数据: {} ...".format(self.sheetName, str(stepListData)[:50]))
        return stepListData


if __name__ == '__main__':
    p = ParseExcel(sheetName="duo_merchant_login")
    a = p.get_step_list()
    print(a)