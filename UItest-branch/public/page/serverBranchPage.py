# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:27

from selenium.webdriver.common.by import By
from public.common.basepage import BasePage
"""
客户管理-服务商列表页面
"""
class ServerBranchPage(BasePage):

    """页面元素路径"""
    # 切换服务商的table按钮
    server_branch_table = (By.XPATH,'//a[text()="服务商"]')
    # 添加服务商按钮
    add_server_btn = (By.XPATH,'//a[text()="添加服务商"]')
    # 客户手机号输入框
    customer_phone_num_input = (By.XPATH,'//input[@placeholder="请输入客户注册时使用的手机号"]')
    # 客户名称
    customer_name_input = (By.XPATH,'//input[@placeholder="请输入客户名称"]')
    # 选择向他派单
    select_please_order = (By.XPATH,'//label[contains(.,"向他派单")]')
    # 选择向他报单
    select_instead_order = (By.XPATH,'//label[contains(.,"向他报单")]')
    # 选择向他返单
    select_return_order = (By.XPATH,'//label[contains(.,"向他返单")]')
    # 邀请服务商确定按钮
    add_branch_confirm_btn = (By.XPATH,'//div[text()="添加服务商"]/../../div[3]/div/button[2]')
    # 服务商搜索框
    search_branch_input = (By.XPATH,'//input[@placeholder="输入客户名称/手机号进行查询"]')
    # 搜索按钮
    search_branch_btn = (By.XPATH,'//a[text()="搜索"]')
    # 左右滑动托条按钮
    roll_btn = (By.XPATH,'//*[@class="ivu-table-body ivu-table-overflowX"]')
    # 服务设置按钮
    set_server_btn = (By.XPATH,'//div/div[2]/.//a[text()="服务设置"]')
    # 服务撒备注
    server_branch_remark = (By.XPATH,'//label[contains(.,"客户备注：")]/.././/input[@type="text"]')
    # 合作类型派单
    teamwork_type_1 = (By.XPATH,'//label[contains(text()," 派单")]')
    # 合作类型报单
    teamwork_type_2 = (By.XPATH,'//label[contains(text()," 报单")]')
    # 合作类型返单
    teamwork_type_3 = (By.XPATH,'//label[contains(text()," 返单")]')




    def __init__(self,driver):
        BasePage.__init__(self,driver)

