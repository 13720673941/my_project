# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 17:40

from public.common.basePage import BasePage
from config.urlConfig import *

class MasterListPage(BasePage):

    """ 师傅列表页面: 邀请师傅、服务设置、禁止派单、开启派单等 """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中登录页面的元素信息"""
        return read_config_data("master_list_page",option,elementDataPath)

    def enter_master_list_page(self):
        """进入师傅列表页面"""
        self.open_url(master_list_url,self.get_elements("add_master_btn"))

    def click_add_master_btn(self):
        """点击添加师傅按钮"""
        self.click_button(self.get_elements("add_master_btn"))

    def input_master_phone_num(self,phoneNumber):
        """输入师傅手机号"""
        self.input_message(self.get_elements("master_phone_input"),phoneNumber)

    def get_msg_of_master_no_reg(self):
        """获取未注册师傅的提示信息"""
        return self.get_text(self.get_elements("visit_no_reg_master_msg"))

    def click_master_name_input(self):
        """点击师傅姓名输入框自动带出名字"""
        self.click_button(self.get_elements("master_name_input"))

    def input_master_name(self,masterName):
        """输入师傅姓名"""
        self.clear_input(self.get_elements("master_name_input"))
        self.sleep(1)
        self.input_message(self.get_elements("master_name_input"),masterName)

    def get_master_phe_input_att(self):
        """获取师傅手机号输入框属性判断是否为空"""
        return self.get_att(self.get_elements("master_phone_input"),"class")

    def get_master_name_input_att(self):
        """获取师傅名称输入框属性判断是否为空"""
        return self.get_att(self.get_elements("master_name_input"),"class")

    def get_master_name_input_value(self):
        """获取师傅名称的字段"""
        return self.get_att(self.get_elements("master_name_input"),"value")

    def click_confirm_add_master(self):
        """点击确定添加师傅"""
        self.click_button(self.get_elements("add_master_confirm_btn"))

    def input_keyword_for_search(self,searchWord):
        """输入关键词搜索师傅"""
        self.clear_input(self.get_elements("master_search_input"))
        self.sleep(1)
        self.input_message(self.get_elements("master_search_input"),searchWord)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("master_search_btn"))

    def get_first_master_info(self):
        """获取第一个师傅的所有信息"""
        return self.get_text(self.get_elements("first_master_info"))

    def click_del_visit_master(self):
        """撤销师傅邀请"""
        self.click_button(self.get_elements("del_master_teamwork_btn"))
        self.sleep(1)
        # 确认弹窗
        self.click_button(self.get_elements("confirm_operate_btn"))

    def find_roll_button(self):
        """找到拖动条"""
        return self.get_element(self.get_elements("roll_btn"))

    def roll_right_to_operate_btn(self):
        """右滑动页面找到按钮"""

        # 点击并且保持左鼠标键不放
        self.sleep(1)
        self.click_and_hold_btn(self.find_roll_button())
        # 获取滑块y坐标位置
        drag_button_y = self.find_roll_button().location['y']
        # 滑动到最右边
        self.roll_element_by_offset(x_offset=1000,y_offset=drag_button_y)
        self.sleep(2)

    def click_stop_send_order(self):
        """点击师傅禁止派单"""

        # 先判断按钮是否在页面，有时候是恢复派单按钮
        if self.is_display(self.get_elements("stop_send_order_btn")):
            pass
        else:
            self.click_button(self.get_elements("open_send_order_btn"))
            self.sleep(1)
        # 确定按钮的是否为禁止派单，再点击按钮
        self.click_button(self.get_elements("stop_send_order_btn"))
        self.click_button(self.get_elements("confirm_operate_btn"))

    def click_open_send_order(self):
        """点击恢复派单"""

        # 先判断按钮是否在页面，有时候是恢复派单按钮
        if self.is_display(self.get_elements("open_send_order_btn")):
            pass
        else:
            self.click_button(self.get_elements("stop_send_order_btn"))
            self.sleep(1)
            self.click_button(self.get_elements("confirm_operate_btn"))
        # 确定按钮的是否为禁止派单，再点击按钮
        self.click_button(self.get_elements("open_send_order_btn"))

    def click_server_set_btn(self):
        """点击服务设置按钮"""
        self.click_button(self.get_elements("server_set_btn"))

    def input_master_remark(self,masterRemark):
        """输入师傅备注信息"""
        self.clear_input(self.get_elements("master_remark_input"))
        self.sleep(1)
        self.input_message(self.get_elements("master_remark_input"),masterRemark)

    def clear_server_type(self):
        """清除师傅配置的服务类型"""

        # 获取师傅的服务配置信息
        master_server_info = self.get_text(self.get_elements("master_server_type_info"))
        # 解析师傅的服务信息
        if "," in master_server_info:
            # 师傅的服务类型放到列表中
            server_info_list = master_server_info.split(",")
            for server in server_info_list:
                # 循环点击清除设置
                self.click_button(
                    self.get_elements("server_type_select_input").replace("+serverType+",server))
        else:
            self.click_button(
                self.get_elements("server_type_select_input").replace("+serverType+",master_server_info))

    def select_server_type(self,serverList):
        """选择师傅服务类型"""

        # 判断传入的参数数据类型
        if type(serverList).__name__ != "list":
            raise TypeError("{} type error ! you must have a list type !".format(serverList))
        # 循环遍历服务类型列表中的值
        for server in serverList:
            self.click_button(self.get_elements("server_type_select_input").replace("+serverType+",server))

    def clear_kinds_type(self):
        """清除师傅配置的服务品类"""

        # 获取师傅的服务品类信息
        master_kinds_info = self.get_text(self.get_elements("master_kinds_type_info"))
        # 解析师傅的服务品类信息
        if "," in master_kinds_info:
            # 师傅的服务品类放到列表中
            kinds_info_list = master_kinds_info.split(",")
            for kind in kinds_info_list:
                # 循环点击清除设置
                self.click_button(
                    self.get_elements("kind_type_select_input").replace("+kindType+",kind))
        else:
            self.click_button(
                self.get_elements("kind_type_select_input").replace("+kindType+",master_kinds_info))

    def select_kinds_type(self,kindsList):
        """选择师傅服务品类"""

        # 判断传入的参数数据类型
        if type(kindsList).__name__ != "list":
            raise TypeError("{} type error ! you must have a list type !".format(kindsList))
        # 循环遍历服务品类列表中的值
        for kind in kindsList:
            self.sleep(1)
            self.click_button(self.get_elements("kind_type_select_input").replace("+kindType+",kind))

    def clear_master_server_place(self):
        """清除师傅服务区域"""

        # 获取师傅服务区域
        server_place = self.get_text(self.get_elements("master_server_place_type"))
        # 获取全部省的子元素列表和总和
        province_count,element_list = self.get_element_count(self.get_elements("province_parent_path"))
        # 循环输出所有的省份
        for i in range(1,province_count):
            self.sleep(1)
            if element_list[i].text in server_place:
                try:
                    # 点击选择框
                    self.click_button(
                        self.get_elements("server_place_select_input").replace("+num+",str(i+1)))
                    # 流程简化只选择一个服务区域
                    break
                except:
                    raise Exception("click master server place select input error !")

    def select_server_province(self,provinceList):
        """选择师傅服务区域"""

        # 判断传入的参数数据类型
        if type(provinceList).__name__ != "list":
            raise TypeError("{} type error ! you must have a list type !".format(provinceList))
        # 获取全部省的子元素列表和总和
        province_count,element_list = self.get_element_count(self.get_elements("province_parent_path"))
        # 循环输出所有的省份
        for i in range(province_count):
            self.sleep(1)
            if element_list[i].text in provinceList:
                try:
                    # 点击选择框
                    self.click_button(
                        self.get_elements("server_place_select_input").replace("+num+",str(i+1)))
                    # 流程简化只选择一个服务区域
                    break
                except:
                    raise Exception("click master server place select input error !")

    def clear_master_location(self):
        """清除师傅位置信息"""
        self.click_button(self.get_elements("master_place_clear_btn"))

    def click_set_server_save(self):
        """点击确定保存服务设置"""
        self.click_button(self.get_elements("server_set_confirm_btn"))




