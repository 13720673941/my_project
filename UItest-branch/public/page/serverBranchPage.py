# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 15:27

from selenium.webdriver.common.by import By
from public.common.basepage import BasePage
from config.urlconfig import *
from public.common.logconfig import Log
log = Log()

class ServerBranchPage(BasePage):
    """
    客户管理-服务商列表页面
    """

    # 父路径该页面有两个一样的页面需要从根目录定位
    parent_xpath = '//div[@id="main"]/following-sibling::div[21]/'
    # 切换服务商的table按钮
    server_branch_table = (By.XPATH,'//a[contains(text(),"服务商")]')
    # 添加服务商按钮
    add_server_btn = (By.XPATH,'//a[text()="添加服务商"]')
    # 客户手机号输入框
    customer_phone_num_input = (By.XPATH,'//div[text()="添加服务商"]/../.././/input[1]')
    # 客户名称
    customer_name_input = (By.XPATH,'//div[text()="添加服务商"]/../.././/input[@placeholder="请输入客户名称"]')
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
    server_branch_remark = (By.XPATH,''+parent_xpath+'.//label[text()="客户备注："]/.././/input')
    # 合作类型派单
    teamwork_type_1 = (By.XPATH,''+parent_xpath+'.//label[text()="合作类型："]/.././/label[text()=" 派单"]')
    # 合作类型报单
    teamwork_type_2 = (By.XPATH,''+parent_xpath+'.//label[text()="合作类型："]/.././/label[text()=" 报单"]')
    # 合作类型返单
    teamwork_type_3 = (By.XPATH,''+parent_xpath+'.//label[text()="合作类型："]/.././/label[text()=" 返单"]')
    # 服务类型-不限
    server_type_not_limit = (By.XPATH,''+parent_xpath+'.//label[text()="服务类型："]/.././/label[contains(text(),"不限")]')
    # 其他服务类型的按钮
    server_type_of_other = (By.XPATH,''+parent_xpath+'.//label[text()="服务类型："]/.././/div[@class="ivu-row"]/div[2]')
    # 服务品牌-不限
    brands_of_not_limit = (By.XPATH,''+parent_xpath+'.//label[text()="服务品牌："]/.././/label[contains(text(),"不限")]')
    # 服务品牌其他品牌
    brands_of_other = (By.XPATH,''+parent_xpath+'.//label[text()="服务品牌："]/.././/div[@class="ivu-row"]/div[2]')
    # 服务品类-不限
    kinds_of_not_limit = (By.XPATH,''+parent_xpath+'.//label[text()="服务品类："]/.././/label[contains(text(),"不限")]')
    # 其他服务品类的父节点
    kinds_of_other = (By.XPATH,''+parent_xpath+'.//label[text()="服务品类："]/.././/div[@class="ivu-row"]/div[2]')
    # 第一个服务商的服务地址信息
    first_branch_address_info = (By.XPATH,'//*[@class="ivu-table-body ivu-table-overflowX"]/.//tr[1]/td[7]')
    # 服务省份父节点
    server_province_parent = (By.XPATH,''+parent_xpath+'.//div[text()="选择服务省份"]/../ul')
    # 服务市区父节点
    server_city_parent = (By.XPATH,''+parent_xpath+'.//div[text()="选择服务城市"]/../ul')
    # 服务区县父节点
    server_area_parent = (By.XPATH,''+parent_xpath+'.//div[text()="选择服务区/县"]/../ul')
    # 确定服务设置按钮
    confirm_teamwork_btn = (By.XPATH,''+parent_xpath+'.//div[contains(.,"服务设置")]/../../div[3]/div/button[2]')
    # 禁止派单按钮
    stop_please_btn = (By.XPATH,'//a[contains(.,"禁止派单")]')
    # 开启派单按钮
    open_please_btn = (By.XPATH,'//a[contains(.,"恢复派单")]')
    # 确定禁止/恢复
    confirm_please_btn = (By.XPATH,'//div[contains(text(),"是否")]/../div[4]/a[2]')
    # 选择属性表示字段
    is_select = "ivu-checkbox-wrapper-checked"

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_customer_list_page(self):
        """进入客户列表页面"""
        self.open_url(teamwork_branch_list_url)

    def click_server_branch_table(self):
        """点击切换服务商的table按钮"""
        self.click_button(self.server_branch_table)

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

    def clear_customer_name(self):
        """清空客户名字，验证不能为空"""
        self.clear_input(self.customer_name_input)

    def select_please_to_someone(self,is_select):
        """选择向他派单"""
        if is_select == "true":
            self.click_button(self.select_please_order)

    def select_instead_to_someone(self,is_select):
        """选择向他报单"""
        if is_select == "true":
            self.click_button(self.select_instead_order)

    def select_return_to_someone(self,is_select):
        """选择向他返单"""
        if is_select == "true":
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

    def find_roll_button(self):
        """获取滚动按钮"""
        return self.get_element(self.roll_btn)

    def click_and_roll_right_page(self):
        """向右边滑动页面展示，操作按钮"""

        # 点击并且保持左鼠标键不放
        self.sleep(1)
        self.click_and_hold_btn(self.find_roll_button())
        # 获取滑块y坐标位置
        drag_button_y = self.find_roll_button().location['y']
        # 滑动到最右边
        self.roll_element_by_offset(x_offset=500,y_offset=drag_button_y)
        self.sleep(2)

    def click_server_set_btn(self):
        """点击服务设置"""
        self.click_button(self.set_server_btn)

    def input_server_branch_remark(self,branch_remark):
        """输入服务商备注"""

        # 清除服务商备注
        self.clear_input(self.server_branch_remark)
        self.sleep(1)
        # 输入最新备注
        self.input_message(self.server_branch_remark,branch_remark)

    def clear_teamwork_type_1(self):
        """初始化合作类型: 派单"""

        # 获取元素的class属性，判断是否已经选取
        teamwork_type1_att = self.get_att(self.teamwork_type_1,"class")
        if self.is_select in teamwork_type1_att:
            self.select_teamwork_type_1()

    def select_teamwork_type_1(self):
        """选择合作类型：派单"""
        self.click_button(self.teamwork_type_1)

    def clear_teamwork_type_2(self):
        """初始化合作类型: 报单"""

        # 获取元素的class属性，判断是否已经选取
        teamwork_type1_att = self.get_att(self.teamwork_type_2,"class")
        if self.is_select in teamwork_type1_att:
            self.select_teamwork_type_2()

    def select_teamwork_type_2(self):
        """选择合作类型：报单"""
        self.click_button(self.teamwork_type_2)

    def clear_teamwork_type_3(self):
        """初始化合作类型: 返单"""

        # 获取元素的class属性，判断是否已经选取
        teamwork_type1_att = self.get_att(self.teamwork_type_3,"class")
        if self.is_select in teamwork_type1_att:
            self.select_teamwork_type_3()

    def select_teamwork_type_3(self):
        """选择合作类型：返单"""
        self.click_button(self.teamwork_type_3)

    # ======选择-授权服务类型操作======
    def clear_server_type(self):
        """初始化授权的服务类型"""

        # 先初始化-不限
        not_limit_attribute = self.get_att(self.server_type_not_limit,"class")
        if self.is_select in not_limit_attribute:
            self.click_button(self.server_type_not_limit)
        # 在初始化后面配置的服务类型
        # 获取可以选择的授权服务类型的个数和列表
        server_type_count,server_type_list = self.get_element_count(self.server_type_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(server_type_count):
            other_server_attribute = server_type_list[i].get_attribute("class")
            # 判断该字段是否在按钮的属性中在的话就是已经选择
            if self.is_select in other_server_attribute:
                self.sleep(1)
                server_type_list[i].click()

    def select_server_type_no_limit(self):
        """选择服务类型-不限"""
        self.click_button(self.server_type_not_limit)

    def select_server_type_of_other(self,server_name):
        """选择服务类型除-不限以外的"""

        # 获取可以选择的授权服务类型的个数和列表
        server_type_count,server_type_list = self.get_element_count(self.server_type_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(server_type_count):
            server_type_text = server_type_list[i].text
            # server_name 是个列表，类型比较多多次匹配
            if server_type_text in server_name:
                self.sleep(1)
                server_type_list[i].click()

    # ======选择-授权服务品牌操作======
    def clear_brands_type(self):
        """初始化授权-品牌"""

        # 先初始化-不限
        not_limit_attribute = self.get_att(self.brands_of_not_limit,"class")
        if self.is_select in not_limit_attribute:
            self.click_button(self.brands_of_not_limit)
        # 在初始化后面配置的品牌类型
        # 获取可以选择的授权品牌类型的个数和列表
        brands_type_count,brands_type_list = self.get_element_count(self.brands_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(brands_type_count):
            other_server_attribute = brands_type_list[i].get_attribute("class")
            # 判断该字段是否在按钮的属性中在的话就是已经选择
            if self.is_select in other_server_attribute:
                self.sleep(1)
                brands_type_list[i].click()

    def select_brands_type_no_limit(self):
        """选择服务品牌-不限"""
        self.click_button(self.brands_of_not_limit)

    def select_brands_type_of_other(self,brands_name):
        """选择品牌类型除-不限以外的"""

        # 获取可以选择的授权品牌类型的个数和列表
        brands_type_count,brands_type_list = self.get_element_count(self.brands_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(brands_type_count):
            # brands_name 是个列表，类型比较多多次匹配
            brands_type_text = brands_type_list[i].text
            # server_name 是个列表，类型比较多多次匹配
            if brands_type_text in brands_name:
                self.sleep(1)
                brands_type_list[i].click()

    # ======选择-授权服务品类操作======
    def clear_kinds_type(self):
        """初始化授权-品类"""

        # 先初始化-不限
        not_limit_attribute = self.get_att(self.kinds_of_not_limit,"class")
        if self.is_select in not_limit_attribute:
            self.click_button(self.kinds_of_not_limit)
        # 在初始化后面配置的品类类型
        # 获取可以选择的授权品类类型的个数和列表
        kinds_type_count,kinds_type_list = self.get_element_count(self.kinds_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(kinds_type_count):
            other_server_attribute = kinds_type_list[i].get_attribute("class")
            # 判断该字段是否在按钮的属性中在的话就是已经选择
            if self.is_select in other_server_attribute:
                self.sleep(1)
                kinds_type_list[i].click()

    def select_kinds_type_no_limit(self):
        """选择服务品类-不限"""
        self.click_button(self.kinds_of_not_limit)

    def select_kinds_type_of_other(self,kinds_name):
        """选择品类类型除-不限以外的"""

        # 获取可以选择的授权品类类型的个数和列表
        kinds_type_count,kinds_type_list = self.get_element_count(self.kinds_of_other,"label")
        # 循环输出按钮的属性判断是否选择
        for i in range(kinds_type_count):
            # brands_name 是个列表，类型比较多多次匹配
            kinds_type_text = kinds_type_list[i].text
            # server_name 是个列表，类型比较多多次匹配
            if kinds_type_text in kinds_name:
                self.sleep(1)
                kinds_type_list[i].click()

    def clear_server_address_info(self):
        """清空服务地址信息"""

        # 统计所有的省份
        provinces_count,all_provinces_element = self.get_element_count(parentEl=self.server_province_parent)
        # 判断省份下的区域是否全选 判断属性字段
        all_is_not_select = "ivu-checkbox-indeterminate"
        all_is_select = "ivu-checkbox-checked"
        # 遍历所有的省份的选择属性值，判断是否已经选择
        for i in range(1,provinces_count):
            # 获取该索引位置的省份的 label、span 元素的 class 属性
            span_attribute = self.get_att(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务省份"]/'
                                                            '../ul/li['+str(i)+']/.//label/span'),attribute="class")
            # 判断省份一下市区是全部选择还是漏选::全选单击清除，漏选双击清除
            if all_is_select in span_attribute:
                # 该情况为省份全选单击所选择的省份
                self.click_button(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务省份"]/'
                                                    '../ul/li['+str(i)+']/.//input'))
            elif all_is_not_select in span_attribute:
                # 该情况为漏选省份后面的地址双击省份清空所有
                self.mouse_double_click(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务省份"]/'
                                                      '../ul/li['+str(i)+']/.//input'))
            else:
                pass

    # ======选择省市区======
    def select_server_province(self,province_list):
        """选择服务省份"""

        # province_list 参数默认写成一个列表的类型
        # 统计所有的省份
        provinces_count,all_provinces_element = self.get_element_count(parentEl=self.server_province_parent)
        # 循环遍历所有的省份,第一个不能点击从2开始
        for i in range(1,provinces_count):
            try:
                province_name = all_provinces_element[i].text
                # 判断省份的名称在所要选择的省份列表中时，选择该省份
                if province_name in province_list:
                    self.sleep(1)
                    self.click_button(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务省份"]/'
                                                    '../ul/li['+str(i+1)+']/.//input'))
            except Exception as e:
                raise e

    def select_server_city(self,city_list):
        """选择服务市区"""

        # 统计所有的市区
        city_count,all_city_element = self.get_element_count(parentEl=self.server_city_parent)
        # 循环遍历所有的省份
        for i in range(1,city_count):
            try:
                city_name = all_city_element[i].text
                # 判断省份的名称在所要选择的省份列表中时，选择该省份
                if city_name in city_list:
                    self.sleep(1)
                    self.click_button(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务城市"]/'
                                                        '../ul/li['+str(i+1)+']/.//input'))
            except Exception as e:
                raise e

    def select_server_area(self,area_list):
        """选择服务区县"""

        # 统计所有的区县
        area_count,all_area_element = self.get_element_count(parentEl=self.server_area_parent)
        # 循环遍历所有的省份
        for i in range(1,area_count):
            try:
                area_name = all_area_element[i].text
                # 判断省份的名称在所要选择的省份列表中时，选择该省份
                if area_name in area_list:
                    self.sleep(1)
                    self.click_button(element=(By.XPATH,'//div[@id="main"]/following-sibling::div[21]/.//div[text()="选择服务区/县"]/'
                                                        '../ul/li['+str(i+1)+']/.//input'))
            except Exception as e:
                raise e

    def click_save_set_server(self):
        """确定服务设置"""
        self.click_button(self.confirm_teamwork_btn)

    def click_stop_please_order(self):
        """点击禁止派单"""

        # 初始化操作按钮
        first_branch_info = self.get_first_branch_info()
        if "恢复派单" in first_branch_info:
            # 说明按钮处于恢复派单状态，恢复按钮初始字段，要不然找不到按钮
            self.click_and_roll_right_page()
            self.click_open_please_order()
            self.click_confirm_stop_please()
        self.click_button(self.stop_please_btn)

    def click_open_please_order(self):
        """点击恢复接单"""

        # 初始化操作按钮
        first_branch_info = self.get_first_branch_info()
        if "禁止派单" in first_branch_info:
            # 说明按钮处于禁止派单状态，恢复按钮初始字段，要不然找不到按钮
            self.click_and_roll_right_page()
            self.click_stop_please_order()
            self.click_confirm_stop_please()
        self.click_button(self.open_please_btn)

    def click_confirm_stop_please(self):
        """点击确定禁止/开启派单"""
        self.click_button(self.confirm_please_btn)

