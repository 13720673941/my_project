# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/20 18:47

import smtplib,os,time
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from Common import Pubilc

class Send_Email(object):

    def __init__(self):
        #==========【获取邮件账号密码配置文件】==========
        #获取邮箱信息
        DataPath = Pubilc.data_dir(filename='EmailMessage.ini')
        cf = ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        self.FromEmailName = cf.get('From_Email','email_name')
        self.FromEmailAddress = cf.get('From_Email','email_address')
        self.FromEmailPassword = cf.get('From_Email','email_password')
        self.ToEmailName = cf.get('To_Email','email_name')
        self.ToEmailAddress = cf.get('To_Email','email_address')

    def EmailTitleMessage(self):
        '''
        :param FromName:    我方用户名
        :param FromEmail:   我方邮箱地址
        :param ToName:      他方用户名
        :param ToEmail:     他方邮箱地址
        '''
        #==========【创建邮件实例】==========
        #邮件发送人、收件人、标题、文件标题信息
        #创建实例
        self.message = MIMEMultipart()
        #发送方的邮箱名称和邮箱地址
        self.message['From'] = formataddr([self.FromEmailName,self.FromEmailAddress])
        #收件人的邮箱名称和地址
        self.message['To'] = formataddr([self.ToEmailName,self.ToEmailAddress])
        #邮件标题信息
        Time = time.strftime('%y-%m-%d',time.localtime(time.time()))
        self.message['Subject'] = Time + '自动化测试结果'

    def GetReportDirName(self):
        #==========【获取Report文件夹下子文件夹的名字】==========
        #获取报告文件夹下面的所有文件夹的名字
        DataPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ReportData = DataPath + '\\Report\\'
        ReportDirList = os.listdir(ReportData)
        #删除第一个初始化的py文件
        ReportDirList.pop(0)
        return ReportDirList

    def GetNewReport(self,ReportDir):
        '''
        :param ReportDir: Report文件夹中子文件夹名字
        '''
        #==========【获取报告文件下所有文件夹的最新文件】==========
        #获取最新的测试报告
        DataPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ReportData = DataPath+'\\Report\\'+ReportDir+'\\'
        ReportList = os.listdir(ReportData)
        #对报告文件加的报告按照创建时间getctime进行重新排序
        NewReportList = sorted(ReportList,key=lambda x:os.path.getctime(os.path.join(ReportData,x)))
        #获取列表最后一个
        NewReport = ReportData + NewReportList[-1]
        return NewReport

    def GetNewRunResultLog(self):
        #==========【获取最新结果日志】==========
        DataPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ReportData = DataPath + '\\Log\\RunResult\\'
        ReportList = os.listdir(ReportData)
        #对日志文件加的报告按照创建时间getctime进行重新排序
        NewReportList = sorted(ReportList,key=lambda x: os.path.getctime(os.path.join(ReportData,x)))
        #获取列表最后一个
        NewRunResult = ReportData + NewReportList[-1]
        return NewRunResult

    def EmailAddTextMessage(self,StartTime,RunTime):
        #==========【上传邮件文本信息】==========
        #三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        TextMessage='脚本开始时间：'+StartTime+'\n脚本运行时间：'+RunTime+'分钟' \
                    '\n1、【品牌商订单流程】：a、品牌商订单流程 b、品牌商订单改派流程 c、WAP门户订单流程 d、WAP用户订单流程 e、品牌商自动派单流程 f、网点添加品牌商订单流程 g、WAP网点完成订单流程 ' \
                    '\n2、【网点订单流程】：a、网点自营订单流程 b、网点改派订单流程 c、WAP门户添加网点订单流程'
        att = MIMEText(TextMessage,'plain','utf-8')
        self.message.attach(att)

    def EmailAddAttachment(self):
        '''
        :param message:         创建的实例
        :param ReportDirName:   文件夹名字也就是报告正文上面的标题信息
        :param NewReport:       附带报告的文件名字
        '''
        #==========【上传附件信息】==========
        #实例化类
        SE = Send_Email()
        #获取报告文件夹下面的所有文件名字
        ReportDirNameList = SE.GetReportDirName()
        #循环上传附件
        for DirName in ReportDirNameList:
            #获取最新文件夹里面的报告
            NewReport = SE.GetNewReport(ReportDir=DirName)
            #长传附件
            att = MIMEText(open(NewReport,'rb').read(),'base64','utf-8')
            att['content-Type'] = 'application/octet-stream'
            #邮件类型附件，附件名称
            att.add_header('Content-Disposition','attachment',filename=('gbk','',DirName+".html"))#文件名字有汉字设置编码
            #att['Content-Disposition'] = 'attachment; filename=report.html"')
            self.message.attach(att)
        #==========【上传日志】==========
        NewRunResult = SE.GetNewRunResultLog()
        #获取日志名称
        LogName = NewRunResult.split("\\")[-1]
        #上传附件
        att1 = MIMEText(open(NewRunResult,'rb').read(),'base64','utf-8')
        att1['content-Type'] = 'application/octet-stream'
        # 邮件类型附件，附件名称
        att1['Content-Disposition'] = 'attachment;filename='+LogName+''
        self.message.attach(att1)

    def SendEmailMessage(self):
        '''
        :param FromEmailAddress:    我方邮箱地址
        :param FromEmailPassword:   我方邮箱密码
        :param ToEmailAddress:      他方邮箱
        :param message:             实例函数
        '''
        #==========【发送邮件的信息】==========
        #服务器以及端口QQ邮箱端口是465
        server = smtplib.SMTP_SSL('smtp.qq.com',465)
        #登录邮箱
        server.login(self.FromEmailAddress,self.FromEmailPassword)
        #发送邮件
        server.sendmail(self.FromEmailAddress,[self.ToEmailAddress],self.message.as_string())
        #关闭连接
        server.quit()

    def SendEmailMain(self,StartTime,RunTime):
        #==========【主函数发送邮件】==========
        isOk=True
        try:
            #实例化
            SE = Send_Email()
            #创建邮件实例
            SE.EmailTitleMessage()
            #上传文件
            SE.EmailAddTextMessage(StartTime,RunTime)
            #上传附件
            SE.EmailAddAttachment()
            #发送邮件
            SE.SendEmailMessage()
        except Exception as A:
            print(A)
            isOk=False
        #判断是否发送成功
        if isOk:
            print('邮件发送成功！')
        else:
            print('邮件发送失败！')


# Send_Email().SendEmailMain(StartTime='12:22',RunTime='102S')
# SendResult=True
# try:
#     #创建实例
#     SendEmail = Send_Email()
#     #上传文本
#     SendEmail.EmailTitleMessage()
#     SendEmail.EmailAddTextMessage()
#     SendEmail.EmailAddAttachment()
#     SendEmail.send_email()
#
# except Exception:
#     #执行失败返回False
#     SendResult=False
# #判断发送邮件是否成功
# if SendResult:
#     print('\n邮件发送成功！')
# else:
#     print('\n邮件发送失败！')
