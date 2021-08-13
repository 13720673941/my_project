# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/19 14:41

"""
    需要动态参数的请求数据，需重新封装读取的请求参数信息，在用例脚本中调用
"""

from common.operateFile import OperateFile
operate = OperateFile()

# 例子程序：
def login_data():
    """登录参数重新赋值"""
    data = operate.read_json("login")
    data["passWord"] = "222222"
    return data



if __name__ == '__main__':

    data = login_data()
    print(data)