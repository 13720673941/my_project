# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 14:43

import os

"""
    数据以及文件夹路径配置文件
"""

# 获取 UItest_Demo 文件夹的相对路径
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 输出日志的文件夹路径
logPath = os.path.join(parentPath,"result","log")+"\\"
# 注册手机号文件库
phoneNumberInfo = os.path.join(parentPath,"config","phoneNumber")
# 配置文件路径
configDataPath = os.path.join(parentPath,"config","configData.ini")
# 测试数据excel文件路径
testExcelPath = os.path.join(parentPath,"data","UItest_case.xls")
# 错误截图保存文件夹路径
errorImgPath = os.path.join(parentPath,"result","Img")+"\\"
# 测试用例存放文件夹路径
testScriptPath = os.path.join(parentPath,"script")+"\\"
# 测试报告存放路径
testReportPath = os.path.join(parentPath,"result","report")+"\\"