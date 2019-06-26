# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/24 17:13

from selenium import webdriver
from public.common.logconfig import Log
from public.common.basepage import BasePage
import time
log=Log()

def browser_driver():
    t1 = time.time()
    #浏览器驱动-谷歌
    options = webdriver.ChromeOptions()
    #禁止历览器弹窗
    prefs = {'profile.default_content_setting_values':{'notifications':2}}
    options.add_experimental_option('prefs',prefs)
    driver = webdriver.Chrome(options=options)
    base = BasePage(driver)
    log.info('{0} Launch browser with chrome, Spend {1} seconds.'.format(base.success,time.time()-t1))
    base.window_max()
    return driver