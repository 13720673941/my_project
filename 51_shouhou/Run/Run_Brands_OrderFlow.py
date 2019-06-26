# coding=utf-8

import sys,unittest
from Common import Pubilc
sys.path.append("../Scripts/品牌商订单流程")
import Brands_OrderFlow01,Brands_OrderFlow02,Brands_OrderFlow03,Brands_OrderFlow04,Brands_OrderFlow05,Brands_OrderFlow06,Brands_OrderFlow07

def run():

    #建测试套添加测试用例
    case = unittest.TestSuite()
    case.addTest(Brands_OrderFlow01.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow02.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow03.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow04.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow05.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow06.Please_Order('test_PleaseOrder'))
    case.addTest(Brands_OrderFlow07.Please_Order('test_PleaseOrder'))

    Pubilc.run_case(report_file="品牌商订单流程",report_name="【正式品牌商】品牌商订单流程",
                    title="【正式品牌商】品牌商订单流程",descript="品牌商全部类型订单流程",case=case)


if __name__ == '__main__':
    run()
