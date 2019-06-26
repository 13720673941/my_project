# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/17 14:47

import os

#父目录路径
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#邮箱账号密码路径
emailPath = os.path.join(parentPath,'config','emaildata.ini')
#注册手机号路径
regPhonePath = os.path.join(parentPath,'config','regphonenum.txt')
#注册用户名路径
regUserPath = os.path.join(parentPath,'config','regusername.txt')
#测试json数据路径
testData = os.path.join(parentPath,'data','testdata.json')
#账户信息文件路径
accountDataPath = os.path.join(parentPath,'data','accountdata.ini')
#工共等待单号路径
orderNumPath = os.path.join(parentPath,'data','ordernumber.ini')
#工单信息保存路径
orderInfo = os.path.join(parentPath,'data','ordermessage.ini')
#上传图片保存路径
picturePath = os.path.join(parentPath,'data','picture') + '\\'
#日志保存文件夹
logSavePath = os.path.join(parentPath,'result','log') + '\\'
#报告保存路径文件夹
reportSavePath = os.path.join(parentPath,'result','report') + '\\'
#错误截图保存路径文件夹
errorImagePath = os.path.join(parentPath,'result','image') + '\\'
#测试结果保存路径
testResultPath = os.path.join(parentPath,'result','testresult.ini')
#获取测试用例路径
testCasePath = os.path.join(parentPath,'testcase') + '\\'

