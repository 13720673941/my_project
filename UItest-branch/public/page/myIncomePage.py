# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/22 16:30

from public.page.brandsPage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *


class MyIncomePage(BasePage):

    """
    我的收入页面
    """
    # 打开下拉收入类型按钮
    open_income_type_btn = (By.XPATH,'//label[text()="收入类型："]/../div/div')
    # 收入类型选项父节点
    income_type_parent_xpath = (By.XPATH,'//label[text()="收入类型："]/..//ul[2]')
    # 打开服务类型下拉按钮
    open_server_type_btn = (By.XPATH,'//label[text()="服务类型："]/../div/div')
    # 服务类型选项父节点
    server_type_parent_xpath = (By.XPATH,'//label[text()="服务类型："]/..//ul[2]')
    # 服务师傅输入框
    server_master_input = (By.XPATH,'//label[text()="服务师傅："]/..//input')
    # 工单编号输入框
    order_number_input = (By.XPATH,'//label[text()="工单编号："]/..//input')
    # 搜索按钮
    search_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 收入列表第一行全部信息
    first_row_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')

    