# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:37

"""
    requests 库中的方法的二次封装
"""

from common.getTestCase import ReadTestCase
from common.logConfig import Log
from config.configVar import *
import requests

class Request():

    def __init__(self):
        self.log = Log()
        self.readCase = ReadTestCase()

    def request(self,caseId,**kwargs):
        """封装请求方法"""

        # 获取初始化参数
        url = HttpConfig.HOST + self.readCase.get_url(caseId)
        method = self.readCase.get_method(caseId)
        # 初始化请求结果
        res = None
        try:
            if method == "get":
                res = requests.get(url=url,**kwargs)
            elif method == "post":
                res = requests.post(url=url,**kwargs)
            elif method == "put":
                res = requests.put(url=url,**kwargs)
            elif method == "delete":
                res = requests.delete(url=url,**kwargs)
            else:
                raise NameError("请求类型传入有误！允许类型：get、post、put、delete ")
        except Exception as e:
            self.log.error("请求报错：{}".format(e))
            raise
        finally:
            return res

    def result(self,resp):
        """判断返回结果"""
        res = {}
        # 获取协议状态码
        httpCode = resp.status_code
        res["httpCode"] = httpCode
        responseData = resp.json()
        # 拼接成一个字典
        return {**res,**responseData}

if __name__ == '__main__':

    from common.operateFile import OperateFile
    getCase = ReadTestCase()
    getYaml = OperateFile()
    req = Request()
    data = getYaml.read_yaml()["login_001"]
    res = req.request(caseId="login_001",json=data)
    print(req.result(res))



