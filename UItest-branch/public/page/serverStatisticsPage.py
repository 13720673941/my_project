# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/18 18:15

from selenium.webdriver.common.by import By
from config.urlconfig import *
from public.common.basepage import BasePage
"""
客户统计页面
"""
class ManageStatisticsPage(BasePage):

    """
    服务商订单统计页面数据获取元素
    """
    # 切换服务商的table按钮
    server_table_btn = (By.XPATH,'//a[text()="服务商"]')
