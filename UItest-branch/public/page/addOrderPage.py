# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/29 17:13

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from public.common.rwconfig import read_config_data
from config.urlconfig import *
from config.pathconfig import *
log = Log()

class AddOrderPage(BasePage):

    """网点添加订单页面"""
    
    # 打开只能识别按钮
    open_text_recognition_btn = (By.XPATH,'//a[text()="智能文本识别"]')
    # 识别文本输入框
    text_recognition_input = (By.XPATH,'//a[text()="提交识别"]/../textarea')
    # 识别文本确定按钮
    text_recognition_confirm = (By.XPATH,'//a[text()="提交识别"]')
    # 联系人输入框
    username_input = (By.XPATH,'//input[@placeholder="请输入联系人"]')
    # 联系人电话输入框
    phone_num_input = (By.XPATH,'//input[@placeholder="请输入联系方式"]')
    # 选择省份select框
    province_select = (By.XPATH,'//label[text()="详细地址："]/../select[1]')
    # 选择城市select框
    city_select = (By.XPATH,'//label[text()="详细地址："]/../select[2]')
    # 选择区县select框
    area_select = (By.XPATH,'//label[text()="详细地址："]/../select[3]')
    # 详细地址输入框
    collage_input = (By.XPATH,'//input[@placeholder="为了能及时提供服务，请填写详细地址"]')
    # 选择服务商select框
    branch_select = (By.XPATH,'//label[text()="工单类型："]/../select')
    # 选择服务类型框
    server_type_select = (By.XPATH,'//label[text()="服务类型："]/../select')
    # 预约时间输入框
    order_time_input = (By.XPATH,'//input[@placeholder="预约时间"]')
    # 预约时间端select框
    time_of_day_select = (By.XPATH,'//label[text()="预约时间："]/../select')
    # 品牌输入框
    brands_input = (By.XPATH,'//input[@placeholder="请选择家电品牌"]')
    # 产品大类选择框
    big_kinds_select = (By.XPATH,'//label[text()="产品大类："]/../select')
    # 产品品类选择框
    kinds_select = (By.XPATH,'//label[text()="产品品类："]/../select')
    # 产品小类选择框
    small_kinds_select = (By.XPATH,'//label[text()="产品小类："]/../select')
    # 产品编码输入框
    product_num_input = (By.XPATH,'//input[@placeholder="请输入产品型号"]')
    # 内机编码输入框
    product_in_num_input = (By.XPATH,'//input[@placeholder="请输入内机编码"]')
    # 外机条码输入框
    product_out_num_input = (By.XPATH,'//input[@placeholder="请输入外机编码"]')
    # 购买时间输入框
    buy_time_input = (By.XPATH,'//input[@placeholder="请选择购买时间"]')
    # 购买渠道选择框
    buy_place_select = (By.XPATH,'//label[text()="购买渠道："]/../select')
    # 订单来源选择框
    info_from_select = (By.XPATH,'//label[text()="信息来源："]/../select')
    # 备注输入框
    remark_input = (By.XPATH,'//label[text()="服务描述："]/../textarea')
    # 图片上传元素路径
    update_picture_input = (By.XPATH,'//input[@type="file"]')
    # 保存工单按钮
    save_order_btn = (By.XPATH,'//div[@class="btnMenubox"]/button[1]')
    # 重置工单按钮
    reset_order_btn = (By.XPATH,'//div[@class="btnMenubox"]/button[2]')
    # 直接派单按钮
    please_order_btn = (By.XPATH,'//div[@class="btnMenubox"]/button[3]')
    # 保存并继续按钮
    save_create_btn = (By.XPATH,'//div[@class="btnMenubox"]/button[4]')
    # 添加工单页面的小title(判断页面是否关闭)
    add_order_page_title = (By.XPATH,'//span[contains(.,"添加工单")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_create_order_url(self):
        """进入新建订单页面"""
        self.open_url(create_order_url)

    def click_recognition_btn(self):
        """点击智能文本识别按钮"""
        self.click_button(self.open_text_recognition_btn)

    def input_text_recognition(self,textRecognition):
        """输入识别文本"""
        self.input_message(self.text_recognition_input,textRecognition)

    def click_recognition_submit(self):
        """点击提交识别按钮"""
        self.click_button(self.text_recognition_confirm)

    def input_username(self,name):
        """输入联系人名称"""
        self.input_message(self.username_input,name)

    def input_phoneNum(self,phoneNum):
        """输入联系人手机号"""
        self.clear_input(self.phone_num_input)
        self.input_message(self.phone_num_input,phoneNum)

    def select_server_address(self,serverAddress):
        """选择服务地址"""
        # 获取省市区数据
        province,city,area = serverAddress.split('-')
        # 选择省份
        self.operate_select(self.province_select,province)
        # 选择市区
        self.operate_select(self.city_select,city)
        # 选择区县
        self.operate_select(self.area_select,area)

    def input_add_collage(self,collage):
        """输入详细地址信息"""
        self.input_message(self.collage_input,collage)

    def select_order_type(self,orderType,branchName=None):
        """选择工单类型"""

        self.path = (By.XPATH,'//input[@name="radio"and@value="'+orderType+'"]/following-sibling::i')
        self.sleep(1)
        self.click_button(self.path)
        # 选择服务商
        if orderType != '无需返单' and branchName != '':
            self.sleep(1)
            self.operate_select(self.branch_select,branchName)
        else:
            pass

    def select_server_type(self,serverType):
        """选择服务类型"""
        if serverType != "":
            self.operate_select(self.server_type_select,serverType)
        else:
            pass

    def input_orderTime(self):
        """输入预约时间"""
        self.input_message(self.order_time_input,self.get_now_time())
        # 选择预约时间段
        self.operate_select(self.time_of_day_select,is_random=True)

    def input_brands(self,brands):
        """输入产品品牌"""
        self.input_message(self.brands_input,brands)

    def select_product_big_kinds(self,big_kinds):
        """选择产品大类"""
        if big_kinds != "":
            self.operate_select(self.big_kinds_select,big_kinds)

    def select_product_kinds(self,kinds):
        """选择产品品类"""
        if kinds != "":
            self.operate_select(self.kinds_select,kinds)

    def select_product_small_kinds(self,small_kinds):
        """选择产品小类"""
        if small_kinds != "":
            self.operate_select(self.small_kinds_select,small_kinds)

    def input_productNum(self):
        """输入产品型号"""
        # 指定产品型号格式
        self.input_message(self.product_num_input,'XH0000')

    def input_in_phoneNum(self):
        """输入内机条码"""
        self.input_message(self.product_in_num_input,'NEIJI'+str(int(self.get_now_timenum())))

    def input_out_phoneNum(self):
        """输入外机条码"""
        self.input_message(self.product_out_num_input,'WAIJI'+str(int(self.get_now_timenum())))

    def select_buyTime(self):
        """选择购买时间"""
        self.input_message(self.buy_time_input,self.get_now_time())

    def select_buyPlace(self):
        """选择购买渠道"""
        self.operate_select(self.buy_place_select,is_random=True)

    def select_info_from(self):
        """选择信息来源"""
        self.operate_select(self.info_from_select,is_random=True)

    def input_remark(self):
        """输入下单备注"""
        self.input_message(self.remark_input,'备注'+self.get_now_time(Time=True))

    def update_picture(self):
        """上传图片"""
        self.up_loading_picture(5,self.update_picture_input)

    def click_save_btn(self):
        """点击保存按钮"""
        self.click_button(self.save_order_btn)

    def click_reset_btn(self):
        """点击重置按钮"""
        self.click_button(self.reset_order_btn)

    def click_please_btn(self):
        """点击直接派单按钮"""
        self.click_button(self.please_order_btn)

    def click_save_and_add(self):
        """点击保存并继续添加按钮"""
        self.click_button(self.save_create_btn)

    def create_title_is_displayed(self):
        """判断 添加工单的table是否关闭"""
        return self.is_display(self.add_order_page_title)

    # 授权页面的服务配置操作方法
    def select_order_type_for_set(self,orderType):
        """选择工单类型-服务设置判断操作"""
        self.click_button((By.XPATH,'//input[@name="radio"and@value="'+orderType+'"]/following-sibling::i'))

    def get_branch_name_list_for_set(self):
        """获取返单、报单服务商的全部名称列表"""

        # 获取下拉网点元素列表
        branch_element_list = self.get_element_count(self.branch_select,"option")[1]
        # 保存元素文本列表中去
        branch_name_list = []
        # 循环元素列表报存到文本列表中
        for name in branch_element_list:
            branch_name_list.append(name.text)
        return branch_name_list

    def create_order_main(self,name,phoneNum,serverAdd,collage,orderType,server_type_select,
                          brands,big_kinds,kinds,small_kinds,branchName=None):
        """
        添加订单主程序
        """
        log.info('-=【创建订单】=-')
        # 进入添加订单页面
        self.enter_create_order_url()
        # 等待页面加载
        self.wait()
        # 输入联系人名称
        self.input_username(name)
        # 输入联系方式
        self.input_phoneNum(phoneNum)
        # 选择服务地址
        self.select_server_address(serverAdd)
        # 输入详细地址
        self.input_add_collage(collage)
        # 选择工单类型
        self.select_order_type(orderType,branchName)
        # 选择服务类型
        self.select_server_type(server_type_select)
        # 选择预约时间和时间段
        self.input_orderTime()
        # 选择家电品牌
        self.input_brands(brands)
        # 选择产品大类
        self.select_product_big_kinds(big_kinds)
        # 选择家电品类
        self.select_product_kinds(kinds)
        # 选择产品小类
        self.select_product_small_kinds(small_kinds)
        # 输入产品型号
        self.input_productNum()
        # 输入内机条码
        self.input_in_phoneNum()
        # 输入外机条码
        self.input_out_phoneNum()
        # 输入购买时间
        self.select_buyTime()
        # 选择购买渠道
        self.select_buyPlace()
        # 选择信息来源
        self.select_info_from()
        # 输入服务描述信息
        self.input_remark()
        # 上传图片
        self.update_picture()
        # 点击保存按钮
        self.click_save_btn()
        self.sleep(1)
        # 获取系统提示信息
        if self.get_system_msg() == '创建成功':
            log.info('{0} ** Create order is success！'.format(self.success))
        else:
            log.error('{0} ** Create order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))

    def create_not_return_order(self):
        """默认创建无需返单订单"""

        user = read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = read_config_data("NotReturnOrder", "品牌", orderInfo)
        big_kinds = read_config_data("NotReturnOrder", "大类", orderInfo)
        kinds = read_config_data("NotReturnOrder", "品类", orderInfo)
        small_kinds = read_config_data("NotReturnOrder", "小类", orderInfo)

        self.create_order_main(user,phe,address,collage,order_type,server,brands,big_kinds,kinds,small_kinds)

    def create_return_order(self):
        """默认创建需返单订单"""

        user = read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = read_config_data("NotReturnOrder", "品牌", orderInfo)
        big_kinds = read_config_data("NotReturnOrder", "大类", orderInfo)
        kinds = read_config_data("NotReturnOrder", "品类", orderInfo)
        small_kinds = read_config_data("NotReturnOrder", "小类", orderInfo)
        branch_name = read_config_data("NotReturnOrder", "服务商", orderInfo)

        self.create_order_main(user,phe,address,collage,order_type,server,brands,big_kinds,kinds,small_kinds,branch_name)