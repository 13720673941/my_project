# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 23:12

"""
相关配置文件、数据读取和写入方法
"""

from configparser import ConfigParser
from public.common.logConfig import Logger

import yaml
import os

Log = Logger().origin_logger


class ReadWriteData:

    def __init__(self, dataPath):
        # 检测文件路径是否存在
        if os.path.exists(dataPath):
            self.dataPath = dataPath
            Log.info("目录：{} 检索成功，正在获取文件中数据，请稍后...".format(dataPath))
        else:
            raise Exception("项目中不存在该目录！！！{}".format(dataPath))

    def read_config_data(self, section, option):
        """
        读取.ini配置文件
        :param section: 标题
        :param option: 变量
        :return:
        """
        cf = ConfigParser()
        cf.read(filenames=self.dataPath, encoding="utf-8")
        readData = cf.get(section, option)
        Log.info("读取.ini配置文件，section：{}，option：{}，value：{}".format(section, option, readData))
        return readData

    def write_config_data(self, section, option, value):
        """
        写入.ini配置文件
        :param section: 标题
        :param option: 变量
        :param value: 值
        :return:
        """
        cf = ConfigParser()
        cf.read(filenames=self.dataPath, encoding="utf-8")
        cf.set(section, option, value)
        with open(file=self.dataPath, mode="w", encoding="utf-8") as f:
            cf.write(f)
        Log.info("正在配置文件中写入，section：{}，option：{}，value：{}".format(section, option, value))


if __name__ == '__main__':
    from config.filePathConfig import configDataPath

    rw = ReadWriteData(configDataPath).read_config_data("CHROME_DRIVER_PATH", "path")
    print(rw)
