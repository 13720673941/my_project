# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/4 10:57

from public.common.basePage import BasePage
from config.urlConfig import *

class CreateGroupPage(BasePage):

    """ 【创建圈子页面】 """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取创建圈子页面的元素"""
        return read_config_data("my_create_group_page",option,elementDataPath)

    def enter_my_group_list_page(self):
        """进入我创建的圈子列表页面"""
        self.open_url(my_create_group_list,self.get_elements("create_group_btn"))

    def click_create_group_btn(self):
        """点击创建圈子按钮"""
        self.click_button(self.get_elements("create_group_btn"))

    def input_group_name(self,groupName):
        """输入圈子名称"""
        self.input_message(self.get_elements("group_name_input"),groupName)

    def select_service_area(self,serviceArea):
        """
        选择服务区域节省脚本运行时间默认服务单独省市区
        :param serviceArea {"省":"陕西省","市":"西安市","区":"碑林区"}
        """

        if serviceArea != "":
            # 判断传入字段的类型 省市区
            if type(serviceArea).__name__ != "dict":
                raise TypeError(" Type is error, you must have a dict type ! usage: {省：陕西省，市：西安市，区：碑林区} .")
            # 获取全部省份信息
            provinceCount,provinceList = self.get_element_count(
                parentEl=self.get_elements("all_province_parent_element"),childEl="a")
            # 遍历省份切换到服务省份
            for i in range(provinceCount):
                self.sleep(1)
                try:
                    if provinceList[i].text == serviceArea["省"]:
                        if serviceArea["市"] == "" and serviceArea["区"] == "":
                            # 选择全部的省份为服务区域
                            self.click_button(self.get_elements("select_all_province_input").replace("+num+",str(i+1)))
                        else:
                            # 点击省份显示出全部市
                            self.click_button(self.get_elements("province_click_btn").replace("+num+",str(i+1)))
                        break
                except:
                    if i == provinceCount-1:
                        raise TimeoutError("Not find service province: {} in page.".format(serviceArea["省"]))
                    else:
                        continue
            # 选择服务市份
            self.sleep(2)
            if serviceArea["市"] != "":
                # 获取全部市份的信息
                cityCount,cityList = self.get_element_count(
                    parentEl=self.get_elements("all_city_parent_element"),childEl="a")
                # 遍历市份选择服务城市
                for i in range(cityCount):
                    self.sleep(1)
                    try:
                        if cityList[i].text == serviceArea["市"]:
                            if serviceArea["区"] == "":
                                # 选择全部的城市为服务市
                                self.click_button(self.get_elements("select_all_city_input").replace("+num+",str(i+1)))
                            else:
                                # 点击城市显示出全部市
                                self.click_button(self.get_elements("city_click_btn").replace("+num+",str(i+1)))
                            break
                    except:
                        if i == provinceCount-1:
                            raise TimeoutError("Not find service city: {} in page.".format(serviceArea["市"]))
                        else:
                            continue
            # 选择服务区县
            self.sleep(2)
            if serviceArea["区"] != "":
                # 获取全部市份的信息
                areaCount,areaList = self.get_element_count(
                    parentEl=self.get_elements("all_area_parent_element"),childEl="a")
                # 遍历区县选择服务区县
                for i in range(areaCount):
                    self.sleep(1)
                    try:
                        if areaList[i].text in serviceArea["区"]:
                            self.click_button(self.get_elements("select_area_input").replace("+num+",str(i+1)))
                    except:
                        if i == provinceCount-1:
                            raise TimeoutError("Not find service area: {} in page.".format(serviceArea["区"]))
                        else:
                            continue

    def select_service_type(self,serviceType):
        """
        选择服务类型可以是多个一起，默认传入列表格式
        :param serviceType 服务类型列表 usage: "安装","维修","保养"
        """

        if serviceType != "":
            # 判断传入字段的格式类型
            if type(serviceType).__name__ != "list":
                raise TypeError(" Service type: {} text is error, you must have a list .".format(serviceType))
            # 循环遍历服务类型列表
            for service in serviceType:
                self.sleep(1)
                try:
                    self.click_button(self.get_elements("server_type_btn").replace("+serviceType+",service))
                except:
                    raise TypeError(" Service type: {} not find in page of type list .".format(service))

    def select_service_brands(self,serviceBrands):
        """
        选择服务品牌可以是多个一起，默认传入列表格式
        :param serviceType 服务类型列表 usage: ["海尔","美的","蓝魔"]
        """

        if serviceBrands != "":
            # 判断传入字段的格式类型
            if type(serviceBrands).__name__ != "list":
                raise TypeError(" Service brands: {} text is error, you must have a list .".format(serviceBrands))
            # 循环遍历服务品牌列表
            for brands in serviceBrands:
                self.sleep(1)
                try:
                    self.click_button(self.get_elements("server_brands_btn").replace("+serviceBrands+",brands))
                except:
                    raise TypeError(" Service brands: {} not find in page of type list .".format(brands))

    def click_add_brands_btn(self):
        """点击添加品牌按钮"""
        self.click_button(self.get_elements("add_service_brands_btn"))

    def input_new_brands_name(self,brandsName):
        """输入品牌名称"""

        # 清除输入框
        self.clear_input(self.get_elements("new_brands_name_input"))
        self.input_message(self.get_elements("new_brands_name_input"),brandsName)

    def click_confirm_add_button(self):
        """点击确认添加按钮"""
        self.click_button(self.get_elements("confirm_add_brands_btn"))

    def get_all_service_brands(self):
        """获取页面所有的服务品牌信息列表"""
        return self.get_text(self.get_elements("all_service_brands_text"))

    def select_service_kinds(self,serviceKinds):
        """
        选择服务品类可以是多个一起，默认传入列表格式
        :param serviceKinds 服务类型列表 usage: ["空调","冰箱","洗衣机"]
        """

        if serviceKinds != "":
            # 判断传入字段的格式类型
            if type(serviceKinds).__name__ != "list":
                raise TypeError(" Service kinds: {} text is error, you must have a list .".format(serviceKinds))
            # 循环遍历服务品牌列表
            for kinds in serviceKinds:
                self.sleep(1)
                try:
                    self.click_button(self.get_elements("server_kinds_btn").replace("+serviceKinds+",kinds))
                except:
                    raise TypeError(" Service brands: {} not find in page of type list .".format(kinds))

    def select_charge_rule(self,isCharge):
        """
        选择收费标准
        :param isCharge -> "设置" / "免费"
        """
        self.click_button(self.get_elements("charge_rules_name_btn").replace("+ruleName+",isCharge))

    def select_charge_mode(self,chargeModeName):
        """
        选择收费模式
        :param chargeModeName: "金额" / "比例"
        """
        if chargeModeName != "":
            self.click_button(self.get_elements("charge_mode_name_btn").replace("+chargeMode+",chargeModeName))

    def input_start_charge_count(self,startChargeCount):
        """
        输入起收单数
        :param startChargeCount 起收单数
        """
        if startChargeCount != "":
            # 这里需要清除原来的数据使用clear()方法无效->获取输入框字段使用退格键删除
            text = self.get_att(self.get_elements("start_charge_order_count_input"),"value")
            for i in range(len(text)):
                self.use_keys_operate(self.get_elements("start_charge_order_count_input"),operate="退格")
            # 输入单数
            self.input_message(self.get_elements("start_charge_order_count_input"),startChargeCount)

    def input_charge_amount(self,chargeAmount):
        """
        输入每单收取费用金额
        :param chargeAmount 每单圈子所收取的费用金额
        """
        if chargeAmount != "":
            text = self.get_att(self.get_elements("charge_amount_input"),"value")
            for i in range(len(text)):
                self.use_keys_operate(self.get_elements("charge_amount_input"),operate="退格")
            self.input_message(self.get_elements("charge_amount_input"),chargeAmount)

    def select_send_order_way(self,sendOrderWay):
        """
        选择派单方式
        :param sendOrderWay 派单方式 -> 派单方自主选择/自动派单/群内抢单/群主派单
        """
        self.operate_select(self.get_elements("send_order_way_select"),value=sendOrderWay)

    def select_settle_way(self,settleWay):
        """
        选择订单结算方式
        :param settleWay: 字段类型 -> 预付给平台担保 / 无需预付
        """
        self.click_button(self.get_elements("settle_way_btn").replace("+settleWay+",settleWay))

    def input_group_notice(self,groupNotice="."):
        """输入圈子公告"""
        self.input_message(self.get_elements("group_notice_input"),groupNotice)

    def click_confirm_create_btn(self):
        """点击确认创建圈子按钮"""
        self.click_button(self.get_elements("confirm_create_group_btn"))

    def create_success_is_displayed(self):
        """判断创建成功的字段在页面上显示"""
        return self.is_display(self.get_elements("is_create_success_text"))

    def create_group_main(self,name,area,type,brands,kinds,isCharge,
                          sendWay,settleWay,chargeMode="金额",startCount="0",charge="0.05"):
        """创建圈子主程序"""

        self.log.info("-=【创建圈子】=-")
        # 进入创建圈子页面
        self.enter_my_group_list_page()
        # 点击创建圈子按钮
        self.click_create_group_btn()
        # 输入圈子名称
        self.input_group_name(name)
        # 选择服务区域
        self.select_service_area(area)
        # 选择服务类型
        self.select_service_type(type)
        # 选择服务品牌
        self.select_service_brands(brands)
        # 选择服务品类
        self.select_service_kinds(kinds)
        # 选择收费设置
        self.select_charge_rule(isCharge)
        if isCharge != "免费":
            # 选择收费模式
            self.select_charge_mode(chargeMode)
            # 输入起手单数
            self.input_start_charge_count(startCount)
            # 输入费用金额
            self.input_charge_amount(charge)
        # 选择派单方式
        self.select_send_order_way(sendWay)
        # 选择结算方式
        self.select_settle_way(settleWay)
        # 输入圈子公告
        self.input_group_notice()
        self.sleep(1)
        # 点击确定创建
        self.click_confirm_create_btn()
        self.sleep(1)
        if self.create_success_is_displayed():
            self.log.info(" ** 圈子：{} 创建成功 ！".format(name))
        else:
            raise Exception(" ** 圈子：{} 创建失败 ！".format(name))