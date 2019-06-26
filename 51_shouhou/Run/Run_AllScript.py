# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/20 18:15

from Common.SendEmail import Send_Email
import sys
sys.path.append('../Run')
import Run_Brands_OrderFlow,Run_Branch_OrderFlow
SE = Send_Email()

if __name__ == '__main__':

    import time

    #默认脚本执行失败
    isPass = False
    #定时间
    startTime = time.time()
    timing = '12:10'
    while True:
        #获取当前时间
        time.sleep(30)
        now_time = time.strftime("%H:%M",time.localtime(time.time()))
        if now_time == timing:
            #获取开始时间
            #starttime = time.strftime("%H:%M",time.localtime(time.time()))
            #时间一样执行脚本
            print('==========开始==========')
            #调用脚本用例集
            Run_Brands_OrderFlow.run()
            Run_Branch_OrderFlow.run()
            print('==========结束==========')
            endTime = time.time()
            isPass = True
            break
    #脚本执行成功发送邮件
    if isPass:
        print("\n脚本执行成功！")
        runtime = str(int((endTime-startTime)/60))#float类型取整,写入文本的是字符串类型转化为str
        #脚本运行时间
        print('脚本运行时间：{0}分钟'.format(runtime))
        #发送邮件
        SE.SendEmailMain(StartTime=timing,RunTime=runtime)
    else:
        print('\n脚本执行失败！')