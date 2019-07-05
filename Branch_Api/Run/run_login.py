# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import sys,unittest
from Common.Public import runCase

sys.path.append("../Script/1、LoginMode")
import test_login

def run():

    case = unittest.TestSuite()
    case.addTest(test_login.BranchLogin("test_login01"))
    case.addTest(test_login.BranchLogin("test_login02"))
    case.addTest(test_login.BranchLogin("test_login03"))
    case.addTest(test_login.BranchLogin("test_login04"))
    case.addTest(test_login.BranchLogin("test_login05"))

    runCase(fileName="test_login",reportName="【正式网点】登录模块",
            titleName="【正式网点】登录模块",scription="网点登录接口测试",case=case)

if __name__ == '__main__':
    run()
