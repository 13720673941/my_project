#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/25 18:43

from public.common.runReport import *
from config.pathConfig import *
from public.common.sendEmail import Send_Email
import os,unittest
SE = Send_Email()

def run_all_case():

    # 获取测试用例文件夹下所有子文件夹的名称
    fileName = os.listdir(testCasePath)
    file_list = ["1、注册登录","2、修改密码","3、工单管理","4、客户管理","5、师傅管理","6、运营管理","7、财务管理","8、备件管理"]
    # 除去py文件保留测试用例文件夹名
    # for file in fileName:
    #     if "__" not in file:
    #         file_list.append(file)
    # 添加到测试套件
    testUnit = unittest.TestSuite()
    # 循环获取测试用例文件夹中的测试套件添加到testUnit中
    for childFile in file_list:
        suits = get_suits(ChildName=childFile)
        testUnit.addTests(suits)
    # 第一次运行返回失败的用例测试套件
    run_report(testSuits=testUnit)
    # 重新运行失败的测试用例
    # run_fail_case(failCaseSuits)

if __name__ == '__main__':

    import time
    # 默认脚本执行失败
    isPass = False
    timing = "06:30"
    while True:
        # 获取当前时间
        time.sleep(10)
        now_time = time.strftime("%H:%M",time.localtime(time.time()))
        # print("\r","Now Time: "+now_time,end="")
        if timing in str(now_time):
            # 时间一样执行脚本
            print('========== 开始 ==========')
            # 定时间
            startTime = time.time()
            # 调用脚本用例集
            run_all_case()
            print('========== 结束 ==========')
            endTime = time.time()
            isPass = True
            break
    # 脚本执行成功发送邮件
    if isPass:
        print("\n脚本执行成功！")
        runtime = str(int((endTime-startTime)/60))# float类型取整,写入文本的是字符串类型转化为str
        # 脚本运行时间
        print('脚本运行时间：{0}分钟'.format(runtime))
        # 发送邮件
        SE.SendEmailMain(start_time=timing,run_time=runtime)
    else:
        print('\n脚本执行失败！')