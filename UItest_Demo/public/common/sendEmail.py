# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/14 20:42

from public.common.rwFile import RWFile
from config.pathConfig import *
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import smtplib,os
rw = RWFile()
"""
    发送邮件方法
"""
class SendEmail:

    def send_email(self):
        # 邮箱服务器地址/服务器端口号
        SMTP_SERVER = 'smtp.qq.com' #"smtp.163.com"
        PORT = 465  # 163端口是 25
        # 发件人名称/邮箱/密码
        SENDER_NAME = rw.read_config_file(CONFIG_DATA_PATH,"FROM_EMAIL","EMAIL_NAME")
        SENDER_EMAIL = rw.read_config_file(CONFIG_DATA_PATH,"FROM_EMAIL","EMAIL_ADDRESS")
        SENDER_PASSWORD = rw.read_config_file(CONFIG_DATA_PATH,"FROM_EMAIL","EMAIL_PASSWORD")
        # 收件人邮箱地址
        RECEIVER_NAME = rw.read_config_file(CONFIG_DATA_PATH,"TO_EMAIL","EMAIL_NAME")
        RECEIVER_EAML = rw.read_config_file(CONFIG_DATA_PATH,"TO_EMAIL","EMAIL_ADDRESS")

        # -------------------------------------
        # 创建邮箱对象
        message = MIMEMultipart()
        # 添加发件人和收件人
        message['From'] = formataddr((SENDER_NAME,SENDER_EMAIL))
        message['To'] = formataddr((RECEIVER_NAME,RECEIVER_EAML))
        # 添加邮件主题名称
        message['Subject'] = rw.read_config_file(CONFIG_DATA_PATH,"EMAIL_MESSAGE","SUBJECT")
        # --------------------------------------
        # 添加文本消息
        textMsg = rw.read_config_file(CONFIG_DATA_PATH,"EMAIL_MESSAGE","TEXT_MESSAGE")
        att = MIMEText(textMsg,"plain","utf-8")
        # 将正文添加到邮件中
        message.attach(att)
        # --------------------------------------
        # 获取最新测试报告
        fileList = os.listdir(REPORT_SAVE_PATH)
        path = sorted(fileList,key=lambda x:os.path.getctime(os.path.join(REPORT_SAVE_PATH,x)))
        newReport = REPORT_SAVE_PATH+path[-1]
        # 读取报告信息
        with open(newReport, "rb") as f:
            report = f.read()
        attachment = MIMEText(report,'base64','utf-8')
        # 附件内容类型
        attachment['Content-Type'] = 'application/octet-stream'
        # 附件处理 filename=('gbk','',"自动化测试报告.html")  # 文件名字有汉字设置编码
        attachment['Content-Disposition'] = 'attachment;filename=%s'%(newReport.split('\\')[-1])
        # 添加附件
        message.attach(attachment)
        # ==============发送邮件===============
        try:
            # 创建对象
            server = smtplib.SMTP_SSL(SMTP_SERVER,PORT)
            # 登录qq邮箱
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            # 发送邮件
            server.sendmail(SENDER_EMAIL,[RECEIVER_EAML],message.as_string())
            # 关闭服务
            server.close()
            print("邮件发送成功！")
        except:
            print("邮件发送失败！")
            raise


if __name__ == '__main__':

    s = SendEmail()
    s.send_email()





