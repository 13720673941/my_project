# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/20 18:37

"""
    读取测试数据 excel 中的所有数据信息
"""

from config.pathConfig import *
import xlrd,json

class Varible:
    """
    excel测试数据表格中所有字段的索引
    """
    Id = 0
    CaseName = 1
    TestData = 2
    Expectation = 3
    Result = 4
    IsRun = 5

class GetTestData:
    """
    获取各个表格的数据
    """

    def __init__(self):
        # 读取测试数据保存文件保持原格式
        workBook = xlrd.open_workbook(filename=TEST_DATA_PATH)
        self.table = workBook.sheet_by_index(0)

    def get_row(self,id):
        """获取测试用例的行索引号"""

        # 获取测试数据中的全部
        idList = self.table.col_values(Varible.Id)
        # 判断id是否存在列表中
        if id not in idList:
            raise NameError("用例编号：{} 不存在列表中！".format(id))
        else:
            return idList.index(id)

    def get_name(self,id):
        """获取测试数据中"""
        return self.table.cell_value(self.get_row(id),Varible.CaseName)

    def get_data(self,id):
        """获取测试数据"""
        return json.loads(self.table.cell_value(self.get_row(id),Varible.TestData))

    def get_expectation(self,id):
        """获取期望值"""
        return self.table.cell_value(self.get_row(id),Varible.Expectation)

    def get_is_run(self,id):
        """获取是否执行该用例字段"""
        isRun = self.table.cell_value(self.get_row(id),Varible.IsRun)
        if isRun.lower() == "yes":
            flag = True
        else:
            flag = False
        return {"isRun":flag}

    def get_dict_data(self,id):
        """组合数据: 测试数据字段全部组合字段格式方便使用"""

        # 初始化字典
        dictData = dict()
        # 添加测试数据
        dictData["caseId"] = id
        dictData["caseName"] = self.get_name(id)
        dictData["testData"] = self.get_data(id)
        dictData["expectation"] = self.get_expectation(id)
        # 返回字段格式数据
        return {**dictData,**self.get_is_run(id)}


if __name__ == '__main__':

    data = GetTestData().get_dict_data("login_001")
    print(data)