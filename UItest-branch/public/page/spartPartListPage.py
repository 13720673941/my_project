# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/2/24 17:33

from public.common.basePage import BasePage
from config.urlConfig import *

class SparePartListPage(BasePage):

    """
        【备件列表页面：编辑、删除、搜索备件功能】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_company_inventory_page(self):
        """进入备件库存页面"""
        self.open_url(company_inventory_url,self.get_elements("sparePart_del_btn"))

    def get_elements(self,option):
        """获取element_data文件中备件列表页面的元素信息"""
        return read_config_data("spare_part_list_page",option,elementDataPath)

    def input_search_sparePart_number(self,sparePartNumber):
        """输入备件条码"""

        # 页面有三个元素循环查找
        for i in range(1,4):
            try:
                self.input_message(
                    self.get_elements("sparePart_number_search_input").replace("+num+",str(i)),sparePartNumber)
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find spare part number search input !")
                else:
                    continue

    def input_search_sparePart_name(self,sparePartName):
        """输入备件名称"""

        # 页面有三个元素循环查找
        for i in range(1,4):
            try:
                self.input_message(
                    self.get_elements("sparePart_name_search_input").replace("+num+",str(i)),sparePartName)
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find spare part name search input !")
                else:
                    continue

    def input_search_sparePart_brand(self,sparePartBrand):
        """输入备件品牌"""

        # 页面有三个元素循环查找
        for i in range(1,4):
            try:
                self.input_message(
                    self.get_elements("sparePart_brand_search_input").replace("+num+",str(i)),sparePartBrand)
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find spare part brand search input !")
                else:
                    continue

    def select_search_sparePart_type(self,sparePartType):
        """选择备件类型"""

        for i in range(1,5):
            try:
                openTypeButton = self.get_elements("sparePart_type_search_open_btn").replace("+num+",str(i))
                if sparePartType != "":
                    self.operate_not_select(
                        open_el=openTypeButton,
                        parent_el=self.get_elements("sparePart_type_search_parent_xpath"),
                        value=sparePartType
                    )
                    break
            except:
                if i == 4:
                    raise TimeoutError("Not find spare part type open button of select !")
                else:
                    continue

    def select_search_use_for_kind(self,useKind):
        """选择适用品类"""

        for i in range(1,4):
            try:
                openUseKindButton = self.get_elements("sparePart_kind_open_btn").replace("+num+",str(i))
                if useKind != "":
                    self.operate_not_select(
                        open_el=openUseKindButton,
                        parent_el=self.get_elements("sparePart_kind_parent_xpath"),
                        value=useKind
                    )
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find spare part use kind open button of select !")
                else:
                    continue

    def click_search_button(self):
        """点击搜索按钮"""

        for i in range(1,4):
            try:
                self.click_button(self.get_elements("sparePart_search_btn").replace("+num+",str(i)))
                break
            except:
                if i == 3:
                    raise TimeoutError("Not find spare part search button in page !")
                else:
                    continue

    def get_first_row_info(self):
        """获取第一行备件所有信息"""
        return self.get_text(self.get_elements("first_row_all_info"))

    def select_first_sparePart(self,sparePartName):
        """选择第一条备件"""
        try:
            # 先搜索备件默认点击第一个备件的修改按钮
            self.input_search_sparePart_name(sparePartName)
            self.click_search_button()
            # 点击修改备件按钮
            self.sleep(2)
            self.click_button(self.get_elements("first_sparePart_select_input"))
        except:
            raise TimeoutError("Not find spare part in list !")

    def click_del_sparePart_btn(self):
        """点击删除备件按钮"""

        self.click_button(self.get_elements("sparePart_del_btn"))
        self.sleep(1)
        # 点击确定删除备件
        self.click_button(self.get_elements("confirm_del_btn"))

    def click_alter_button(self,sparePartName):
        """点击修改备件按钮"""

        # 先搜索备件默认点击第一个备件的修改按钮
        self.input_search_sparePart_name(sparePartName)
        self.click_search_button()
        # 点击修改备件按钮
        self.sleep(2)
        self.click_button(self.get_elements("alter_sparePart_btn"))

    def input_alter_sparePart_name(self,sparePartName):
        """输入修改备件名称"""

        # 清空备件名称
        self.clear_input(self.get_elements("alter_sparePart_name"))
        # 输入新备件名称
        self.input_message(self.get_elements("alter_sparePart_name"),sparePartName)

    def click_alter_save_btn(self):
        """点击修改保存按钮"""
        self.click_button(self.get_elements("alter_save_btn"))