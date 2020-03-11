# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/30 20:19

from appium import webdriver
import time

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps['platformVersion'] = 6.0
#网点模拟器端口
desired_caps['deviceName'] = "612QZBQK333SB"
#打开中文输入
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['appPackage'] = "com.chaoshu.shouhou"
desired_caps['appActivity'] = "com.uzmap.pkg.EntranceActivity"
desired_caps['appWaitActivity'] = "com.uzmap.pkg.EntranceActivity"
#设置appium超时，appium默认60s内没有命令就关闭APP
desired_caps['newCommandTimeout'] = 3600
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(10)

driver.find_element_by_xpath('//android.view.View[@content-desc=""]').click()
time.sleep(5)
driver.find_element_by_xpath('//android.view.View[@content-desc="未登录"]').click()
time.sleep(5)
driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入手机号或用户名"]').send_keys("13700000004")
time.sleep(3)
driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="密码登录"]/android.widget.EditText[2]').send_keys("222222")
time.sleep(2)
driver.find_element_by_xpath('//android.widget.Button[@content-desc="登录"]').click()