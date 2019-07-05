# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import requests,time,json,logging
from Common.OperationExcel import operationExcel
from Common.OperationConfig import operationConfig
from Common.OperationJson import operationJson
from Common.WriteResult import write_to_Excel

'''
1、对api头部信息的处理
2、对requests模块的二次封装
3、对api输出内容的格式,返回信息的判断api是否执行成功
'''

class Method:

    def __init__(self):
        '''读取文件的类进行实例化'''
        self.operatexcel = operationExcel()
        self.operatjson = operationJson()
        self.operatconfig = operationConfig()

    def apiUrl(self,row):
        '''读取配置文件中url中的公用部分信息'''
        readUrl = self.operatexcel.getUrl(row)
        url1 = self.operatconfig.readConfig("BaseUrl", "url_1")
        url2 = self.operatconfig.readConfig("BaseUrl", "url_2")
        url3 = self.operatconfig.readConfig("BaseUrl", "url_3")
        if "http://" in readUrl:
            Url = readUrl
        elif "Url1" in readUrl:
            Url = readUrl.replace("Url1",url1,1)
        elif "Url2" in readUrl:
            Url = readUrl.replace("Url2",url2,1)
        elif "Url3" in readUrl:
            Url = readUrl.replace("Url3",url3,1)
        else:
            pass
        return Url

    def apiHeaders(self,row):
        '''读取接口的请求头部公共信息'''
        token = self.operatconfig.readConfig("Globals", "token")
        apiToken = self.operatconfig.readConfig("Globals", "apitoken")
        PkId = self.operatconfig.readConfig("Globals", "pkid")
        #没有需要到的请求头信息的api
        if self.operatexcel.getHeader(row) == "":
            #没有请求有数据传入公共数据
            Headers = {
                "Origin":"http://www.51shouhou.cn",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
            }
        #需要标签的api同事需要apitoken和pkid
        elif "sign" in self.operatexcel.getHeader(row):
            #字符串转化为字典
            dict = json.loads(self.operatexcel.getHeader(row))
            #遍历读取的EXCEL中字典的value值信息添加到下面字典中
            for value in dict.values():
                Headers = {
                    "ApiToken":apiToken,
                    "PkId":PkId,
                    "sign":value
                }
        elif self.operatexcel.getHeader(row) == "ApiToken":
            Headers = {
                "ApiToken": apiToken,
                "PkId": PkId
            }
        #值需要token的api
        elif self.operatexcel.getHeader(row) == "Authorization":
            Headers = {
                "Authorization":"Bearer " + token
            }

        return Headers

    def testApi(self,row):
        '''对request模块的二次封装'''
        #默认执行失败
        self.success="Fail"
        #读取excel中的method字段信息
        method = self.operatexcel.getMethod(row)
        global r
        #POST请求封装
        if method.lower() == "post":
            #对请求的参数实例
            try:
                r = requests.post(url=self.apiUrl(row),
                                  data=self.operatjson.get_jsonData(row),
                                  headers=self.apiHeaders(row),
                                  timeout=8
                                  )
            except Exception as e:
                logging.error("!!!!!接口发生未知错误：%s"%e)
                #raise RuntimeError("接口发生未知错误！")
        #GET请求封装
        elif method.lower() == "get":
            try:
                if self.operatexcel.getBody(row)=="":
                    #请求数据为空
                    r = requests.get(url=self.apiUrl(row),
                                     headers=self.apiHeaders(row),
                                     timeout=8
                                     )
                else:
                    r = requests.get(url=self.apiUrl(row),
                                     param=self.operatjson.get_jsonData(row),
                                     headers=self.apiHeaders(row),
                                     timeout=8
                                     )
            except Exception as e:
                logging.info("接口发生未知错误：%s"%e)

        else:
            logging.error("!!!!!接口发生未知错误：%s"%method)
        return r

    def test_Api(self,row,data):
        '''再次封装post请求特殊赋值处理的请求调用'''
        #默认执行失败
        self.success = "Fail"
        #读取excel中的method字段信息
        method = self.operatexcel.getMethod(row)
        if method.lower() == "post":
            try:
                r = requests.post(url=self.apiUrl(row),
                                  data=data,
                                  headers=self.apiHeaders(row),
                                  timeout=8
                                  )
            except Exception as e:
                logging.error("!!!!!接口发生未知错误：%s"%e)
        elif method.lower() == "get":
            try:
                r = requests.get(url=self.apiUrl(row),
                                 param=data,
                                 headers=self.apiHeaders(row),
                                 timeout=8
                                 )
            except Exception as e:
                logging.info("接口发生未知错误：%s" % e)

        else:
            logging.error("!!!!!接口发生未知错误：%s" % method)
        return r

    def isContent(self,r,row,isWrite):
        '''api执行结果的判断，包括：协议状态码、业务状态码、返回信息'''
        logging.info("-------------------------分割线---------------------------")
        logging.info("用例编号：" + self.operatexcel.getId(row))
        logging.info("用例描述：" + self.operatexcel.getCase(row))
        self.success = "Fail"
        #协议状态码验证
        flag1=None
        if r.status_code == self.operatexcel.getHttpCode(row):
            logging.info("协议状态码验证OK！")
            flag1=True
        else:
            logging.error('!!!!!协议状态码验证失败！')
        logging.info("协议状态码：" + str(r.status_code))
        #业务状态码验证
        flag2=None
        if self.operatexcel.getResponseCode(row) == "":
            logging.info('没有业务状态码不需要验证！')
            flag2 = True
        else:
            try:
                responsecode = str(int(self.operatexcel.getResponseCode(row)))
            except:
                responsecode = self.operatexcel.getResponseCode(row)
            if responsecode in r.text:
                logging.info('业务状态码验证OK！')
                flag2 = True
            else:
                logging.error('!!!!!业务状态码验证失败！')
            logging.info('业务状态码：' + responsecode)
        #返回Body包含字段信息验证
        flag3=None
        if self.operatexcel.getException(row) == "":
            logging.info('没有返回字段信息不需要验证！')
            flag3 = True
        else:
            if self.operatexcel.getException(row) in r.text:
                logging.info("ResponseBody中返回关键字验证OK！")
                flag3 = True
            else:
                logging.info("ResponseBody中返回关键字验证失败！")
            #logging.info("ResponseData:\n" + json.dumps(r.json(),ensure_ascii=False,indent=4))
        #判断脚本是否执行成功
        if flag1==True and flag2==True and flag3==True:
            #默认接口测试成功写入测试结果
            self.success = "Pass"
        write_to_Excel(isWrite=isWrite,row=row,run_result=self.success)




# b = operationJson()
# a = Method()
# print(a.apiUrl(29))
# print(a.apiHeaders(row=29))
# print(b.get_jsonData(29))
#
# r = requests.post(url=a.apiUrl(29),
#                   data=b.get_jsonData(29),
#                   headers=a.apiHeaders(29)
#                   )
# print(r.text)
