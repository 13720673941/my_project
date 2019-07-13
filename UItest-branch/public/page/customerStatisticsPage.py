# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 17:16

from selenium.webdriver.common.by import By
from config.urlconfig import *
from public.common.basepage import BasePage
"""
客户统计页面
"""
class CustomerStatisticsPage(BasePage):

    """客户订单统计页面数据获取元素"""

    # 客户名称手机号搜索输入框
    customer_search_input = (By.XPATH,'//label[text()="客户名称/手机号："]/..//input')
    # 下单开始时间输入框
    create_order_start_time = (By.XPATH,'//label[text()="下单时间："]/../div[1]/.//input')
    # 下单结束时间输入框
    create_order_end_time = (By.XPATH,'//label[text()="下单时间："]/../div[2]/.//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 

    def __init__(self,driver):
        BasePage.__init__(self,driver)