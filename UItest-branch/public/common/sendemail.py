#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/2 11:52

import smtplib,os,time
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from config.pathconfig import *


class Send_Email(object):

    def __init__(self):
        # -=获取发送邮件的数据文件=-
        DataPath = emailPath
        cf = ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        self.FromEmailName = cf.get('From_Email','email_name')
        self.FromEmailAddress = cf.get('From_Email','email_address')
        self.FromEmailPassword = cf.get('From_Email','email_password')
        self.ToEmailName = cf.get('To_Email','email_name')
        self.ToEmailAddress = cf.get('To_Email','email_address')

    def EmailTitleMessage(self):
        '''邮件标题信息'''
        # 邮件发送人、收件人、标题、文件标题信息
        # 创建实例
        self.Message = MIMEMultipart()
        # 发送人的名称和邮箱地址
        self.Message['From'] = formataddr([self.FromEmailName,self.FromEmailAddress])
        # 收件人的名称和邮箱地址
        self.Message['To'] = formataddr([self.ToEmailName,self.ToEmailAddress])
        # 邮箱标题信息
        Time = time.strftime('%y-%m-%d',time.localtime(time.time()))
        self.Message['Subject'] = Time + '自动化测试结果'

    def EmailAddTextMessage(self,start_time,run_time):
        '''添加邮件正文文本信息'''
        TextMessage = 'test start time: '+start_time+'\nrunning time: '+run_time+'' \
                      '\n1、注册登录模块：' \
                      '\n2、修改密码模块：' \
                      '\n3、订单管理模块：'
        # plain文本格式
        att = MIMEText(TextMessage,'plain','utf-8')
        self.Message.attach(att)

    def AttNewReport(self):
        '''获取最新的测试报告路径'''
        ReportPath = reportSavePath
        ReportDirs = os.listdir(ReportPath)
        # 循环获取最新的测试报告
        for ReportDir in ReportDirs:
            # 获取每个文件夹下的报告列表
            ReportList = os.listdir(ReportPath + ReportDir)
            # 跳过为空的文件夹
            if len(ReportList) != 0:
                # 把获取的报告文件列表文件按照创建顺序排列
                NewResportList = sorted(ReportList,key=lambda x:os.path.getctime(os.path.join(ReportPath+ReportDir,x)))
                # 获取最后一个报告就是最新的报告
                NewReport = ReportPath + '\\'+ReportDir+'\\' + NewResportList[-1]
                # 上传文件到邮件
                # 长传附件
                att = MIMEText(open(NewReport,'rb').read(),'base64','utf-8')
                att['content-Type'] = 'application/octet-stream'
                # 邮件类型附件，附件名称
                att.add_header('Content-Disposition','attachment',filename=('gbk','',ReportDir+".html"))  # 文件名字有汉字设置编码
                # att['Content-Disposition'] = 'attachment; filename=report.html"')
                self.Message.attach(att)

    def AttNewResult(self):
        '''获取测试结果文件上传'''
        TestResult = testResultPath
        # 获取日志名称
        LogName = TestResult.split("\\")[-1]
        # 上传附件
        att1 = MIMEText(open(TestResult,'rb').read(),'base64','utf-8')
        att1['content-Type'] = 'application/octet-stream'
        # 邮件类型附件，附件名称
        att1['Content-Disposition'] = 'attachment;filename=' + LogName + ''
        self.Message.attach(att1)

    def SendEmailMessage(self):
        '''
        :param FromEmailAddress:    我方邮箱地址
        :param FromEmailPassword:   我方邮箱密码
        :param ToEmailAddress:      他方邮箱
        :param message:             实例函数
        '''
        # ==========【发送邮件的信息】==========
        # 服务器以及端口QQ邮箱端口是465
        server = smtplib.SMTP_SSL('smtp.qq.com',465)
        # 登录邮箱
        server.login(self.FromEmailAddress,self.FromEmailPassword)
        # 发送邮件
        server.sendmail(self.FromEmailAddress,[self.ToEmailAddress],self.Message.as_string())
        # 关闭连接
        server.quit()

    def SendEmailMain(self,start_time,run_time):
        # ==========【主函数发送邮件】==========
        isOk=True
        try:
            # 实例化
            SE = Send_Email()
            # 创建邮件实例
            SE.EmailTitleMessage()
            # 上传文件
            SE.EmailAddTextMessage(start_time,run_time)
            # 上传附件
            SE.AttNewReport()
            SE.AttNewResult()
            # 发送邮件
            SE.SendEmailMessage()
        except Exception as A:
            print(A)
            isOk=False
        # 判断是否发送成功
        if isOk:
            print('邮件发送成功！')
        else:
            print('邮件发送失败！')
# 
# 
#  Send_Email().SendEmailMain()
