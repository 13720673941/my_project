#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/25 18:43

from public.common.sendemail import Send_Email
import sys
SE = Send_Email()
sys.path.append('../run')
import run_a_registerLogin,run_b_alterPassword,run_c_orderManage,run_d_customManage,\
    run_e_masterManage,run_f_operationManage,run_g_financeManage

if __name__ == '__main__':

    import time
    # 默认脚本执行失败
    isPass = False
    # 定时间
    startTime = time.time()
    timing = "12:12"
    while True:
        # 获取当前时间
        time.sleep(1)
        now_time = time.strftime("%H:%M",time.localtime(time.time()))
        if now_time == timing:
            # 时间一样执行脚本
            print('========== 开始 ==========')
            # 调用脚本用例集
            run_a_registerLogin.run()
            run_b_alterPassword.run()
            run_c_orderManage.run()
            # run_d_customManage.run()
            # run_e_masterManage.run()
            # run_f_operationManage.run()
            # run_g_financeManage.run()
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