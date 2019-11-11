# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/6 11:37

from common import filePath
from common.operateExcel import OperateExcel
import json

class OperateJson():

    """
    获取json请求数据
    """

    def __init__(self):

        # 实例化类
        self.operate_excel = OperateExcel()

    def read_json(self):

        # 加载读取所有json文件
        with open(filePath.requestData_path,encoding="utf-8") as f:
            # 返回一个字典格式的数据类型
            return json.load(f)

    def get_request_data(self,id):
        """获取对应的请求数据"""

        # 获取excel中body关联json文件的字段
        json_key = self.operate_excel.get_body(id)
        # 获取全部json文件
        json_data = self.read_json()
        if json_key in json_data.keys():
            # 序列化value值
            return json_data[json_key]
        else:
            return "Error: " + '"'+json_key+'"' + " not in json data of keys."






# a = OperateJson().get_request_data("login_001")
#
# print(a)



