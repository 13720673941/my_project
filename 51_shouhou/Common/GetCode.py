# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from selenium import webdriver
import time,logging,configparser,os
from Common import Driver
from Common import Logger
from Common import Pubilc
from selenium.webdriver.support.wait import WebDriverWait

def FindCheckNum(driver,Phonenum,Handle='table',url='http://houtai.51shouhou.cn/#/login'):

    '''
    后台登录查找WAP网店登录验证码信息
    :param driver:PCdriver
    :param Phonenum:所要查找的手机号
    :param Handle:是否要奇幻窗口
    :param url:地址
    :return:
    '''
    #---------------------------------------------【大后台获取登陆验证码】-------------------------------------------------
    #获取后台账号密码配置文件
    DataPath = Pubilc.data_dir(filename='Login.ini')
    cf = configparser.ConfigParser()
    cf.read(DataPath,encoding='utf-8')
    user = cf.get('HT_Login','HT_username')
    pwd = cf.get('HT_Login','HT_password')

    #后台获取验证码
    driver.implicitly_wait(30)
    logging.info('<=====>【后台获取验证码】<=====>')
    #打开后台网址
    if Handle == 'table':
        Pubilc.table_handle(driver=driver,url=url)
    elif Handle == 'new':
        driver.get(url)

    driver.refresh()
    #输入用户名密码点击登陆
    time.sleep(1)
    for i in range(5):
        try:
            driver.find_element_by_xpath('//*[@id="login"]/form[1]/input[1]').clear()
            driver.find_element_by_xpath('//*[@id="login"]/form[1]/input[1]').send_keys(user)
            logging.info('.....输入用户名：%s'%user)
            driver.find_element_by_xpath('//*[@id="login"]/form[1]/input[2]').clear()
            driver.find_element_by_xpath('//*[@id="login"]/form[1]/input[2]').send_keys(pwd)
            logging.info('.....输入密码：xxxxxx')
            driver.find_element_by_css_selector('button.but').click()
            logging.info('.....点击->【登陆】')
            break
        except:
            if i == 4:
                logging.error('!!!!!后台登陆失败...')
                exit()
            else:
                pass
    #获取登陆系统提示异常信息
    try:
        HTmsg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="k-notification-wrap"]')).text
        logging.info('.....后台登陆异常：%s'%HTmsg)
    except:
        pass
    #判断后台登陆是否成功
    for i in range(5):
        try:
            title = driver.title
            if '服务后台' in title:
                logging.info('.....系统后台登陆成功！')
            else:
                logging.error('!!!!!系统后台登陆失败')
                exit()
            break
        except:
            if i == 4:
                logging.error('!!!!!获取网页标题失败...')
                exit()
            else:
                pass
    #获取手机号最新验证码
    driver.get("http://houtai.51shouhou.cn/#/code/verification/%E9%AA%8C%E8%AF%81%E7%A0%81")
    time.sleep(1)
    #输入手机号查询验证吗
    for i in range(5):
        try:
            driver.find_element_by_id('inputKey').send_keys(Phonenum)
            logging.info('.....输入手机号：%s'%Phonenum)
            driver.find_element_by_css_selector('button.btn.btn-primary.btn-block').click()
            logging.info('.....点击->【查询】')
            break
        except:
            if i == 4:
                logging.error('!!!!!输入手机号失败')
                exit()
            else:
                pass
    #获取验证码
    for i in range(5):
        time.sleep(1)
        try:
            PhoneCode = driver.find_element_by_xpath('//tbody[@role="rowgroup"]/tr[1]/td[3]/span').text
            logging.info('.....当前验证码为最新验证码：%s'%PhoneCode)
            break
        except:
            pass
    #关闭当前窗口
    driver.close()
    return PhoneCode


# from selenium import webdriver
# driver = webdriver.Chrome()
# a = FindCheckNum(driver=driver,Phonenum='13700000047',Handle='new')
# print(a)