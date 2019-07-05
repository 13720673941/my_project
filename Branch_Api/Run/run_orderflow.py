# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/28 17:05

from Common.Public import runCase
import sys,HTMLTestRunnerCN,unittest

sys.path.append("../Script/3、OrderMode")
import test_orderflow

def run():

    case = unittest.TestSuite()
    case.addTests([test_orderflow.OrderFlow("test_flow01"),
                   test_orderflow.OrderFlow("test_flow02"),
                   test_orderflow.OrderFlow("test_flow03"),
                   test_orderflow.OrderFlow("test_flow04"),
                   test_orderflow.OrderFlow("test_flow05"),
                   test_orderflow.OrderFlow("test_flow06"),
                   test_orderflow.OrderFlow("test_flow07")
                   ])

    runCase(fileName="test_orderflow",reportName="【正式网点】订单模块网点自营订单流程",
            titleName="【正式网点】订单模块网点自营订单流程",scription="网点自营订单流程",case=case)


if __name__ == '__main__':
    run()