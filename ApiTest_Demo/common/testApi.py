# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:37

"""
    requests 库中的方法的二次封装
"""

from common.getTestCase import ReadTestCase
from common.logConfig import Log
from common.operateFile import OperateFile
import requests

class Request():

    def __init__(self):
        self.log = Log()
        self.readCase = ReadTestCase()
        self.readFile = OperateFile()

    def get_url(self,caseId):
        """拼接url"""
        # host地址读取
        host = self.readFile.read_config("HTTP","HOST")
        url = self.readCase.get_url(caseId)
        return host+url

    def request(self,url,method,**kwargs):
        """封装请求方法"""

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


if __name__ == '__main__':

    r = Request()
    e = r.get_url(caseId="login_001")
    print(e)

