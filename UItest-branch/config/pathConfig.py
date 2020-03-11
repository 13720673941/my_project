#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/17 14:47

"""
    所有文件夹位置路径的配置文件
"""

import os

# 父目录路径
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件数据路径
configPath = os.path.join(parentPath,'config','configData.ini')
# 注册手机号路径
regPhonePath = os.path.join(parentPath,'config','regPhoneNum.txt')
# 注册用户名路径
regUserPath = os.path.join(parentPath,'config','regUsername.txt')
# 已经注册账户文件信息
regAccountPath = os.path.join(parentPath,'config','regAccount.txt')
# 账户信息文件路径
accountDataPath = os.path.join(parentPath,'data','accountData.ini')
# 工共关联订单单号路径
orderNumPath = os.path.join(parentPath,'data','orderNumber.ini')
# 工单信息保存路径
orderInfo = os.path.join(parentPath,'data','orderMessage.ini')
# 上传图片保存路径
picturePath = os.path.join(parentPath,'data','picture') + '\\'
# 日志保存文件夹
logSavePath = os.path.join(parentPath,'result','log') + '\\'
# 报告保存路径文件夹
reportSavePath = os.path.join(parentPath,'result','report') + '\\'
# 错误截图保存路径文件夹
errorImagePath = os.path.join(parentPath,'result','image') + '\\'
# 测试结果保存路径
testResultPath = os.path.join(parentPath,'result','testResult')+'\\'
# 获取测试用例路径
testCasePath = os.path.join(parentPath,'testcase') + '\\'
# excel 测试用例数据路径
testExcelPath = os.path.join(parentPath,"data","UI_testCase.xls")
# 页面元素配置文件路径
elementDataPath = os.path.join(parentPath,'data','elementData.ini')
# 导出文件的默认路径位置
exportFilePath = "C:\\Users\\kk\\Downloads"

