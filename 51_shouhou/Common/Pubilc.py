# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/2/25 20:17

import os,time,HTMLTestRunnerCN

def data_dir(file="Config",filename=None):

    #文件夹读取
    '''
    :param file:        文件夹
    :param filename:    文件名字
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),file,filename)

def run_case(report_file,report_name,title,descript,case):

    #生成报告
    '''
    :param report_file: 报告文件夹名字
    :param report_name: 报告名字
    :param title:       报告标题
    :param descript:    报告描述
    :param case:        用例集合
    '''
    tm = time.strftime('%y-%m-%d %H_%M_%S', time.localtime(time.time()))
    Path = '../Report/'+report_file+'/'
    Report = Path + report_name + tm + '.html'
    fp = open(Report,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=title,
                                             description=descript)
    # print('开始时间：{0}'.format(tm))
    runner.run(case)
    fp.close()

def table_handle(driver,url):

    #切换窗口，获取当前窗口的handle
    '''
    :param driver: driver驱动
    :param url:    js打开的地址
    '''
    CurrentHandles = driver.window_handles
    driver.execute_script("window.open('"+url+"')")
    NowHandles = driver.window_handles
    for handle in NowHandles:
        if handle not in CurrentHandles:
            driver.switch_to.window(handle)

