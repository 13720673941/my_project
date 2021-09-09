# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/27 20:44

"""
.txt 文件读写
"""

from common.tools.logConfig import Logger

import os

Log = Logger().origin_logger


class OperateTxtData:

    def __init__(self, dataPath):
        # 检测文件路径是否存在
        if os.path.exists(dataPath):
            self.dataPath = dataPath
            Log.info(f"目录：{dataPath} 检索成功，正在获取文件中数据，请稍后...")
        else:
            raise Exception(f"项目中不存在该目录！！！{dataPath}")

    def read_txt_data(self) -> list:
        """
        读取txt文件数据
        :return:
        """
        with open(self.dataPath, "r", encoding="utf-8") as f:
            return [lineData.strip("\n") for lineData in f.readlines()]

    def write_txt_data(self, data: str or int):
        """
        txt文件中写入数据
        :param data:
        :return:
        """
        with open(self.dataPath, "a", encoding="utf-8") as f:
            f.write(data)
        Log.info(f"文件：{self.dataPath} 中写入一行数据：{data}")


if __name__ == '__main__':
    op = OperateTxtData("../../requirements").read_txt_data()
    print(op)
