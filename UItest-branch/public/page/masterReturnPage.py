# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 16:34

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By

class MasterReturnPage(BasePage):

    """
    【备件管理】-【师傅返还】页面
    """

    # 师傅返还按钮
    master_return_btn = (By.XPATH,'//a[contains(text(),"师傅返还")]')
    # 调拨出库打开按钮
    open_allot_out_btn = (By.XPATH,'//label[contains(text(),"调拨出库")]/..//div/div/span[1]')
    # 调拨出库下拉父节点
    allot_out_parent_element = (By.XPATH,'//label[contains(text(),"调拨出库")]/..//ul[2]')
    # 返还页面备件条码输入框
    return_sp_number_input = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[2]//input[2]')
    # 备件条码模糊匹配下拉框父节点
    sp_number_parent_element = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[2]//ul[2]/li[1]')
    # 返还页面备件名称输入框
    return_sp_name_input = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[3]//input[2]')
    # 备件名称模糊匹配下拉框父节点
    sp_name_parent_element = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[3]//ul[2]/li[1]')
    # 师傅匹配的备件当前库存数量
    master_sp_inventory_count = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[7]')
    # 返还数量输入框
    return_count_input = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]/td[8]/div//input')
    # 保存按钮
    save_return_info = (By.XPATH,'//div[contains(text(),"工程师返还")]/../..//button[2]')
    # 获取模糊匹配的备件
    search_sp_info = (By.XPATH,'(//tr[@class="ivu-table-row"])[4]')


    def click_master_return_button(self):
        """点击师傅返还"""
        self.click_button(self.master_return_btn)

    def select_return_master_name(self,master_name):
        """选择返还备件的师傅名称"""
        self.operate_not_select(
            open_el=self.open_allot_out_btn,
            parent_el=self.allot_out_parent_element,
            value=master_name
        )

    def input_spare_part_number(self,sp_number):
        """输入备件条码"""
        self.input_message(self.return_sp_number_input,sp_number)
        # 点击下备件条码输入框弹出匹配结果
        self.click_button(self.return_sp_number_input)
        # 移动鼠标
        self.mouse_move_to_element(self.save_return_info)

    def click_spare_part_number(self):
        """选择模糊匹配的备件条码"""
        self.click_button(self.sp_number_parent_element)

    def get_search_sp_number(self):
        """获取模糊匹配的备件条码"""

        try:
            sp_number = self.get_text(self.sp_number_parent_element)
        except:
            sp_number = "没有按条码匹配出备件"

        return sp_number

    def input_spare_part_name(self,sp_name):
        """输入备件名称"""
        self.input_message(self.return_sp_name_input,sp_name)
        # 点击下备件名称输入框弹出匹配结果
        self.click_button(self.return_sp_name_input)
        # 移动鼠标
        self.mouse_move_to_element(self.save_return_info)

    def click_spare_part_name(self):
        """选择模糊匹配的备件名称"""
        self.click_button(self.sp_name_parent_element)

    def get_search_sp_name(self):
        """获取模糊匹配的备件名称"""

        try:
            sp_name = self.get_text(self.sp_name_parent_element)
        except:
            sp_name = "没有按名称匹配出备件"

        return sp_name

    def get_master_inventory_count(self):
        """获取师傅备件库存数量"""

        try:
            master_inventory = self.get_text(self.master_sp_inventory_count)
        except:
            master_inventory = "没有获取到师傅库存"

        return master_inventory

    def input_sp_return_count(self,sp_count):
        """输入备件返还数量"""
        self.input_message(self.return_count_input,sp_count)

    def get_input_return_count(self):
        """获取输入的返还数量大于库存会自动变为师傅最大库存值"""

        try:
            input_number = self.get_att(self.return_count_input,"value")
        except:
            input_number = "没有获取到输入的库存"

        return input_number

    def click_save_button(self):
        """点击返还保存"""
        self.click_button(self.save_return_info)

    def get_search_sp_all_info(self):
        """获取模糊匹配的备件的全部信息"""

        first_row_info = self.get_text(self.search_sp_info)
        # 第一行默认的没有备件信息，用删除字段判断是否有备件匹配出来
        if "删除" not in first_row_info:
            return "没有模糊匹配出备件信息"
        else:
            return first_row_info
