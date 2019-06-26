# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/23 16:42

import sys,unittest
from Common import Pubilc
sys.path.append("../Scripts/网点订单流程")
import Branch_OrderFlow01

def run():

    #建测试套添加测试用例
    case = unittest.TestSuite()
    case.addTest(Branch_OrderFlow01.Please_Order('test_PleaseOrder'))

    Pubilc.run_case(report_file="网点订单流程",report_name="【正式网点】网点订单流程",
                    title="【正式网点】网点订单流程",descript="网点全部类型订单流程",case=case)


if __name__ == '__main__':
    run()