#-*- coding: utf-8 -*-

#@Author  : Mr.Deng
#@Time    : 2019/5/29 17:13

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log = Log()

'''
网点添加订单页面
'''
class AddOrderPage(BasePage):

    '''网点新建订单页面信息'''
    create_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/add'
    textRecognitionBtn = (By.XPATH,'//a[text()="智能文本识别"]')
    inputText = (By.XPATH,'//a[text()="提交识别"]/../textarea')
    submitTextBtn = (By.XPATH,'//a[text()="提交识别"]')
    inputUserName = (By.XPATH,'//input[@placeholder="请输入联系人"]')
    inputPhoneNum = (By.XPATH,'//input[@placeholder="请输入联系方式"]')
    selectProvince = (By.XPATH,'//label[text()="详细地址："]/../select[1]')
    selectCity = (By.XPATH,'//label[text()="详细地址："]/../select[2]')
    selectArea = (By.XPATH,'//label[text()="详细地址："]/../select[3]')
    inputCollage = (By.XPATH,'//input[@placeholder="为了能及时提供服务，请填写详细地址"]')
    selectBranch = (By.XPATH,'//label[text()="工单类型："]/../select')
    serverType = (By.XPATH,'//label[text()="服务类型："]/../select')
    inputOrderTime = (By.XPATH,'//input[@placeholder="预约时间"]')
    selectTime = (By.XPATH,'//label[text()="预约时间："]/../select')
    inputBrands = (By.XPATH,'//input[@placeholder="请选择家电品牌"]')
    inputKinds = (By.XPATH,'//input[@placeholder="请选择家电品类"]')
    inputProductNum = (By.XPATH,'//input[@placeholder="请输入产品型号"]')
    inputInNum = (By.XPATH,'//input[@placeholder="请输入内机编码"]')
    inputOutNum = (By.XPATH,'//input[@placeholder="请输入外机编码"]')
    inputBuyTime = (By.XPATH,'//input[@placeholder="请选择购买时间"]')
    selectBuyPlace = (By.XPATH,'//label[text()="购买渠道："]/../select')
    selectInfoFrom = (By.XPATH,'//label[text()="信息来源："]/../select')
    inputRemark = (By.XPATH,'//label[text()="服务描述："]/../textarea')
    inputPicture = (By.XPATH,'//input[@type="file"]')
    saveBtn = (By.XPATH,'//div[@class="btnMenubox"]/button[1]')
    resetBtn = (By.XPATH,'//div[@class="btnMenubox"]/button[2]')
    pleaseBtn = (By.XPATH,'//div[@class="btnMenubox"]/button[3]')
    saveAndCreateBtn = (By.XPATH,'//div[@class="btnMenubox"]/button[4]')
    addOrderTitle = (By.XPATH,'//span[contains(.,"添加工单")]')
    printOrderInfo = (By.XPATH,'//button[contains(.,"打印工单")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_create_order_url(self):
        '''进入新建订单页面'''
        self.open_url(self.create_order_url)

    def click_recognition_btn(self):
        '''点击智能文本识别按钮'''
        self.click_button(self.textRecognitionBtn)
        #log.info('{0}点击->智能文本识别'.format(self.success))

    def input_text_recognition(self,textRecognition):
        '''输入识别文本'''
        self.input_message(self.inputText,textRecognition)
        #log.info('{0}输入识别文本：{1}'.format(self.success,textRecognition))

    def click_recognition_submit(self):
        '''点击提交识别按钮'''
        self.click_button(self.submitTextBtn)
        #log.info('{0}点击->提交识别'.format(self.success))

    def input_username(self,name):
        '''输入联系人名称'''
        self.input_message(self.inputUserName,name)
        #log.info('{0}输入联系人：{1}'.format(self.success,name))

    def input_phoneNum(self,phoneNum):
        '''输入联系人手机号'''
        self.input_message(self.inputPhoneNum,phoneNum)
        #log.info('{0}输入联系方式：{1}'.format(self.success,phoneNum))

    def select_server_address(self,serverAddress):
        '''选择服务地址'''
        #获取省市区数据
        province,city,area = serverAddress.split('-')
        #选择省份
        self.operate_select(self.selectProvince,province)
        #选择市区
        self.operate_select(self.selectCity,city)
        #选择区县
        self.operate_select(self.selectArea,area)
        #log.info('{0}选择服务区域：{1}'.format(self.success,serverAddress))

    def input_add_collage(self,collage):
        '''输入详细地址信息'''
        self.input_message(self.inputCollage,collage)
        #log.info('{0}输入详细地址：{1}'.format(self.success,collage))

    def select_order_type(self,orderType,branchName=None):
        '''选择工单类型'''
        Path = (By.XPATH,'//input[@name="radio"and@value="'+orderType+'"]/following-sibling::i')
        self.sleep(1)
        self.click_button(Path)
        #log.info('{0}选择工单类型：{1}'.format(self.success,orderType))
        #选择服务商
        if orderType != '无需返单' and branchName != "":
            self.sleep(1)
            self.operate_select(self.selectBranch,branchName)
            #log.info('{0}选择服务商：{1}'.format(self.success,branchName))
        else:
            pass

    def select_server_type(self,serverType):
        '''选择服务类型'''
        if serverType != "":
            self.operate_select(self.serverType,serverType)
            #log.info('{0}选择服务类型：{1}'.format(self.success,serverType))
        else:
            pass

    def input_orderTime(self):
        '''输入预约时间'''
        self.input_message(self.inputOrderTime,self.get_now_time())
        #选择预约时间段
        DayTime = self.operate_select(self.selectTime,is_random=True)
        #log.info('{0}选择预约时间：{1},{2}'.format(self.success,self.get_now_time(),DayTime))

    def input_brands(self,brands):
        '''输入产品品牌'''
        self.input_message(self.inputBrands,brands)
        #log.info('{0}输入产品品牌：{1}'.format(self.success,brands))

    def input_kinds(self,kinds):
        '''输入产品品类'''
        self.input_message(self.inputKinds,kinds)
        #log.info('{0}输入产品品类：{1}'.format(self.success,kinds))

    def input_productNum(self):
        '''输入产品型号'''
        #指定产品型号格式
        self.input_message(self.inputProductNum,'XH0000')
        #log.info('{0}输入产品型号：XH0000'.format(self.success))

    def input_in_phoneNum(self):
        '''输入内机条码'''
        self.input_message(self.inputInNum,'NEIJI'+str(int(self.get_now_timenum())))
        #log.info('{0}输入内机条码：{1}'.format(self.success,'NEIJI'+str(int(self.get_now_timenum()))))

    def input_out_phoneNum(self):
        '''输入外机条码'''
        self.input_message(self.inputOutNum,'WAIJI'+str(int(self.get_now_timenum())))
        #log.info('{0}输入外机条码：{1}'.format(self.success,'WAIJI'+str(int(self.get_now_timenum()))))

    def select_buyTime(self):
        '''选择购买时间'''
        self.input_message(self.inputBuyTime,self.get_now_time())
        #log.info('{0}选择购买时间：{1}'.format(self.success,self.get_now_time()))

    def select_buyPlace(self):
        '''选择购买渠道'''
        BuyPlace = self.operate_select(self.selectBuyPlace,is_random=True)
        #log.info('{0}选择购买渠道：{1}'.format(self.success,BuyPlace))

    def select_info_from(self):
        '''选择信息来源'''
        InfoFrom = self.operate_select(self.selectInfoFrom,is_random=True)
        #log.info('{0}选择信息来源：{1}'.format(self.success,InfoFrom))

    def input_remark(self):
        '''输入下单备注'''
        self.input_message(self.inputRemark,'备注'+self.get_now_time(Time=True))
        #log.info('{0}备注：{1}'.format(self.success,'备注'+self.get_now_time(Time=True)))

    def update_picture(self):
        '''上传图片'''
        self.up_loading_picture(5,self.inputPicture)

    def click_save_btn(self):
        '''点击保存按钮'''
        self.click_button(self.saveBtn)
        #log.info('{0}点击->保存'.format(self.success))

    def click_reset_btn(self):
        '''点击重置按钮'''
        self.click_button(self.resetBtn)
        #log.info('{0}点击->重置'.format(self.success))

    def click_please_btn(self):
        '''点击直接派单按钮'''
        self.click_button(self.pleaseBtn)
        #log.info('{0}点击->直接派单'.format(self.success))

    def click_save_and_add(self):
        '''点击保存并继续添加按钮'''
        self.click_button(self.saveAndCreateBtn)
        #log.info('{0}点击->保存并继续'.format(self.success))

    def create_title_is_displayed(self):
        '''判断 添加工单的table是否关闭'''
        return self.is_display(self.addOrderTitle)

    def print_order_info(self):
        '''打印工单按钮切换窗口'''
        self.click_button(self.printOrderInfo)
        #log.info('{0}点击->打印工单'.format(self.success))

    def create_order_main(self,name,phoneNum,serverAdd,collage,orderType,branchName,serverType,brands,kinds,
                     add_Url='http://www.51shouhou.cn/singleBranch/#/order/add'):
        '''添加订单主程序'''
        #log.info('-=【创建订单】=-')
        #进入添加订单页面
        self.open_url(add_Url)
        #等待页面加载
        self.wait()
        #输入联系人名称
        self.input_username(name)
        #输入联系方式
        self.input_phoneNum(phoneNum)
        #选择服务地址
        self.select_server_address(serverAdd)
        #输入详细地址
        self.input_add_collage(collage)
        #选择工单类型
        self.select_order_type(orderType,branchName)
        #选择服务类型
        self.select_server_type(serverType)
        #选择预约时间和时间段
        self.input_orderTime()
        #选择家电品牌
        self.input_brands(brands)
        #选择家电品类
        self.input_kinds(kinds)
        #输入产品型号
        self.input_productNum()
        #输入内机条码
        self.input_in_phoneNum()
        #输入外机条码
        self.input_out_phoneNum()
        #输入购买时间
        self.select_buyTime()
        #选择购买渠道
        self.select_buyPlace()
        #选择信息来源
        self.select_info_from()
        #输入服务描述信息
        self.input_remark()
        #上传图片
        self.update_picture()
        #点击保存按钮
        self.click_save_btn()
        self.sleep(1)
        #获取系统提示信息
        if self.get_system_msg() == '创建成功':
            log.info('{0} *Create order is success！'.format(self.success))
        else:
            log.error('{0} *Create order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
