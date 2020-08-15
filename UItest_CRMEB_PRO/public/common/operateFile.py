# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/14 17:28

"""
配置文件读取方法
"""

from configparser import ConfigParser
from config.pathConfig import *

class OperateFile:

    def get_config_data(self,section,option,path=GLOBAL_PARAMS_PATH):
        """获取配置文件 .ini 类型数据"""

        cf = ConfigParser()
        cf.read(path,encoding="utf-8")
        return cf.get(section,option)


if __name__ == '__main__':

    cf = OperateFile()
    data = cf.get_config_data("GLOBAL_URL","URL")
    print(data)