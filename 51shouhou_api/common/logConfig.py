# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/17 20:50

from common import filePath
import datetime

class Log:

    def __init__(self):

        # 定义当前时间格式
        self.now_time = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        # 定义日志保存路径
        self.log_save_path = filePath.log_save_path + str(datetime.datetime.now().date())+".txt"

    def write_txt(self,message):

        # 写入txt文件
        with open(self.log_save_path,"a",encoding="gbk") as f:
            f.write("\n"+message)

    def info(self,message):

        # 加宫所要打印的字段
        log_txt = self.now_time + "-INFO-: " + message
        # 控制台打印
        print(log_txt)
        # 保存到日志文件
        self.write_txt(log_txt)

    def error(self,message):

        # 加宫所要打印的字段
        log_txt = self.now_time + "-ERROR-: " + message
        # 控制台打印
        print(log_txt)
        # 保存到日志文件
        self.write_txt(log_txt)

    def warning(self,message):

        # 加宫所要打印的字段
        log_txt = self.now_time + "-WARNING-: " + message
        # 控制台打印
        print(log_txt)
        # 保存到日志文件
        self.write_txt(log_txt)



