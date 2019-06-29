# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/12 16:07

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
返单页面操作
'''
class ReturnOrderPage(BasePage):

    '''
    返单页面元素操作
    '''
    #待返单url
    return_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'
    #已返单url
    finish_return_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=已返单&page=1'
    #返单按钮
    return_order_btn = (By.XPATH,'//a[text()="返单"]')
    #修改返单服务商按钮
    alter_return_branch_btn = (By.XPATH,'//a[text()="修改返单服务商"]')
    #确定修改按钮
    confirm_alter_btn = (By.XPATH,'//div[text()="服务商列表"]/../following-sibling::div[2]/button[2]')
    #添加服务商按钮
    add_branch_btn = (By.XPATH,'//a[text()="添加代结单服务商"]')
    #撤销返单按钮
    del_return_btn = (By.XPATH,'//a[text()="撤销返单"]')
    #添加服务商页面title(验证跳转按钮)
    turn_add_branch_title = (By.XPATH,'//a[text()="添加经销商"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_return_order_page(self):
        self.open_url(self.return_order_url)

    def enter_finish_return_page(self):
        self.open_url(self.finish_return_url)

    def click_return_btn(self):
        '''点击返单按钮'''
        self.click_button(self.return_order_btn)

    def click_alter_return_branch(self):
        '''点击修改返单服务商'''
        self.click_button(self.alter_return_branch_btn)

    def select_branch_name(self,branchName):
        '''选择返单服务商名称'''
        if branchName != '':
            self.click_button(element=(By.XPATH,'//label[text()=" '+branchName+'"]'))

    def click_confirm_btn(self):
        '''点击确定'''
        self.click_button(self.confirm_alter_btn)
        #log.info('{0}点击->确定'.format(self.success))

    def click_add_branch(self):
        '''点击添加待接单服务商'''
        self.click_button(self.add_branch_btn)

    def click_del_return(self):
        '''点击撤销返单'''
        self.click_button(self.del_return_btn)

    def turn_title_isDisplayed(self):
        '''判断页面是否跳转添加服务商页面'''
        return self.is_display(self.turn_add_branch_title)

    def return_order_main(self,orderNumber,alter_return_branch_btn=False,branchName=None):
        '''返单主程序'''
        log.info('-=【返单】=-')
        #进入返单页面
        self.enter_return_order_page()
        self.wait()
        #选择订单
        self.select_new_order(orderNumber)
        #返单是否修改返单服务商
        if alter_return_branch_btn:
            #点击修改返单服务商
            self.click_alter_return_branch()
            #选择服务商名称
            self.select_branch_name(branchName)
        #点击返单按钮
        self.click_return_btn()
        self.sleep(1)
        #断言
        if '操作成功' in self.get_system_msg():
            log.info('{0} *Return order: {1} success！'.format(self.success,orderNumber))
        else:
            log.error('{0} *Return order: {1} fail, system msg: {2}.'.format(self.fail,orderNumber,self.get_system_msg()))