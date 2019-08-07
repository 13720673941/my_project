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
    # 未注册师傅提示发送短信字段
    visit_no_reg_master_msg = (By.XPATH,'//label[text()="师傅手机号："]/../div/div')
    # 师傅备注输入框
    master_name_input = (By.XPATH,'//label[text()="师傅姓名："]/..//input')
    # 确定添加师傅
    add_master_confirm_btn = (By.XPATH,'//div[text()="添加师傅"]/../..//button[2]')
    # 师傅搜索框
    master_search_input = (By.XPATH,'//input[starts-with(@placeholder,"输入师傅姓名")]')
    # 搜索按钮
    master_search_btn = (By.XPATH,'//a[text()="搜索"]')
    # 获取第一行师傅所有信息
    first_master_info = (By.XPATH,'//tr[@class="ivu-table-row"][1]')
    # 撤销申请师傅合作//默认先搜索师傅再撤销
    del_master_teamwork_btn = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]//a[text()="撤销"]')
    # 确认弹窗操作按钮
    confirm_operate_btn = (By.XPATH,'//div[contains(text(),"？")]/..//a[2]')
    # 师傅禁止派单按钮
    master_stop_please_btn = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]//a[text()="禁止派单"]')
    # 师傅恢复派单按钮
    master_open_please_btn = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]//a[text()="恢复派单"]')
    # 左右滑动托条按钮
    roll_btn = (By.XPATH, '//*[@class="ivu-table-body ivu-table-overflowX"]')
    # ===师傅服务设置===
    # 服务设置按钮
    server_set_btn = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]//a[1]')
    # 师傅备注输入框
    master_remark_input = (By.XPATH,'//label[text()="师傅备注："]/..//input')
    # 获取师傅服务类型配置
    master_server_type_info = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]/td[10]/div/div')
    # 获取师傅服务品类的配置
    master_kinds_type_info = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]/td[11]/div/div')
    # 获取师傅服务区域的配置
    master_server_place_type = (By.XPATH,'//tr[starts-with(@class,"ivu-table-row")][1]/td[12]/div/div')
    # 清除服务区域设置
    master_place_clear_btn = (By.XPATH,'//a[text()="清除"]')
    # 服务设置确定按钮
    server_set_confirm_btn = (By.XPATH,'//div[contains(text(),"服务设置")]/../..//button[2]')
    # 省份的父目录
    province_parent_path = (By.XPATH,'//div[@class="city-picker"][1]//ul')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_master_list_page(self):
        """进入师傅列表页面"""
        self.open_url(master_list_url)

    def click_add_master_btn(self):
        """点击添加师傅按钮"""
        self.click_button(self.add_master_btn)

    def input_master_phone_num(self,phe_num):
        """输入师傅手机号"""
        self.input_message(self.master_phone_input,phe_num)

    def get_msg_of_master_no_reg(self):
        """获取未注册师傅的提示信息"""
        return self.get_text(self.visit_no_reg_master_msg)

    def click_master_name_input(self):
        """点击师傅姓名输入框//自动带出名字"""
        self.click_button(self.master_name_input)

    def input_master_name(self,master_name):
        """输入师傅姓名"""
        self.clear_input(self.master_name_input)
        self.sleep(1)
        self.input_message(self.master_name_input,master_name)

    def get_master_phe_input_att(self):
        """获取师傅手机号输入框属性//判断是否为空"""
        return self.get_att(self.master_phone_input,"class")

    def get_master_name_input_att(self):
        """获取师傅名称输入框属性//判断是否为空"""
        return self.get_att(self.master_name_input, "class")

    def get_master_name_input_value(self):
        """获取师傅名称的字段"""
        return self.get_att(self.master_name_input,"value")

    def click_confirm_add_master(self):
        """点击确定添加师傅"""
        self.click_button(self.add_master_confirm_btn)

    def input_keyword_for_search(self,search_word):
        """输入关键词搜索师傅"""
        self.clear_input(self.master_search_input)
        self.sleep(1)
        self.input_message(self.master_search_input,search_word)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.master_search_btn)

    def get_first_master_info(self):
        """获取第一个师傅的所有信息"""
        return self.get_text(self.first_master_info)

    def click_del_visit_master(self):
        """撤销师傅邀请"""

        # 滑动托条点击
        self.roll_right_to_operate_btn()
        self.sleep(1)
        # 点击撤销按钮
        self.click_button(self.del_master_teamwork_btn)

    def find_roll_button(self):
        """找到拖动条"""
        return self.get_element(self.roll_btn)

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

    def click_master_stop_please(self):
        """点击师傅禁止派单"""

        # 先判断按钮是否在页面，有时候是恢复派单按钮
        if self.is_display(self.master_stop_please_btn):
            pass
        else:
            self.click_button(self.master_open_please_btn)
            self.sleep(1)
        # 确定按钮的是否为禁止派单，再点击按钮
        self.click_button(self.master_stop_please_btn)

    def click_master_open_please(self):
        """点击恢复派单"""

        # 先判断按钮是否在页面，有时候是恢复派单按钮
        if self.is_display(self.master_open_please_btn):
            pass
        else:
            self.click_button(self.master_stop_please_btn)
            self.sleep(1)
            self.click_confirm_window_operate()
        # 确定按钮的是否为禁止派单，再点击按钮
        self.click_button(self.master_open_please_btn)

    def click_confirm_window_operate(self):
        """点击确认弹窗操作"""
        self.click_button(self.confirm_operate_btn)

    def click_server_set_btn(self):
        """点击服务设置按钮"""
        self.click_button(self.server_set_btn)

    def input_master_remark(self,master_remark):
        """输入师傅备注信息"""
        self.clear_input(self.master_remark_input)
        self.sleep(1)
        self.input_message(self.master_remark_input,master_remark)

    def clear_server_type(self):
        """清除师傅配置的服务类型"""

        # 获取师傅的服务配置信息
        master_server_info = self.get_text(self.master_server_type_info)
        # 解析师傅的服务信息
        if "," in master_server_info:
            # 师傅的服务类型放到列表中
            server_info_list = master_server_info.split(",")
            for server in server_info_list:
                # 循环点击清除设置
                self.click_button(element=(By.XPATH,'//label[text()="服务类型："]/..//div/'
                                                    'label[contains(.,"'+server+'")]'))
        else:
            self.click_button(element=(By.XPATH, '//label[text()="服务类型："]/..//div/'
                                                 'label[contains(.,"'+master_server_info+'")]'))

    def select_server_type(self,server_list):
        """选择师傅服务类型"""

        # 循环遍历服务类型列表中的值
        for server in server_list:
            self.click_button(element=(By.XPATH,'//label[text()="服务类型："]/..//div/'
                                                'label[contains(.,"'+server+'")]'))

    def clear_kinds_type(self):
        """清除师傅配置的服务品类"""

        # 获取师傅的服务品类信息
        master_kinds_info = self.get_text(self.master_kinds_type_info)
        # 解析师傅的服务品类信息
        if "," in master_kinds_info:
            # 师傅的服务品类放到列表中
            kinds_info_list = master_kinds_info.split(",")
            for kind in kinds_info_list:
                # 循环点击清除设置
                self.click_button(element=(By.XPATH,'//label[text()="服务品类："]/..//div/'
                                                    'label[contains(.,"'+kind+'")]'))
        else:
            self.click_button(element=(By.XPATH, '//label[text()="服务品类："]/..//div/'
                                                 'label[contains(.,"'+master_kinds_info+'")]'))

    def select_kinds_type(self,kinds_list):
        """选择师傅服务品类"""

        # 循环遍历服务品类列表中的值
        for kind in kinds_list:
            self.click_button(element=(By.XPATH,'//label[text()="服务品类："]/..//div/'
                                                'label[contains(.,"'+kind+'")]'))

    def clear_master_server_place(self):
        """清除师傅服务区域"""

        # 获取师傅服务区域
        server_place = self.get_text(self.master_server_place_type)
        print(server_place)
        # 获取全部省的子元素列表和总和
        province_count,element_list = self.get_element_count(self.province_parent_path)
        print(element_list[0].text)
        # 循环输出所有的省份
        for i in range(1,province_count):
            self.sleep(1)
            if element_list[i].text in server_place:
                # 点击选择框
                self.click_button(element=(By.XPATH,'//div[@class="city-picker"][1]'
                                                    '//ul/li['+str(i+1)+']//input'))
                # 流程简化只选择一个服务区域
                break
            else:
                pass

    def select_server_province(self,province_list):
        """选择师傅服务区域"""

        # 获取全部省的子元素列表和总和
        province_count,element_list = self.get_element_count(self.province_parent_path)
        # 循环输出所有的省份
        for i in range(province_count):
            self.sleep(1)
            if element_list[i].text in province_list:
                # 点击选择框
                self.click_button(element=(By.XPATH,'//div[@class="city-picker"][1]'
                                                    '//ul/li['+str(i+1)+']//input'))
                # 流程简化只选择一个服务区域
                break
            else:
                pass

    def clear_master_location(self):
        """清除师傅位置信息"""
        self.click_button(self.master_place_clear_btn)

    def click_set_server_save(self):
        """点击确定保存服务设置"""
        self.click_button(self.server_set_confirm_btn)




