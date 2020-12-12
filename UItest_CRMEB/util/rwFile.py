# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/6 3:40

"""
.txt .ini .json .yaml 文件读写封装，文件夹路径需在 fileConfig.py 文件中配置
"""
import json
import os

from configparser import ConfigParser
from ruamel import yaml
from util.log import Log

# 实例化日志类
log = Log().logger


class ReadWriteFile:

    def __init__(self, filePath):
        # 实例化config类
        self.cf = ConfigParser()
        # 判断是否存在该文件
        if os.path.exists(filePath):
            self.filePath = filePath
            log.info("检测文件路径成功: {}，正在获取数据信息...".format(filePath))
        else:
            raise OSError("文件路径不存在！！！")

    def read_ini_file(self, section, option):
        """读取.ini类型配置文件"""
        try:
            self.cf.read(self.filePath, encoding="utf-8")
            value = self.cf.get(section, option)
            log.info("获取配置文件数据成功，section: {}，option: {}，value: {}".format(section, option, value))
            return value
        except Exception:
            raise NameError("配置文件中不存在section、option！！！")

    def write_ini_file(self, section, option, value):
        """写入.ini类型配置文件"""
        try:
            self.cf.read(self.filePath, encoding="utf-8")
            self.cf.set(section, option, value)
            with open(self.filePath, "w", encoding="utf-8") as f:
                self.cf.write(f)
            log.info("配置文件中 ‘{}’ 下写入数据 ‘{}={}’ 成功".format(section, option, value))
        except Exception:
            raise NameError("配置文件中不存在section: {}！！！".format(section))

    def read_json_file(self):
        """读取.json文件"""
        with open(self.filePath, "r", encoding="utf-8") as f:
            jsonData = json.load(f)
            log.info("读取json文件数据信息成功！")
        return jsonData

    def write_json_file(self, value):
        """写入.json文件"""
        # 写入json数据，需先读取源文件数据，修改字典值后再进行写入
        # ** 文件会覆盖源文件
        with open(self.filePath, "w", encoding="utf-8") as f:
            json.dump(value, f)
        log.info("json数据写入成功！")

    def read_txt_file(self):
        """读取.txt类型文件"""
        newList = []
        # 读取txt类型文件返回列表
        with open(self.filePath, "r", encoding="utf-8") as f:
            # 默认读取返回列表
            for line in f.readlines():
                newList.append(line.strip("\n"))
            log.info("读取txt文件数据信息成功！")
        return newList

    def write_txt_file(self, writeInfo, writeMode="a"):
        """写入.txt类型文件"""
        # 判断追加类型
        if writeMode not in ["a", "w", "w+"]:
            raise TypeError("写入文件类型: {}有误！writeMode允许类型：a、w、w+".format(writeMode))
        # 写入txt文件默认追加写入
        with open(self.filePath, writeMode, encoding="utf-8") as f:
            f.write(writeInfo + "\n")
        log.info("数据: {}，写入txt文件成功！".format(writeInfo))

    def read_yaml_file(self):
        """读取yaml类型文件"""
        with open(self.filePath, "r", encoding="utf-8") as f:
            yamlData = yaml.load(f, Loader=yaml.Loader)
            log.info("读取yaml文件数据成功！")
        return yamlData

    def write_yaml_file(self, value):
        """写入yaml类型文件"""
        # 写入yaml数据，需先读取源文件数据，修改字典值后再进行写入
        # ** 文件会覆盖源文件
        with open(self.filePath, "w", encoding="utf-8") as f:
            # Dumper 标准yaml文件格式
            yaml.dump(value, f, Dumper=yaml.RoundTripDumper)
        log.info("读取txt文件数据信息成功！")


if __name__ == '__main__':
    # from config.fileConfig import *

    # 测试代码
    rw = ReadWriteFile(filePath="C:\\Users\\kk\\Desktop\\ym.yaml")
    print(rw.read_yaml_file())
