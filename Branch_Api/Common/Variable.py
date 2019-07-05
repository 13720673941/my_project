# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

class variable():

    '''excel中每列的索引'''
    Id = 0
    Case = 1
    Url = 2
    Method = 3
    Headers = 4
    Body = 5
    HttpCode = 6
    ResponseCode = 7
    Exception = 8
    Result = 9
    ContentType = 10

'''
对excel中的数据列进行赋变量处理，因为列永远不会变动
'''

def get_id():

    return variable.Id

def get_case():

    return variable.Case

def get_url():

    return variable.Url

def get_method():

    return variable.Method

def get_headers():

    return variable.Headers

def get_body():

    return variable.Body

def get_httpcode():

    return variable.HttpCode

def get_responsecode():

    return variable.ResponseCode

def get_Exception():

    return variable.Exception

def get_Result():

    return variable.Result

def get_ContentType():

    return variable.ContentType