# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/29 17:44

from Common.Public import runCase
import unittest,sys,HTMLTestRunnerCN

sys.path.append("../Script/3、OrderMode")
import test_JDorder

def run():

    case = unittest.TestSuite()
    case.addTests([test_JDorder.JDOrder("test_JD01"),test_JDorder.JDOrder("test_JD02"),
                   test_JDorder.JDOrder("test_JD03"),test_JDorder.JDOrder("test_JD04")
                   ])

    runCase(fileName="test_JDorder",reportName="【正式网点】鉴定单模块",titleName="【正式网点】鉴定单模块",
            scription="网点鉴定单模块接口",case=case)

if __name__ == '__main__':
    run()