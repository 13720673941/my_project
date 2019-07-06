# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/24 17:15

import json
from config.pathconfig import *

def get_test_data():
    """
    获取json类型的测试数据
    :return:
    """
    with open(testData,encoding='utf-8') as f:
        # 适用json模块读取是字典格式的
        return json.load(f)


# print(GetJsonData())