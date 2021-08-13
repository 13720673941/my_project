# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 15:54

from configparser import ConfigParser
from ruamel import yaml
import json

"""
    读写 txt ini json yaml 格式文件
"""

class RWFile():

    def read_txt_file(self,filePath):
        """
        :param filePath: 文件路径
        :return:
        """
        newList = []
        # 读取txt类型文件返回列表
        with open(filePath,"r",encoding="utf-8") as f:
            # 默认读取返回列表
            for line in f.readlines():
                newList.append(line.replace("\n",""))
            return newList

    def write_txt_file(self,filePath,writeInfo,writeMode="a"):
        """
        :param filePath:    文件路径
        :param writeMode:   写入文件类型
        :return:
        """
        # 判断追加类型
        if writeMode not in ["a","w","w+"]:
            raise TypeError("写入文件类型: {}有误！writeMode允许类型：a、w、w+".format(writeMode))
        # 写入txt文件默认追加写入
        with open(filePath,writeMode,encoding="utf-8") as f:
            f.write(writeInfo+"\n")

    def read_config_file(self,filePath,section,option):
        """
        :param filePath: 文件路径
        :param section: 标题
        :param option:  键值
        :return:
        """
        cf = ConfigParser()
        cf.read(filePath,encoding="utf-8")
        return cf.get(section,option)

    def write_config_file(self,filePath,section,option,value,addSection=False):
        """
        :param filePath: 文件路径
        :param section: 标题
        :param option: 键值
        :param value: 写入参数
        :param addSection: 默认不添加标题
        :return:
        """
        cf = ConfigParser()
        cf.read(filePath,encoding="utf-8")
        # 没有section添加section
        if addSection:
            cf.add_section(section)
        cf.set(section,option,value)
        with open(filePath,"w",encoding="utf-8") as f:
            cf.write(f)

    def read_json_file(self,filePath):
        """
        :param filePath: 文件路径
        :return:
        """
        with open(filePath,"r",encoding="utf-8") as f:
            return json.load(f)

    def write_json_file(self,filePath,value):
        """
        :param filePath: 文件路径
        :param value:   写入数据
        :return:
        """
        # 写入json数据，需先读取源文件数据，修改字典值后再进行写入
        # ** 文件会覆盖源文件
        with open(filePath,"w",encoding="utf-8") as f:
            json.dump(value,f)

    def read_yaml_file(self,filePath):
        """
        :param filePath: 文件路径
        :return:
        """
        with open(filePath,"r",encoding="utf-8") as f:
            return yaml.load(f,Loader=yaml.Loader)

    def write_yaml_file(self,filePath,value):
        """
        :param filePath: 文件路径
        :param value:   写入数据
        :return:
        """
        # 写入json数据，需先读取源文件数据，修改字典值后再进行写入
        # ** 文件会覆盖源文件
        with open(filePath,"w",encoding="utf-8") as f:
            yaml.dump(value,f,Dumper=yaml.RoundTripDumper) # Dumper 标准yaml文件格式