# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from selenium import webdriver
import time,os
import logging.config

def screen_shop(driver):

    #错误截图
    picture_name = time.strftime('%Y-%m-%d %H %M %S', time.localtime(time.time()))
    picture_file = 'D:\\MyWork\\51_shouhou\\Config\\Screenshop\\'
    picture_path = picture_file + picture_name + '.png'
    driver.get_screenshot_as_file(picture_path)
    print('!!!!!错误截图：%s'%picture_path)


def WAP_Brower():

    # 设置浏览器手机模式
    mobile_emulation = {"deviceName": "iPhone 8"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.maximize_window()
    driver.set_window_size(width=300, height=800)
    #driver.set_window_position(x=400, y=10)
    return driver

def PC_Brower():

    # 禁止浏览器弹窗
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'notifications': 2}}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver