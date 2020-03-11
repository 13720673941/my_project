# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/31 14:07

from public.common.basePage import BasePage
from config.urlConfig import *

class AddSparePartPage(BasePage):

    """
        【添加备件页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中添加备件页面的元素信息"""
        return read_config_data("add_spare_part_page",option,elementDataPath)

    def enter_company_inventory_page(self):
        """进入备件库存页面"""
        self.open_url(company_inventory_url,self.get_elements("add_sparePart_btn"))

    def click_add_new_sparePart(self):
        """点击新增备件按钮"""
        self.click_button(self.get_elements("add_sparePart_btn"))

    def input_add_sparePart_name(self,sparePartName):
        """输入添加的备件名称"""
        self.input_message(self.get_elements("sparePart_name_add_input"),sparePartName)

    def select_add_sparePart_type(self,sparePartType):
        """选择添加的备件类型"""

        if sparePartType != "":
            self.operate_not_select(
                open_el=self.get_elements("sparePart_type_add_open_btn"),
                parent_el=self.get_elements("sparePart_type_parent_xpath"),
                value=sparePartType
            )

    def select_measuring_unit(self,measuringUnit):
        """选择计量单位"""

        if measuringUnit != "":
            self.operate_not_select(
                open_el=self.get_elements("measuring_unit_open_btn"),
                parent_el=self.get_elements("measuring_unit_parent_xpath"),
                value=measuringUnit
            )

    def input_add_sparePart_number(self,sparePartNumber):
        """输入备件条码"""
        self.input_message(self.get_elements("sparePart_number_input"),sparePartNumber)

    def input_add_sparePart_brand(self,sparePartBrands):
        """输入备件品牌"""
        self.input_message(self.get_elements("sparePart_brand_input"),sparePartBrands)

    def select_sparePart_from(self,sparePartFrom):
        """选择备件来源"""

        if sparePartFrom != "":
            self.operate_not_select(
                open_el=self.get_elements("sparePart_from_open_btn"),
                parent_el=self.get_elements("sparePart_from_parent_xpath"),
                value=sparePartFrom
            )

    def input_sparePart_type_number(self,typeNumber):
        """输入备件型号"""
        self.input_message(self.get_elements("sparePart_type_number_input"),typeNumber)

    def select_use_kind(self,isSelect):
        """选择适用品类"""

        if isSelect == "True":
            # 统计所有的品类个数信息
            kind_count,kind_list = self.get_element_count(
                parentEl=self.get_elements("use_kind_parent_xpath"),childEl='label')
            # 选择全部的适用品类信息
            for i in range(1,kind_count+1):
                try:
                    self.click_button(self.get_elements("use_kind_select_input").replace("+num+",str(i)))
                except:
                    raise TimeoutError("Not find spare part use kind of {} kind in add page !".format(str(i)))

    def operate_up_loading_picture(self,isLoading):
        """操作上传图片默认传一张就好了多了耗时间"""

        if isLoading == "True":
            # 加载图片列表
            Plist = os.listdir(picturePath)
            # 循环上传
            for i in range(5):
                try:
                    Picture = picturePath + Plist[i]
                    self.sleep(2)
                    self.input_message(self.get_elements("loading_up_picture"),message=Picture)
                    self.log.info(' * Uploading picture: {0} . '.format(Picture))
                except:
                    raise Exception(' * Uploading is anomaly ! ')

    def input_into_inventory_price(self,intoStorePrice):
        """输入入库价格"""
        self.input_message(self.get_elements("into_store_price_input"),intoStorePrice)

    def input_user_buy_price(self,useBuyPrice):
        """输入零售价格"""
        self.input_message(self.get_elements("user_buy_price_input"),useBuyPrice)

    def select_old_return_btn(self):
        """选择旧件返回备件操作"""
        self.click_button(self.get_elements("old_sparePart_return_btn"))

    def select_old_not_return_btn(self):
        """选择旧件不返回按钮"""
        self.click_button(self.get_elements("old_sparePart_not_return_btn"))

    def click_add_save_btn(self):
        """点击保存备件按钮"""
        self.sleep(2)
        self.click_button(self.get_elements("add_save_btn"))

    def get_first_row_info(self):
        """获取第一行备件所有信息"""
        try:
            return self.get_text(self.get_elements("first_row_all_info"))
        except:
            raise TimeoutError("Not Find first spare part in list page !")
