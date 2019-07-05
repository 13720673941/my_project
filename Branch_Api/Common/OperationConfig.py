# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59
import os,logging
from configparser import ConfigParser
from Common import Public

'''
config配置文件的读取和写入
'''
class operationConfig(object):

    def __init__(self):

        '''获取配置文件路径'''
        self.DataPath = Public.data_dir(filename="BaseConfig.ini")
        self.cf = ConfigParser()
        self.cf.read(self.DataPath, encoding='utf-8')

    def readConfig(self,section,option):

        '''
        :param DomeName: 读取的配置文件的名称
        :param section: 配置文件标题信息
        :param option:  配置文件的KEY值
        '''
        data = self.cf.get(section,option)
        return data

    def writeConfig(self,section,option,value):

        '''
        :param DomeName: 读取的配置文件的名称
        :param section: 配置文件标题信息
        :param option: 配置文件的KEY值
        :param value: 索要设置的option的值信息
        '''
        self.cf.set(section,option,value)
        with open(self.DataPath,"w") as f:
            self.cf.write(f)
            logging.info("成功写入公用参数：%s"%option)


