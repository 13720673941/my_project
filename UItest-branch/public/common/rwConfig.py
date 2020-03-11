# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/25 22:13

from configparser import ConfigParser
from config.pathConfig import *

# 获取配置文件路径，默认文件路径
Data = accountDataPath
def read_config_data(section,option,DataPath=Data):
    """
    读取ini配置文件
    """
    cf = ConfigParser()
    cf.read(DataPath,encoding="utf-8")
    return cf.get(section,option)

def write_config_data(section,option,writeData,DataPath=Data):
    """
    写入ini配置文件
    """
    cf = ConfigParser()
    cf.read(DataPath,encoding='utf-8')
    cf.set(section,option,writeData)
    with open(DataPath,'w',encoding='utf-8') as f:
        cf.write(f)
    print(' * Write success value: {0} in {1} {2}'.format(writeData,section,option))


def write_txt_data(data_path,write_data):
    """
    写入txt文件
    :return:
    """
    with open(data_path,"a",encoding="utf-8") as f:
        f.write(write_data)
