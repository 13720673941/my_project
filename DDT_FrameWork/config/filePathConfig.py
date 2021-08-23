# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/21 23:43

"""
项目所有文件夹相对路径
"""

import os

# 项目相对父路径
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 浏览器驱动配置文件路径
chromeDriverPath = os.path.join(parentPath, "config", "driver") + "\\"
# 测试数据文件路径
testDataPath = os.path.join(parentPath, "data") + "\\"
# 错误截图保存路径
errorPicturePath = os.path.join(parentPath, "result", "errorPic") + "\\"
# 日志保存路径
logSavePath = os.path.join(parentPath, "result", "log") + "\\"
# 测试报告保存路径
reportSavePath = os.path.join(parentPath, "result", "report") + "\\"
# 项目运行依赖安装文件
requirementsPath = os.path.join(parentPath, "requirements")
# 配置文件路径
configDataPath = os.path.join(parentPath, "config", "configData.ini")
