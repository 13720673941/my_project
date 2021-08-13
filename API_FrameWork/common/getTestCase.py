# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:36

"""
    读取测试用例excel中的数据
"""
from config.pathConfig import *
from xlutils.copy import copy
import xlrd,xlwt

class Varible:
    """测试用例excel中所有变量的索引值"""
    CaseId = 0
    CaseName = 1
    Url = 2
    Method = 3
    Header = 4
    RequestData = 5
    HttpCode = 6
    ServiceCode = 7
    ResponseValue = 8
    IsRun = 9
    Result = 10

class ReadTestCase:
    """读取用例excel中的所有测试数据"""

    def __init__(self):
        self.workBook = xlrd.open_workbook(TEST_CASE_PATH)
        self.workTable = self.workBook.sheet_by_name("apiTest")

    def get_case_row(self,caseId):
        """获取测试用例所在的行数"""
        firstColList = self.workTable.col_values(Varible.CaseId)
        if caseId not in firstColList:
            raise NameError("用例id: {} 不在apiTestCase.xlsx文件中！！！".format(caseId))
        return firstColList.index(caseId)

    def get_case_name(self,caseId):
        """获取测试用例名称"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.CaseName)

    def get_url(self,caseId):
        """获取请求地址"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.Url)

    def get_method(self,caseId):
        """获取请求方式"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.Method)

    def get_headers(self,caseId):
        """获取请求头信息"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.Header)

    def get_data(self,caseId):
        """获取请求参数"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.RequestData)

    def get_http_code(self,caseId):
        """获取协议状态码"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.HttpCode)

    def get_service_code(self,caseId):
        """获取业务状态吗"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.ServiceCode)

    def get_response_value(self,caseId):
        """获取返回值"""
        return self.workTable.cell_value(self.get_case_row(caseId),Varible.ResponseValue)

    def get_is_run(self,caseId):
        """获取返回值并加工返回bool变量"""
        text = self.workTable.cell_value(self.get_case_row(caseId),Varible.IsRun)
        if text.lower() == "yes":
            return True
        elif text.lower() == "no":
            return False
        else:
            raise NameError("测试用例表格中isRun参数错误！允许字段：yes、no ")


if __name__ == '__main__':

    r = ReadTestCase()
    print(r.get_method("login_001"))


