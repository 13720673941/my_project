# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/6 11:44

from configparser import ConfigParser
from common import filePath

class OperateConfig():

    """
    操作config配置文件的读取、写入功能
    """

    def __init__(self):

        # 实例化类
        self.cf = ConfigParser()
        # 读取文件路径
        self.cf.read(filePath.publicData_path,encoding="utf-8")

    def read_config_data(self,section,option):
        """读取配置文件"""

        # 读取需要的文本信息
        return self.cf.get(section,option)

    def write_config_data(self,section,option,data):
        """写入配置文件"""

        # 设置写入的字段信息
        self.cf.set(section,option,data)
        # 写入
        with open(filePath.publicData_path,"w") as f:
            self.cf.write(f)



# OperateConfig().write_config_data("header_info","token","hhhhhhhh")
# a = OperateConfig().read_config_data("header_info","token")
# print(a)
