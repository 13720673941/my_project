# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/5 11:58

from public.common.basePage import BasePage
from config.urlConfig import *
from config.pathConfig import *
import os

class MasterReceivePage(BasePage):

    """
        【备件管理】-【师傅领用】页面
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中师傅领用页面的元素信息"""
        return read_config_data("master_receive_page",option,elementDataPath)

    def enter_receive_log_page(self):
        """进入师傅领用日志记录页面"""
        self.open_url(master_receive_log_url,self.get_elements("receive_end_time_input"))

    def enter_master_inventory_page(self):
        """进入师傅库存页面"""
        self.open_url(master_inventory_url)

    def click_master_receive_btn(self):
        """点击师傅领用按钮"""
        self.click_button(self.get_elements("master_receive_btn"))

    def select_receive_master_name(self,masterName):
        """选择领用备件师傅名字"""

        self.sleep(2)
        if masterName != "":
            self.operate_not_select(
                open_el=self.get_elements("master_select_open_btn"),
                parent_el=self.get_elements("master_select_parent_xpath"),
                value=masterName
            )

    def input_receive_count(self,receiveCount):
        """输入领用数量"""
        self.input_message(self.get_elements("sparePart_count_input"),receiveCount)

    def input_receive_remark(self,receiveRemark):
        """输入领用备注信息"""
        self.input_message(self.get_elements("remark_input"),receiveRemark)

    def click_delete_sparePart(self):
        """点击领用页面删除备件按钮"""
        self.click_button(self.get_elements("sparePart_del_btn"))

    def get_receive_first_info(self):
        """获取领用页面第一条备件所有信息"""
        return self.get_text(self.get_elements("receive_first_info"))

    def click_save_receive(self):
        """点击保存领用"""
        self.click_button(self.get_elements("save_btn"))

    def get_company_inventory_count(self):
        """获取公司库存数量"""
        try:
            return int(self.get_text(self.get_elements("all_inventory_count")))
        except:
            return 0

    def get_master_inventory_count(self):
        """获取师傅库存数量: 师傅库存备件第二次添加的相同条码的备件回生成两条库存记录 BUG """

        # 初始化数量为 0
        count = 0
        getCount = 0
        for i in range(1,10):
            try:
                getCount = int(self.get_text(
                    self.get_elements("master_inventory_count").replace("+num+",str(i))))
            except:
                break
            finally:
                count += getCount
        return count

    def select_search_master_name(self,masterName):
        """选择搜索师傅名称"""

        if masterName != "":
            self.sleep(2)
            self.operate_not_select(
                open_el=self.get_elements("search_master_open_btn"),
                parent_el=self.get_elements("search_master_parent_xpath"),
                value=masterName
            )

    def input_receive_start_time(self,startDate):
        """输入师傅领用开始时间"""
        if startDate != "":
            self.input_message(self.get_elements("receive_start_time_input"),startDate)

    def input_receive_end_time(self,endDate):
        """输入师傅领用结束日期"""
        if endDate != "":
            self.input_message(self.get_elements("receive_end_time_input"),endDate)

    def input_sparePart_number(self,spartPartNumber):
        """输入备件条码"""
        self.input_message(self.get_elements("sparePart_number_input"),spartPartNumber)

    def input_sparePart_name(self,sparePartName):
        """输入备件名称"""
        self.input_message(self.get_elements("sparePart_name_input"),sparePartName)

    def click_search_btn(self):
        """点击搜素按钮"""
        self.click_button(self.get_elements("search_receive_log_btn"))

    def get_first_search_info(self):
        """获取搜索后的第一条信息"""
        return self.get_text(self.get_elements("search_first_info"))

    def click_export_btn(self):
        """点击导出按钮"""
        self.click_button(self.get_elements("export_btn"))

    def get_export_file_list(self):
        """获取导出默认文件夹路径的所有文件,返回一个列表"""

        # 导出的excel列表
        export_excel_list = os.listdir(exportFilePath)
        # 按创建时间排序
        new_list = sorted(export_excel_list,key=lambda x:os.path.getctime(os.path.join(exportFilePath,x)))
        # 获取最后一个excel就是最新导出的
        return new_list[-1]


