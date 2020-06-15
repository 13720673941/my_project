# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/14 22:30

from public.common.sendEmail import SendEmail
from run.running import run
import datetime,time
"""
    定时运行测试脚本并发送邮件
"""
def run_timing(startTime):
    """
    :param startTime: 格式例如 23:10:00
    :return:
    """
    # 获取当前日期
    nowDate = datetime.datetime.now().strftime("%Y-%m-%d")
    start = nowDate+" "+startTime
    print("---------- 开始执行时间：{} ----------".format(start))
    # 开始时间转化成时间戳
    startTimeNum = time.mktime(time.strptime(start,"%Y-%m-%d %H:%M:%S"))
    # 初始化执行失败
    isOk = False
    while True:
        # 判断当前时间是否大于开始时间
        nowTimeNum = time.time()
        if nowTimeNum > startTimeNum:
            startRunTimeNum = time.time()
            print("\n")
            # 执行脚本
            run()
            endRunTimeNum = time.time()
            isOk = True
            break
        else:
            nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\r","当前时间："+nowTime,end="")
    # 脚本执行成功
    if isOk:
        # 发送邮件通知
        SendEmail().send_email()
        runTime = format(((endRunTimeNum-startRunTimeNum)/60),".2f")
        print("---------- 脚本运行时间：{} 分钟 ----------".format(str(runTime)))
    else:
        print("！！！！！！！脚本执行失败！！！！！！！")


if __name__ == '__main__':

    run_timing(startTime="23:10:00")
