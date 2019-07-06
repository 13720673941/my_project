# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:27

from selenium.webdriver.common.by import By
from public.common.basepage import BasePage
"""
客户管理-服务商列表页面
"""
class ServerBranchPage(BasePage):

    """页面元素信息"""

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
    # 第一个经销商的全部信息
    first_branch_info = (By.XPATH,'//div/div[2]/table/tbody/tr[1]')
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
    # 确定服务设置按钮
    confirm_teamwork_btn = (By.XPATH,'//div[contains(.,"服务设置")]/../../div[3]/button[2]')
    # 禁止派单按钮
    stop_please_btn = (By.XPATH,'//a[contains(.,"禁止派单")]')
    # 开启派单按钮
    open_please_btn = (By.XPATH,'//a[contains(.,"恢复派单")]')
    # 确定禁止/恢复
    confirm_please_btn = (By.XPATH,'//div[contains(text(),"是否")]/../div[4]/a[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_add_server_branch(self):
        """点击添加服务商"""
        self.click_button(self.add_server_btn)

    def get_customer_auto_name(self):
        """获取自动带出的客户的名字"""
        return self.get_att(self.customer_name_input,"value")

    def input_customer_phone_num(self,phone_num):
        """输入客户手机号"""
        self.input_message(self.customer_phone_num_input,phone_num)

    def input_customer_name(self,customer_name):
        """输入客户备注名称"""
        self.input_message(self.customer_name_input,customer_name)

    def select_please_to_someone(self):
        """选择向他派单"""
        self.click_button(self.select_please_order)

    def select_instead_to_someone(self):
        """选择向他报单"""
        self.click_button(self.select_instead_order)

    def select_return_to_someone(self):
        """选择向他返单"""
        self.click_button(self.select_return_order)

    def click_confirm_add_branch(self):
        """点击确定添加服务商"""
        self.click_button(self.add_branch_confirm_btn)

    def input_search_branch_keyword(self,branch_keyword):
        """输入搜索服务商关键字"""
        self.input_message(self.search_branch_input,branch_keyword)

    def click_search_branch_btn(self):
        """点击搜索服务商按钮"""
        self.click_button(self.search_branch_btn)

    def get_first_branch_info(self):
        """获取第一个服务商信息"""
        return self.get_text(self.first_branch_info)

