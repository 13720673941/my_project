# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 11:50

from public.page.brandsPage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *

class OrderLogPage(BasePage):

    """网点单量记录页面"""

    # 搜索开始日期输入框
    start_date_input = (By.XPATH,'//input[contains(@placeholder,"开始日期")]')
    # 搜索结束日期输入框
    end_date_input = (By.XPATH,'//input[contains(@placeholder,"结束日期")]')
    # 扣除类型搜索父路径
    type_select_parent_path = (By.XPATH,'//label[contains(text(),"类型")]/..//ul[2]')
    # 工单编号输入框
    order_number_input = (By.XPATH,'//label[contains(text(),"编号")]/..//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)