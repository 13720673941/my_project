# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/12 19:03

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *
"""
厂商系统添加页面
"""
class BrandsPage(BasePage):

    """厂商系统账号列表页面元素"""

    # 厂商系统table按钮
    brands_table_btn = (By.XPATH,'//a[text()="签约厂商系统"]')
    # 添加厂商账号按钮
    add_brands_btn = (By.XPATH,'//a[text()="添加厂商系统账号"]')
    # 打开厂商系统选择框
    open_brands_select = (By.XPATH,'//label[text()="厂商系统"]/.././/span[@class="ivu-select-placeholder"]')
    # 厂商系统选择父元素节点
    parent_brands_select = (By.XPATH,'//label[text()="厂商系统"]/.././/ul[@class="ivu-select-dropdown-list"]')
    # 登录账号输入框
    login_use_input = (By.XPATH,'//label[text()="登录账号"]/.././/input')
    # 登录密码输入框
    login_pwd_input = (By.XPATH, '//label[text()="登录密码"]/.././/input')
    # 确定添加厂商账号按钮
    confirm_add_btn = (By.XPATH,'//div[contains(text(),"系统账号")]/../.././/button[2]')



    def __init__(self,driver):
        BasePage.__init__(self,driver)
