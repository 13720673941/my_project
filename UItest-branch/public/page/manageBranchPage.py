# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/26 12:00
from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
"""
客户管理-经销商列表页面
"""
class DealerBranchPage(BasePage):

    """经销商列表页面"""
    branch_list_url = 'http://www.51shouhou.cn/singleBranch/#/customer/list'
    #添加经销商按钮
    add_manage_branch_btn = (By.XPATH,'//a[text()="添加经销商"]')
    #经销商客户主账号输入框
    manage_branch_phone_input = (By.XPATH,'//input[@placeholder="请输入客户注册时使用的手机号"]')
    #经销商客户名称输入框
    manage_branch_name_input = (By.XPATH,'//input[@placeholder="请输入客户名称"]')
    #添加经销商确定按钮
    add_branch_confirm_btn = (By.XPATH,'//div[text()="添加经销商"]/../../div[3]/div/button[2]')
    #客户列表搜索框
    search_branch_input = (By.XPATH,'//input[@placeholder="输入客户名称/手机号进行查询"]')
    #搜索按钮
    search_branch_btn = (By.XPATH,'//a[text()="搜索"]')
    #服务设置按钮
    set_server_btn = (By.XPATH,'//div/div[2]/.//a[text()="服务设置"]')
    #输入客户备注
    branch_remark = (By.XPATH,'//label[text()="客户备注："]/../div/div/div/div/input')
    #服务设置确定按钮
    set_server_confirm_btn = (By.XPATH,'//div[contains(.,"服务设置")]/../../div[3]/div/button[2]')
    #第一个经销商的全部信息
    first_branch_info = (By.XPATH,'//div/div[2]/table/tbody/tr[1]')
    #暂停接单按钮
    stop_take_order_btn = (By.XPATH,'//a[contains(text(),"暂停接单")]')
    #暂停接单确定按钮
    stop_take_confirm_btn = (By.XPATH,'//div[text()="是否暂停接单"]/../div[4]/a[2]')
    #开启接单按钮
    open_take_order_btn = (By.XPATH,'//a[contains(text(),"恢复接单")]')
    #开启接单确定按钮
    open_take_confirm_btn = (By.XPATH, '//div[text()="是否恢复接单"]/../div[4]/a[2]')
    #撤销申请按钮
    del_visit_branch_btn = (By.XPATH,'//a[contains(text(),"撤销")]')
    #撤销申请确定按钮
    del_visit_confirm_btn = (By.XPATH,'//div[text()="是否撤销？"]/../div[4]/a[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_dealer_page(self):
        """进入邀请经销商页面"""
        self.open_url(self.branch_list_url)

    def click_add_manage_branch(self):
        """点击添加经销商"""
        self.click_button(self.add_manage_branch_btn)

    def input_branch_phone_num(self,phone_num):
        """输入客户手机号"""
        self.input_message(self.manage_branch_phone_input,phone_num)

    def input_branch_name(self,branch_name):
        """输入客户名称"""
        self.clear_input(self.manage_branch_name_input)
        self.input_message(self.manage_branch_name_input,branch_name)

    def get_branch_name(self):
        """获取输入框的网点名称"""
        return self.get_att(self.manage_branch_name_input,'value')

    def click_confirm_add(self):
        """点击确定添加经销"""
        self.click_button(self.add_branch_confirm_btn)

    def input_search_message(self,search_info):
        """输入搜索信息"""
        self.input_message(self.search_branch_input,search_info)

    def click_search(self):
        """点击搜索"""
        self.click_button(self.search_branch_btn)

    def get_first_branch_info(self):
        """获取第一行的网点的信息"""
        return self.get_text(self.first_branch_info)

    def click_set_server(self):
        """点击服务设置"""
        self.click_button(self.set_server_btn)

    def clear_branch_remark(self):
        """清除旧备注"""
        self.clear_input(self.branch_remark)

    def input_branch_remark(self,branch_remark):
        """输入客户备注"""
        self.input_message(self.branch_remark,branch_remark)

    def click_server_set_confirm(self):
        """点击服务设置的确定"""
        self.click_button(self.set_server_confirm_btn)

    def click_stop_take_order(self):
        """点击暂停接单"""
        self.click_button(self.stop_take_order_btn)

    def click_stop_take_confirm(self):
        """点击暂停接单确定"""
        self.click_button(self.stop_take_confirm_btn)

    def click_open_take_order(self):
        """点击开启接单"""
        self.click_button(self.open_take_order_btn)

    def click_open_take_confirm(self):
        """点击开启接单确定"""
        self.click_button(self.open_take_confirm_btn)