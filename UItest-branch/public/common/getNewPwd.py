# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/1 23:51

from public.common import rwConfig

def get_new_pwd():

    # 固定修改密码为列表中的两个密码
    password_list = ["111111", "222222"]
    # 获取旧密码
    old_pwd = rwConfig.read_config_data("T西安好家帮家政有限公司","password")
    # 初始化新密码
    new_pwd = None
    for pwd in password_list:
        if pwd != old_pwd:
            # 获取新密码
            new_pwd = pwd

    return old_pwd,new_pwd