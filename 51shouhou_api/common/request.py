# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/6 14:33

from common.operateExcel import OperateExcel
from common.operateJson import OperateJson
from common.operateConfig import OperateConfig
import requests,json

class Requests():

    """
    requests 模块的二次封装
    """

    def __init__(self,id):

        # 初始化变量
        self.id = id
        # 实例化类
        self.operate_excel = OperateExcel()
        self.operate_json = OperateJson()
        self.operate_config = OperateConfig()

    def headers(self):
        """定义请求头格式信息"""

        # 获取excel表格中header的字段
        excel_headers = self.operate_excel.get_headers(self.id)
        if excel_headers == "":
            headers = None
        else:
            # 读取的字符串转化为字典格式
            headers = json.loads(excel_headers)
            # 判断需要加入请求头的参数
            if "Authorization" in excel_headers:
                # 替换最新写入的token
                headers["Authorization"] = self.operate_config.read_config_data("headers","token")


        return headers

    def test_api(self):
        """requests模块请求类型封装"""

        # 获取excel中的请求类型
        request_type = self.operate_excel.get_method(self.id)
        # 判断请求类型
        if request_type.lower() == "get":
            try:
                response = requests.get(url=self.operate_excel.get_url(self.id),
                                        headers=None,
                                        params=None
                                        )
                return response
            except:
                return "Error: Api test get request error ! "
        elif request_type.lower() == "post":
            try:
                response = requests.post(url=self.operate_excel.get_url(self.id),
                                         headers=None,
                                         json=self.operate_json.get_request_data(self.id)
                                         )
                return response
            except:
                return "Error: Api test post request error ! "
        else:
            return "Error: Request type error, not have: "+request_type+" type. "






response = Requests("login_001").headers()

print(response)





