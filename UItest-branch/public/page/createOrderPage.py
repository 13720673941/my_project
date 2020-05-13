# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/29 17:13

from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from config.urlConfig import *
from config.pathConfig import *
import datetime

class CreateOrderPage(BasePage):
    """
        【网点创建订单页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.login = LoginPage(driver)

    def get_elements(self,option):
        """获取element_data文件中创建工单页面的元素信息"""
        return read_config_data("create_order_page",option,elementDataPath)

    def enter_create_order_url(self):
        """进入新建订单页面"""
        self.open_url(create_order_url,self.get_elements("username_input"))

    def click_recognition_btn(self):
        """打开智能文本识别按钮"""
        self.click_button(self.get_elements("open_text_recognition_btn"))

    def input_text_recognition(self,textRecognition):
        """输入识别文本"""
        self.input_message(self.get_elements("text_recognition_input"),textRecognition)

    def click_recognition_submit(self):
        """点击提交识别按钮"""
        self.click_button(self.get_elements("text_recognition_submit_btn"))

    def input_username(self,name):
        """输入联系人名称"""
        self.sleep(2)
        self.clear_input(self.get_elements("username_input"))
        self.input_message(self.get_elements("username_input"),name)

    def input_phoneNum(self,phoneNum):
        """输入联系人手机号"""
        self.input_message(self.get_elements("phone_number_input"),phoneNum)

    def select_server_address(self,serverAddress):
        """选择服务地址"""

        # 获取省市区数据,这里测试数据中省市区中间使用 “-” 符号隔开
        province,city,area = serverAddress.split('-')
        # 选择省份
        self.operate_select(self.get_elements("province_select"),province)
        # 选择市区
        self.operate_select(self.get_elements("city_select"),city)
        # 选择区县
        self.operate_select(self.get_elements("area_select"),area)

    def input_add_collage(self,collage):
        """输入详细地址信息"""
        self.input_message(self.get_elements("collage_input"),collage)

    def select_order_type(self,orderType,branchName=None):
        """选择工单类型"""

        # 选择工单类型，无需返单不需要传入服务商，其他的需要传入服务商
        if orderType == "无需返单":
            self.click_button(self.get_elements("i_create_order"))
        elif orderType == "需返单":
            self.click_button(self.get_elements("instead_settle_order"))
        elif orderType == "仅报单":
            self.click_button(self.get_elements("instead_create_order"))
        else:
            raise NameError("Not have this order type: {0} ! ".format(orderType))
        # 选择服务商
        if orderType != '无需返单' and branchName != "" and branchName != None:
            self.sleep(1)
            self.operate_select(self.get_elements("server_branch_select"),branchName)

    def select_server_type(self,serverType):
        """选择服务类型"""
        if serverType != "":
            self.operate_select(self.get_elements("server_type_select"),serverType)

    def input_orderTime(self):
        """输入预约时间"""

        # 获取预约时间当前日期加一天
        date = str(datetime.datetime.now().date() + datetime.timedelta(2))
        # 预约时间段默认固定取值就好了
        time_ = "08:00 - 09:00"
        self.input_message(self.get_elements("appoint_time_input"),date)
        self.sleep(1)
        # 选择预约时间段
        self.input_message(self.get_elements("time_of_day_input"),time_)

    def input_brands(self,brands):
        """输入产品品牌"""
        self.input_message(self.get_elements("brand_input"),brands)

    def select_product_big_kinds(self,big_kinds):
        """选择产品大类"""
        if big_kinds != "":
            self.operate_select(self.get_elements("big_kinds_select"),big_kinds)

    def select_product_kinds(self,kinds):
        """选择产品品类"""
        if kinds != "":
            self.operate_select(self.get_elements("kinds_select"),kinds)

    def select_product_small_kinds(self,small_kinds):
        """选择产品小类"""
        if small_kinds != "":
            self.operate_select(self.get_elements("small_kinds_select"),small_kinds)

    def input_productNum(self):
        """输入产品型号"""
        self.input_message(self.get_elements("product_num_input"),'XH0000')

    def input_in_phoneNum(self):
        """输入内机条码"""
        self.input_message(self.get_elements("product_in_num_input"),'NEIJI'+str(int(self.get_now_timenum())))

    def input_out_phoneNum(self):
        """输入外机条码"""
        self.input_message(self.get_elements("product_out_num_input"),'WAIJI'+str(int(self.get_now_timenum())))

    def select_buyTime(self):
        """选择购买时间"""
        self.input_message(self.get_elements("buy_time_input"),self.get_now_time())

    def select_buyPlace(self):
        """选择购买渠道"""
        self.operate_select(self.get_elements("buy_place_select"),is_random=True)

    def select_info_from(self):
        """选择信息来源"""
        self.operate_select(self.get_elements("info_from_select"),is_random=True)

    def input_remark(self):
        """输入下单备注"""
        self.input_message(self.get_elements("remark_input"),'备注'+self.get_now_time(Time=True))

    def update_picture(self,num=5):
        """
        上传图片
        :param num      上传图片的个数
        :param element  上传图片元素位置
        Usage:
        driver.up_loading_picture()
        """
        # 加载图片列表
        Plist = os.listdir(picturePath)
        # 循环上传
        for i in range(num):
            try:
                Picture = picturePath + Plist[i]
                self.sleep(2)
                self.input_message(self.get_elements("update_picture_input"),message=Picture)
                self.log.info(' * Uploading picture: {0} . '.format(Picture))
            except:
                raise Exception(' * Uploading is anomaly ! ')

    def click_save_btn(self):
        """点击保存按钮"""
        self.sleep(2)
        self.click_button(self.get_elements("save_order_btn"))

    def click_reset_btn(self):
        """点击重置按钮"""
        self.click_button(self.get_elements("reset_order_btn"))

    def click_please_btn(self):
        """点击直接派单按钮"""
        self.click_button(self.get_elements("please_order_btn"))

    def click_save_and_add(self):
        """点击保存并继续添加按钮"""
        self.click_button(self.get_elements("save_and_continue_btn"))

    def create_title_is_displayed(self):
        """判断 添加工单的table是否关闭"""
        return self.is_display(self.get_elements("add_order_page_title"))

    def get_branch_name_list_for_set(self):
        """获取返单、报单服务商的全部名称列表"""

        # 获取下拉网点元素列表
        branch_list = self.get_element_count(self.get_elements("server_branch_select"),"option")[1]
        # 保存元素文本列表中去
        branch_name_list = []
        # 循环元素列表报存到文本列表中
        for name in branch_list:
            branch_name_list.append(name.text)
        return branch_name_list

    def get_order_number(self,insteadOrder=False):
        """
            获取最新工单单号
        """

        # 判断需要打开的订单列表页面，仅报单到待报单页面获取
        if insteadOrder:
            self.open_url(instead_order_list_url)
        else:
            self.open_url(all_order_list_url)
        self.sleep(1)
        newOrderNum = None
        # 获取工单单号
        for i in range(10):
            try:
                self.refresh_page()
                # 获取第一个订单的创建时间
                if insteadOrder: # 代报单获取创建时间不一样
                    addOrderTime = self.get_text(self.get_elements("instead_order_create_time"))
                else:
                    addOrderTime = self.get_text(self.get_elements("my_order_create_time"))
                # 把时间转化为时间戳小于30秒就是新订单
                oldTimeNumber = self.get_one_timenum(DataTime=addOrderTime,Time=True)
                newTime = self.get_now_timenum()
                if newTime - oldTimeNumber < 60:
                    newOrderNum = self.get_text(self.get_elements("get_order_number_path"))
                    self.log.info(' * Get order number: {0}.'.format(newOrderNum))
                    # 有时候获取不到订单单号，判断单号的长度，否则刷新页面
                    if len(newOrderNum) == 18:
                        break
                    else:
                        self.refresh_page()
            except:
                if i == 9:
                    raise Exception(' * Unable get order number.')
        return newOrderNum

    def select_operate_order(self,order_number):
        """
            勾选需要操作的订单,一般新建订单都在前面所以只查找前是个没有找到就是没有前面操作失败
        """

        self.sleep(2)
        for i in range(1,10):
            try:
                OrderNum = self.get_text(self.get_elements("order_list_of_number").replace("+order_row+",str(i)))
                if OrderNum == order_number:
                    self.click_button(self.get_elements("select_order_input").replace("+order_row+",str(i)))
                    self.log.info(' * Select order: {0}.'.format(order_number))
                    break
            except Exception:
                if i == 9:
                    raise Exception(" * Not found order number: {0} in order list.".format(order_number))
                else:
                    self.refresh_page()

    def assert_order_in_list(self,order_number):
        """
            判断订单是否存在订单列表中
        """
        # 建立一个flag默认False
        flag = False
        for i in range(1,10):
            try:
                self.sleep(2)
                OrderNum = self.get_text(self.get_elements("order_list_of_number").replace("+order_row+",str(i)))
                if OrderNum == order_number:
                    flag = True
            except:
                if i == 9:
                    raise Exception(" * Not found order number: {0} in order list.".format(order_number))
                else:
                    self.refresh_page()
            finally:
                return flag

    def open_order_details(self,OrderNumber):
        """
        点击订单号进入详情页
        """
        self.sleep(2)
        for i in range(1,10):
            try:
                OrderNum = self.get_text(self.get_elements("order_list_of_number").replace("+order_row+",str(i)))
                if OrderNum == OrderNumber:
                    self.click_button(self.get_elements("order_list_of_number").replace("+order_row+",str(i)))
                    self.log.info(' * Into order: {0} details page.'.format(OrderNumber))
                    break
            except:
                if i == 2:
                    self.refresh_page()
                elif i == 9:
                    raise Exception(' * Unable into order: {0} details page.'.format(OrderNumber))

    def create_order_main(self,name,phoneNum,serverAdd,orderType,collage,server_type,
                          brands,big_kinds,kinds,small_kinds,branchName=None):
        """
            添加订单主程序
        """
        self.log.info('-=【创建订单】=-')
        # 进入添加订单页面
        self.enter_create_order_url()
        # 输入联系人名称
        self.input_username(name)
        # 输入联系方式
        self.input_phoneNum(phoneNum)
        # 选择服务地址
        self.select_server_address(serverAdd)
        # 选择工单类型
        self.select_order_type(orderType,branchName)
        # 输入详细地址
        self.input_add_collage(collage)
        self.sleep(2)
        # 选择服务类型
        self.select_server_type(server_type)
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
        # 点击保存按钮
        self.click_save_btn()
        self.sleep(2)
        # 获取当前跳转地址判断是否创建成功
        if self.login.get_system_msg() == "创建成功":
            self.log.info(' ** Create order is success！')
        else:
            raise TimeoutError(' ** Create order is fail ！')

    def create_not_return_order(self):
        """默认创建无需返单订单"""

        user = read_config_data("NotReturnOrder", "用户姓名", createMessage)
        phe = read_config_data("NotReturnOrder", "联系方式", createMessage)
        address = read_config_data("NotReturnOrder", "服务地址", createMessage)
        collage = read_config_data("NotReturnOrder", "详细地址", createMessage)
        order_type = read_config_data("NotReturnOrder", "工单类型", createMessage)
        server = read_config_data("NotReturnOrder", "服务类型", createMessage)
        brands = read_config_data("NotReturnOrder", "品牌", createMessage)
        big_kinds = read_config_data("NotReturnOrder", "大类", createMessage)
        kinds = read_config_data("NotReturnOrder", "品类", createMessage)
        small_kinds = read_config_data("NotReturnOrder", "小类", createMessage)

        self.create_order_main(user,phe,address,order_type,collage,server,brands,big_kinds,kinds,small_kinds)

    def create_return_order(self):
        """默认创建需返单订单"""

        user = read_config_data("ReturnOrder", "用户姓名", createMessage)
        phe = read_config_data("ReturnOrder", "联系方式", createMessage)
        address = read_config_data("ReturnOrder", "服务地址", createMessage)
        collage = read_config_data("ReturnOrder", "详细地址", createMessage)
        order_type = read_config_data("ReturnOrder", "工单类型", createMessage)
        branch_name = read_config_data("ReturnOrder", "服务商", createMessage)
        server = read_config_data("ReturnOrder", "服务类型", createMessage)
        brands = read_config_data("ReturnOrder", "品牌", createMessage)
        big_kinds = read_config_data("ReturnOrder", "大类", createMessage)
        kinds = read_config_data("ReturnOrder", "品类", createMessage)
        small_kinds = read_config_data("ReturnOrder", "小类", createMessage)

        self.create_order_main(user,phe,address,order_type,collage,server,brands,big_kinds,kinds,small_kinds,branch_name)