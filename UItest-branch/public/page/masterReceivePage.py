# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/5 11:58

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *
from config.pathconfig import *
import os

class MasterReceivePage(BasePage):

    """
    【备件管理】-【师傅领用】页面
    """

    # 师傅领用记录按钮
    master_receive_btn = (By.XPATH,'//div[@class="work-operation"]//li[2]/a')
    # 工程师选择下拉打开按钮
    master_select_open_btn = (By.XPATH,'//label[contains(text(),"工程师")]/../div/div')
    # 工程师下拉父节点
    master_select_parent_xpath = (By.XPATH,'//label[contains(text(),"工程师")]/../div//ul[2]')
    # 备件申请数量输入框
    sparePart_count_input = (By.XPATH,'(//tr[@class="ivu-table-row"][1])[3]/td[6]//input')
    # 领用备件备注输入框
    remark_input = (By.XPATH,'(//tr[@class="ivu-table-row"][1])[3]/td[7]//input')
    # 备件删除按钮
    sparePart_del_btn = (By.XPATH,'(//tr[@class="ivu-table-row"][1])[3]/td[8]//a')
    # 获取第一行备件的所有信息
    receive_first_info = (By.XPATH,'(//tr[@class="ivu-table-row"][1])[3]')
    # 保存按钮
    save_btn = (By.XPATH,'(//button[contains(text(),"保存")])[2]')
    # 筛选师傅项打开下拉按钮
    search_master_open_btn = (By.XPATH,'//label[contains(text(),"师傅")]/..//div')
    # 筛选师傅项打开父节点
    search_master_parent_xpath = (By.XPATH,'//label[contains(text(),"师傅")]/..//div//ul[2]')
    # 领用时间开始输入框
    receive_start_time_input = (By.XPATH,'//label[contains(text(),"领用时间")]/../div[1]//input')
    # 领用结束时间输入框
    receive_end_time_input = (By.XPATH,'//label[contains(text(),"领用时间")]/../div[2]//input')
    # 备件编码输入框
    sparePart_number_input = (By.XPATH,'(//label[contains(text(),"备件条码")]/..//input)[1]')
    # 备件名称输入框
    sparePart_name_input = (By.XPATH,'(//label[contains(text(),"备件名称")]/..//input)[1]')
    # 搜索按钮
    search_receive_log_btn = (By.XPATH,'//a[contains(text(),"搜索")]')
    # 搜索后第一条备件全部信息
    search_first_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 点击导出按钮
    export_btn = (By.XPATH,'//a[contains(text(),"导出")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_receive_log_page(self):
        """进入师傅领用日志记录页面"""
        self.open_url(master_receive_log_url)

    def click_master_receive_btn(self):
        """点击师傅领用按钮"""
        self.click_button(self.master_receive_btn)

    def select_receive_master_name(self,master_name):
        """选择领用备件师傅名字"""
        self.operate_not_select(
            open_el=self.master_select_open_btn,parent_el=self.master_select_parent_xpath,value=master_name)

    def input_receive_count(self,receive_count):
        """输入领用数量"""
        self.input_message(self.sparePart_count_input,receive_count)

    def input_receive_remark(self,receive_remark):
        """输入领用备注信息"""
        self.input_message(self.remark_input,receive_remark)

    def click_delete_sparePart(self):
        """点击删除备件按钮"""
        self.click_button(self.sparePart_del_btn)

    def get_receive_first_info(self):
        """获取领用页面第一条备件所有信息"""
        return self.get_text(self.receive_first_info)

    def click_save_receive(self):
        """点击保存领用"""
        self.click_button(self.save_btn)

    def select_search_master_name(self,master_name):
        """选择搜索师傅名称"""
        self.operate_not_select(
            open_el=self.search_master_open_btn,parent_el=self.search_master_parent_xpath,value=master_name)

    def input_receive_start_time(self,start_date):
        """输入师傅领用开始时间"""
        self.input_message(self.receive_start_time_input,start_date)

    def input_receive_end_time(self,end_date):
        """输入师傅领用结束日期"""
        self.input_message(self.receive_end_time_input,end_date)

    def input_sparePart_number(self,spartPart_number):
        """输入备件条码"""
        self.input_message(self.sparePart_number_input,spartPart_number)

    def input_sparePart_name(self,sparePart_name):
        """输入备件名称"""
        self.input_message(self.sparePart_name_input,sparePart_name)

    def click_search_btn(self):
        """点击搜素按钮"""
        self.click_button(self.search_receive_log_btn)

    def get_first_search_info(self):
        """获取搜索后的第一条信息"""
        return self.get_text(self.search_first_info)

    def click_export_btn(self):
        """点击导出按钮"""
        self.click_button(self.export_btn)

    def get_export_file_list(self):
        """获取导出默认文件夹路径的所有文件,返回一个列表"""

        # 导出的excel列表
        export_excel_list = os.listdir(exportFilePath)
        # 按创建时间排序
        new_list = sorted(export_excel_list,key=lambda x:os.path.getctime(os.path.join(exportFilePath,x)))
        # 获取最后一个excel就是最新导出的
        return new_list[-1]


