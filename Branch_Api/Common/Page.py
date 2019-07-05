# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

from Common.OperationJson import operationJson
from Common.OperationConfig import operationConfig
from Common.OperationExcel import operationExcel
from Common.Requests import Method
import json

'''
对接口测试中动态请求数据的特殊处理重新赋值
'''
class Page:

    def __init__(self):
        '''设置派单流程中api需要的订单号和PKID'''
        #实例化
        self.opconfig = operationConfig()
        self.opjson = operationJson()
        self.method = Method()
        self.orderPkId = self.opconfig.readConfig(section="AddOrder",option="addtradepkid")
        self.orderId = self.opconfig.readConfig(section="AddOrder",option="addtradeid")

    def setPleaseOrder(self):
        '''网点派单到师傅'''
        jsonData = self.opjson.get_jsonData(row=22)
        #设置jsonData中的PkId和TradeId
        jsonData["PkId"] = self.orderPkId
        jsonData["TradeId"] = self.orderId
        return jsonData

    def submitFK(self):
        '''网点提交记录反馈信息'''
        jsonData = json.loads(self.opjson.get_jsonData(row=23))
        jsonData["FkTradeInfoPkId"] = self.orderPkId
        return jsonData

    def reserveOrder(self):
        '''网点预约订单'''
        jsonData = self.opjson.get_jsonData(24)
        jsonData["PkId"] = self.orderPkId
        return jsonData

    def reserverOrder2(self):
        '''网点改约订单'''
        jsonData = self.opjson.get_jsonData(25)
        jsonData["TradePkId"] = self.orderPkId
        return jsonData

    def canelOrder(self,row=26):
        '''网点取消订单'''
        url = self.method.apiUrl(row)
        newUrl = url.replace("{TradePkId}",self.orderPkId)
        return newUrl

    def setSeach(self,keyword="待处理"):
        '''异常订单模块，已处理、待处理、处理中订单查询请求参数赋值函数'''
        jsonData = self.opjson.get_jsonData(40)
        newStr = jsonData["params"].replace("{status}",keyword)
        newJson = {"params":newStr}
        return newJson

    def ChaPingOrder(self,row,keyword="待处理"):
        '''异常订单：待处理、已处理、处理中->差评单、预约延时、上门延时、服务延时、投诉、驳回订单查询'''
        jsonData = self.opjson.get_jsonData(row)
        newStr = jsonData["param"].replace("{status}",keyword)
        newJson = {
            "key":"es_common_query",
            "param":newStr
        }
        return newJson

    #keyword订单状态关键字信息
    def JDorder(self,row,keyword):
        '''待鉴定、已鉴定单搜索、整机退换订单待网点提交、品牌审核、品牌入库、品牌出库、网点入库、已完成、已拒绝'''
        jsonData = self.opjson.get_jsonData(row)
        newStr = jsonData["query"].replace("{status}",keyword)
        newJson = {
            "query":newStr
        }
        return newJson

    #billData品牌商账单的日期 y-m-d格式2018-12-01
    def branchIncome(self,row,billData):
        '''网点财务收入：网点品牌商月份收入账单信息'''
        jsonData = self.opjson.get_jsonData(row)
        newStr = jsonData["query"].replace("{billData}",billData)
        newJson = {
            "query":newStr
        }
        return newJson

    #"2018-01-01","2018-12-01","2019-02-01"
    def searchIncome(self,row,queryId,billData,startData,endData):
        '''
        :param row:         用例行数
        :param queryId:     查询ID账单信息
        :param billData:    账单日期 y-m-d
        :param startData:   账单开始时间
        :param endData:     账单结束时间
        '''
        #'''网点用户、市场、服务账单信息'''
        jsonData = self.opjson.get_jsonData(row)
        newStr = jsonData["params"].replace("{queryId}",queryId).replace("{billData}",billData).replace("{startData}",startData).replace("{endData}",endData)
        newJson = {
            "params":newStr
        }
        return newJson

    def setQueryId(self,row,queryId):
        '''设置请求数据的queryId财务模块请求数据的Id'''
        jsonData = self.opjson.get_jsonData(row)
        newStr = jsonData["params"].replace("{queryId}",queryId)
        newJson = {
            "params":newStr
        }
        return newJson


# a = Page()
# print(a.searchIncome(77,"41","2018-01-01","2018-12-01","2019-02-01"))