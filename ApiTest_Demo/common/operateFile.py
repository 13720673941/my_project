# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:36

"""
    文件读写
"""

from configparser import ConfigParser
from config.pathConfig import *
from ruamel import yaml

class OperateFile():

    def __init__(self):
        self.cf = ConfigParser()

    def read_config(self,section,option,configPath):
        """读取 ini 类型配置文件"""
        self.cf.read(configPath,encoding="utf-8")
        return self.cf.get(section,option)

    def write_config(self,section,option,value,configPath):
        """写入 ini 类型配置文件"""
        self.cf.read(configPath,encoding="utf-8")
        self.cf.set(section,option,value)
        # 写入
        with open(configPath,"w",encoding="utf-8") as f:
            self.cf.write(f)

    def read_yaml(self,filePath=REQUEST_DATA_PATH):
        """读取yaml文件数据"""
        with open(filePath,"r",encoding="utf-8") as f:
            return yaml.load(f,Loader=yaml.Loader)



if __name__ == '__main__':
    r = OperateFile()
    r.write_config("GLOBAL_PARAMS","TOKEN","aaaaaaaaaaaaa",GLOBAL_PARAMS_PATH)