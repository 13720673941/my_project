#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/21 18:25

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
"""
网点登录后修改密码页面
"""
class AlterPwdPage(BasePage):

    """
    页面元素路径信息
    """
    # 修改密码页面的url地址
    alter_pwd_url = 'http://www.51shouhou.cn/singleBranch/#/changePassword'
    # 手机号->修改按钮
    phe_alter_btn = (By.XPATH,'//label[text()="手机号："]/../div/p/a')
    # 登录密码输入框
    login_pwd_input = (By.XPATH,'//input[@placeholder="输入登录密码"]')
    # 登录密码红字提示信息
    login_none_msg = (By.XPATH,'//label[text()="登录密码:"]/../div/div[2]')
    # 手机号输入框
    phe_num_input = (By.XPATH,'//input[@placeholder="输入手机号码"]')
    # 手机号码红字提示信息
    phe_none_msg = (By.XPATH, '//label[text()="手机号码:"]/../div/div[2]')
    # 获取验证码按钮
    get_code_btn = (By.XPATH,'//span[text()="获取验证码"]')
    # 获取验证码按钮发送后的disabled属性
    get_code_btn_att = (By.XPATH,'//label[text()="验证码"]/../div/div[1]/div[2]/button')
    # 验证码输入框
    code_num_input = (By.XPATH,'//input[@placeholder="输入验证码"]')
    # 验证码红字提示信息
    code_none_msg = (By.XPATH,'//label[text()="验证码"]/../div/div[2]')
    # 确定修改按钮
    confirm_alter = (By.XPATH,'//span[contains(.,"确定修改")]')
    # 密码->修改按钮>>>>>>
    pwd_alter_btn = (By.XPATH,'//label[text()="登陆密码："]/../div/p/a')
    # 原登录密码输入框
    old_pwd_input = (By.XPATH,'//input[@placeholder="输入原登录密码"]')
    # 原来登录密码系统提示
    old_pwd_none_msg = (By.XPATH,'//label[text()="原登录密码:"]/../div/div[2]')
    # 新密码输入框
    new_pwd_input = (By.XPATH,'//input[@placeholder="6-18位数字、字母的组合"]')
    # 新密码输入框为空提示
    new_pwd_none_msg = (By.XPATH,'//label[text()="新登录密码:"]/../div/div[2]')
    # 确认密码
    confirm_pwd_input = (By.XPATH,'//input[@placeholder="请重复输入新登录密码"]')
    # 确认密码为空系统提示
    confirm_pwd_none_msg = (By.XPATH,'//label[text()="重复密码:"]/../div/div[2]')
    # 修改密码确认修改
    confirm_pwd_btn = (By.XPATH,'//div[text()="修改登录密码"]/../../div[3]/div/button')


    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_alterPwd_page(self):
        '''进入修改密码页面'''
        self.open_url(self.alter_pwd_url)

    # 修改手机号
    def click_alter_pheNum(self):
        '''点击修改手机号->修改'''
        self.click_button(self.phe_alter_btn)
        # log.info('{0}点击->修改手机号'.format(self.success))

    def input_login_pwd(self,login_pwd):
        '''输入登录密码'''
        self.input_message(self.login_pwd_input,login_pwd)
        # log.info('{0}输入登录密码: {1}'.format(self.success,login_pwd))

    def get_login_pwd_msg(self):
        '''获取登录密码提示信息'''
        return self.get_text(self.login_none_msg)

    def input_phe_num(self,phone_num):
        '''输入手机号'''
        self.input_message(self.phe_num_input,phone_num)
        # log.info('{0}输入手机号: {1}'.format(self.success,phone_num))

    def get_phone_num_msg(self):
        '''获取输入手机号提示'''
        return self.get_text(self.phe_none_msg)

    def click_code_button(self):
        '''点击获取验证码'''
        self.click_button(self.get_code_btn)
        # log.info('{0}点击->获取验证码'.format(self.success))

    def get_code_button_att(self):
        '''获取发送验证码后: 获取验证码按钮-disabled属性'''
        return self.get_att(self.get_code_btn_att,'disabled')

    def input_code_number(self,code_num):
        '''输入验证码'''
        self.input_message(self.code_num_input,code_num)
        # log.info('{0}输入验证码: {1}'.format(self.success,code_num))

    def get_code_input_msg(self):
        '''获取验证码输入框系统提示'''
        return self.get_text(self.code_none_msg)

    def click_confirm_alter(self):
        '''点击确定修改'''
        self.click_button(self.confirm_alter)
        # log.info('{0}点击->确定修改'.format(self.success))

    # 修改密码
    def click_alter_pwd(self):
        '''点击修改密码->修改'''
        self.click_button(self.pwd_alter_btn)

    def input_old_pwd(self,old_pwd):
        '''输入旧密码'''
        self.input_message(self.old_pwd_input,old_pwd)

    def get_old_pwd_msg(self):
        '''获取旧密码为空的系统提示'''
        return self.get_text(self.old_pwd_none_msg)

    def input_new_pwd(self,new_pwd):
        '''输入新密码'''
        self.input_message(self.new_pwd_input,new_pwd)

    def get_new_pwd_msg(self):
        '''获取新密码为空提示'''
        return self.get_text(self.new_pwd_none_msg)
    
    def input_confirm_pwd(self,confirm_pwd):
        '''输入确认密码'''
        self.input_message(self.confirm_pwd_input,confirm_pwd)
    
    def get_confirm_pwd_msg(self):
        '''获取确认密码为空提示'''
        return self.get_text(self.confirm_pwd_none_msg)

    def click_confirm_alterPwd(self):
        '''修改密码下面的确定修改'''
        self.click_button(self.confirm_pwd_btn)

