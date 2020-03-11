# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/2/25 22:19

from pywifi import const,PyWiFi,Profile
import time,os

def isConnect():
    """查看无限网卡是否处于连接状态"""

    # 创建一个对象
    wifi = PyWiFi()
    # 获取第一个无限网卡
    first_wifi = wifi.interfaces()[0]

    if first_wifi.status() in [const.IFACE_CONNECTED,const.IFACE_CONNECTING]:
        print("无限网卡：{} 已连接".format(first_wifi))
    else:
        print("无限网卡：{} 断开连接".format(first_wifi))

def findWifiOfRound():
    """查找周围无线网"""

    # 创建一个对象
    wifi = PyWiFi()
    # 获取第一个无限网卡
    first_wifi = wifi.interfaces()[0]
    # 扫描周围无线网
    first_wifi.scan()
    wifiList = first_wifi.scan_results()
    for wifi in wifiList:
        print("wifi 名称：%s"%wifi.ssid)

def disConnectWifi():
    """断开无线网连接"""

    # 创建一个对象
    wifi = PyWiFi()
    # 获取第一个无限网卡
    first_wifi = wifi.interfaces()[0]
    # 断开无线网连接
    first_wifi.disconnect()

def connectWifi(wifi_name,wifi_password):
    """连接无线网"""

    # 创建一个对象
    wifi = PyWiFi()
    # 获取第一个无限网卡
    first_wifi = wifi.interfaces()[0]
    # 断开无线网连接
    first_wifi.disconnect()
    time.sleep(5)
    # wifi 配置类
    profile_info = Profile()
    # 配置wifi名称
    profile_info.ssid = wifi_name
    # 是否需要密码
    profile_info.auth = const.AUTH_ALG_OPEN
    # 密码加密类型
    profile_info.akm.append(const.AKM_TYPE_WPA2PSK)
    # 加密单元
    profile_info.cipher = const.CIPHER_TYPE_CCMP
    # wifi 密码
    profile_info.key = wifi_password
    # 删除其他配置文件
    first_wifi.remove_all_network_profiles()
    # 加载配置文件
    tmp_profile = first_wifi.add_network_profile(profile_info)
    # 连接
    first_wifi.connect(tmp_profile)
    time.sleep(5)
    if first_wifi.status() == const.IFACE_CONNECTED:
        return "无线网已连接"
    else:
        return "无线网连接失败"

def checkWifiIsConnect():
    # 查看本地网络连接是否正常，尝试ping百度是否正常
    network = os.popen("ping www.baidu.com")
    out = network.read()
    # 判断是否有网络
    while True:
        if "请求找不到主机" in out:
            print("......网络连接错误！！！")
            # 断开重新连接无线网
            wifiStatus = connectWifi(wifi_name="DengPF",wifi_password="peng123456")
            if wifiStatus == "无线网已连接":
                print("......无线网已重新连接 ！")
                break
            else:
                raise IOError("......无线网连接异常！！！")
        else:
            print("网络连接正常......")
            break