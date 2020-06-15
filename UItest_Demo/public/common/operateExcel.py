# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 19:24

from config.pathConfig import *
from xlutils.copy import copy
import xlrd,json,xlwt,datetime

"""
    读取excel测试数据,写入测试结果到excel中
"""

class Variable():

    # excel中每列数据对应的索引
    Id = 0
    CaseName = 1
    TestData = 2
    Expectation = 3
    Result = 4
    IsRun = 5

class ReadTestCase():

    def __init__(self):
        self.workBook = xlrd.open_workbook(filename=testExcelPath)
        self.sheetTable = self.workBook.sheet_by_name("Sheet1")

    def get_row_index(self,caseId):
        """获取id的索引"""

        # 获取所有id字段列表
        allIdList = self.sheetTable.col_values(Variable.Id)
        # 判断是否存在
        if caseId not in allIdList:
            raise TypeError("用户编号：{} 不存在！".format(caseId))
        else:
            idIndex = allIdList.index(caseId)
        return idIndex

    def get_case_name(self,caseId):
        """获取用例名称"""
        return self.sheetTable.cell(self.get_row_index(caseId),Variable.CaseName).value

    def get_test_data(self,caseId):
        """获取测试数据"""

        # 读取测试数据为字符串类型
        strData = self.sheetTable.cell(self.get_row_index(caseId),Variable.TestData).value
        try:
            # 转化为字典类型
            jsonData = json.loads(strData)
        except:
            raise TypeError("用户编号为：{} 的 TestData 数据格式有误！必须是字典格式的字符串".format(caseId))
        return jsonData

    def get_expect_data(self,caseId):
        """获取用例期望值"""
        return self.sheetTable.cell(self.get_row_index(caseId),Variable.Expectation).value

    def get_run_data(self,caseId):
        """获取是否执行用例字段"""
        isRunTxt = self.sheetTable.cell(self.get_row_index(caseId),Variable.IsRun).value
        # @unittest.skipUnless 中condition参数为False跳过用例
        if isRunTxt.lower() == "no":
            flag = False
        elif isRunTxt.lower() == "yes":
            flag = True
        else:
            raise TypeError("用户编号为：{} 的 ‘ IsRun ’ 字段有误！允许类型：yes、no ".format(caseId))
        return flag

    def get_all_data(self,caseId):
        """组合所有测试数据,全部数据放到一个字典中固定键值方便调用"""

        allTestData = {}
        allTestData["CaseId"] = caseId
        allTestData["CaseName"] = self.get_case_name(caseId)
        allTestData["Expectation"] = self.get_expect_data(caseId)
        allTestData["IsRun"] = self.get_run_data(caseId)
        # 返回所有测试数据字典类型
        return {**allTestData,**self.get_test_data(caseId)}

    def get_ddt_data(self,caseId):
        """
        :param caseId: 所有需要组合ddt类型数据的用例id
        :return:
        """
        if type(caseId).__name__ != "list":
            raise TypeError("ddt 类型的测试数据组合，传入的caseId必须是列表 ！")
        # 组合 ddt 类型的测试数据添加到元组中
        ddtData = []
        for id in caseId:
            ddtData.append(self.get_all_data(id))
        return ddtData

class WriteResult:

    def write_result(self,result,caseId):
        """
        :param result: 测试结果字段一般之允许传入 pass fail
        :param caseId: 需要写入结果的用例编号
        :return:
        """

        # 读取测试数据
        workBook = xlrd.open_workbook(testExcelPath,formatting_info=True) # formatting_info 复制样式
        table = workBook.sheet_by_name("Sheet1")
        # 复制excel
        copyExcel = copy(workBook)
        # 获取表格
        copyTable = copyExcel.get_sheet("Sheet1")
        # 实例化样式
        style = xlwt.XFStyle()
        font = xlwt.Font()
        # 设置写入字体颜色
        if result.lower() == "pass":
            font.colour_index = 3
        elif result.lower() == "fail":
            font.colour_index = 2
        else:
            raise TypeError("测试结果传入字段有误！允许字段：pass 、fail 不计大小写。")
        # 添加样式
        style.font = font
        # 设置写入结果字段
        resultTxt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "->" + result
        # 写入测试结果
        copyTable.write(table.col_values(Variable.Id).index(caseId),Variable.Result,resultTxt,style)
        # 保存文件
        copyExcel.save(testExcelPath)



# if __name__ == '__main__':
#
#     read = ReadTestCase()
#     a = read.get_ddt_data(caseId=["baidu_search_001","baidu_search_002"])
#     print(a)
