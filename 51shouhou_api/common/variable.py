# -*- coding: utf-8 -*-

# @Author  : MrDeng
# @Time    : 2019/11/5 11:38

class Variable():

    """
    固定列字段赋值列数一般是不改变的
    """

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

"""
定义获取每个列数的函数
"""

def get_col_id():

    return Variable.Id

def get_col_case():

    return Variable.Case

def get_col_url():

    return Variable.Url

def get_col_method():

    return Variable.Method

def get_col_headers():

    return Variable.Headers

def get_col_body():

    return Variable.Body

def get_col_httpCode():

    return Variable.HttpCode

def get_col_responseCode():

    return Variable.ResponseCode

def get_col_exception():

    return Exception

def get_col_result():

    return Variable.Result






# a = get_col_id()
#
# print(a)
