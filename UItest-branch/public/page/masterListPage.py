# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 17:40

from selenium.webdriver.common.by import By
from public.common.basepage import BasePage
from config.urlconfig import *

class MasterListPage(BasePage):

    """师傅列表页面"""

    # 添加师傅按钮
    add_master_btn = (By.XPATH,'//a[contains(text(),"添加师傅")]')
    # 师傅手机号输入框
    master_phone_input = (By.XPATH,'//label[text()="师傅手机号："]/..//input')
    # 师傅备注输入框
    master_remark_input = (By.XPATH,'//label[text()="师傅姓名："]/..//input')
    # 确定添加师傅
    add_master_confirm_btn = (By.XPATH,'//div[text()="添加师傅"]/../..//button[2]')
    # 师傅搜索框
    master_search_input = (By.XPATH,'//input[starts-with(@placeholder,"输入师傅姓名")]')
    # 搜索按钮
    master_search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 撤销申请师傅合作//默认先搜索师傅再撤销
    del_master_teamwork_btn = (By.XPATH,'//tr[@class="ivu-table-row"][1]//a[text()="撤销"]')
    # 确认弹窗操作按钮
    confirm_master_btn = (By.XPATH,'//div[contains(text(),"？")]/..//a[2]')
    # 师傅服务设置按钮
    master_server_set_btn = (By.XPATH,'//tr[@class="ivu-table-row"][1]//a[text()="设置"]')
    # 师傅禁止派单按钮
    master_stop_please_btn = (By.XPATH,'//tr[@class="ivu-table-row"][1]//a[text()="禁止派单"]')
    # 师傅恢复派单按钮
    master_open_please_btn = (By.XPATH,'//tr[@class="ivu-table-row"][1]//a[text()="恢复派单"]')
    # ===师傅服务设置===
    # 设置师傅服务备注输入框
    set_master_remark_input = (By.XPATH,'//label[contains(text(),"师傅备注：")]/..//input')
    #

    def __init__(self,driver):
        BasePage.__init__(self,driver)