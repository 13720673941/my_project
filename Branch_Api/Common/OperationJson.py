# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import json
from Common import Public
from Common.OperationExcel import operationExcel
from Common.OperationConfig import operationConfig

'''
对header中的数据进行分离，放到json文件中去，获取json文件中的值信息,也就是读取请求里面的body数据的函数
'''

class operationJson:

    def __init__(self):

        self.operationexcel = operationExcel()
        self.operationconfig = operationConfig()

    def readjson(self):

        '''读取json文件中的数据信息-->读取时字符串类型->反序列化转化为字典类型格式'''
        with open(Public.data_dir("Data","RequestData.json"),encoding="utf-8") as f:
            data = json.load(f)
            return data

    def updataJson(self,row):

        '''json数据中的token和apitoken的自动关联'''
        jsonData = self.readjson()[self.operationexcel.getBody(row=row)]
        #遍历循环字典中的key值，设置jsondata中的value值关联BaseConfig.ini中的公共参数
        token = self.operationconfig.readConfig(section="Globals",option="token")
        api_token = self.operationconfig.readConfig(section="Globals",option="apitoken")
        #遍历json数据
        for k,v in jsonData.items():
            #遍历字典网点信息数据里面的value值替换动态参数
            if k == "UserInfo":
                v["access_token"]=token
                v["api_Token"]=api_token
        return jsonData

    def get_jsonData(self,row):

        '''获取json文件字典格式,以excel中的body值信息为KEY值进行获取json文件中的value值信息'''
        #对请求的数据类型进行判断序列化或者反序列化
        if self.operationexcel.getContentType(row).lower() == "json":
            return json.dumps(self.updataJson(row))
        elif self.operationexcel.getContentType(row).lower() == "form":
            return self.updataJson(row)
        else:
            print("!!!!!数据格式类型不对不是json or form")





#
# a=operationJson().get_jsonData(40)
# b = a["params"].replace("{status}","AAAA",1)
# print(b)

