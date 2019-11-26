# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/6 14:33

from common.operateExcel import OperateExcel
from common.operateJson import OperateJson
from common.operateConfig import OperateConfig
from common.logConfig import Log
import requests,json

class Requests():

    """
    requests 模块的二次封装
    """

    def __init__(self,sheet):

        # 实例化类
        self.operate_excel = OperateExcel(sheet)
        self.operate_json = OperateJson(sheet)
        self.operate_config = OperateConfig()
        self.log = Log()

    def headers(self,id):
        """
        定义请求头格式信息
        """

        # 获取excel表格中header的字段
        excel_headers = self.operate_excel.get_headers(id)
        if excel_headers == "":
            headers = None
        else:
            # 读取的字符串转化为字典格式
            headers = json.loads(excel_headers)
            # 获取token值
            token = self.operate_config.read_config_data("headers","token")
            # 判断需要加入请求头的参数
            if "Authorization" in excel_headers:
                # 替换最新写入的token
                headers["Authorization"] = "Bearer "+token

        return headers

    def test_api(self,id):
        """
        requests模块请求类型封装
        """

        # 获取excel中的请求类型
        request_type = self.operate_excel.get_method(id)
        # 判断请求类型
        if request_type.lower() == "get":
            try:
                response = requests.get(url=self.operate_excel.get_url(id),
                                        headers=self.headers(id),
                                        params=self.operate_json.get_request_data(id),
                                        timeout=5
                                        )
                return response
            except:
                return "Error: Api test get request error ! "

        elif request_type.lower() == "post":
            try:
                # 获取excel表格中header的字段
                excel_headers = self.operate_excel.get_headers(id)
                # 读取的字符串转化为字典格式
                headers = json.loads(excel_headers)
                # 初始化response为空
                if headers["Content-Type"] == "application/json":
                    response = requests.post(url=self.operate_excel.get_url(id),
                                             headers=self.headers(id),
                                             json=self.operate_json.get_request_data(id),
                                             timeout = 5
                                             )
                    return response
                elif headers["Content-Type"] == "application/x-www-form":
                    response = requests.post(url=self.operate_excel.get_url(id),
                                             headers=self.headers(id),
                                             data=self.operate_json.get_request_data(id),
                                             timeout = 5
                                             )
                    return response
                else:
                    return "Error: Content Type is None"

            except:
                return "Error: Api test post request error ! "
        else:
            return "Error: Request type error, not have: "+request_type+" type. "

    def is_content(self,id,response):
        """
        返回请求数据的断言包括：协议状态码断言、接口状态码断言、关键字断言
        :return:
        """
        # 获取用力名称
        self.log.info("-------------------------")
        self.log.info("Case name: "+self.operate_excel.get_case(id))
        # 初始化变量
        number = 0
        # 协议码断言获取文档中期望的协议码
        http_code = self.operate_excel.get_httpCode(id)
        # 判断返回的协议状态码
        response_http_code = response.status_code
        if response_http_code == http_code:
            number += 1
            self.log.info(".....Http code: success.")
        else:
            self.log.info("!!!!!Http code: fail."+"\nFail reason: {0}".format(response_http_code))
        # 获取文档中的业务状态码
        api_code = self.operate_excel.get_responseCode(id)
        # 获取接口返回的文本信息为字符串
        response_text = response.text
        if api_code in response_text:
            number += 1
            self.log.info(".....Response code: success.")
        else:
            self.log.info("!!!!!Response code: fail."+"\nFail reason: {0}".format(response_text))
        # 获取期望字段
        key_word = self.operate_excel.get_exception(id)
        # 返回关键字校验
        if key_word in response_text:
            number += 1
            self.log.info(".....Expect word: success.")
        else:
            self.log.info("!!!!!Expect word: fail."+"\nFail reason: {0}".format(response_text))

        # 写入测试结果判断三个是否全部判断成功了
        if number == 3:
            # 写入成功
            self.operate_excel.write_result("PASS",id)
        else:
            # 测试失败
            self.operate_excel.write_result("FAIL",id)

    def test_main(self,id):

        # 调用测试接口
        response = self.test_api(id)
        # 断言
        self.is_content(id,response)




