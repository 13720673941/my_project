# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/18 20:14

"""
    利用threading模块进行接口压测
"""

import requests,threading,re,time

event = threading.Event()


def get_session():

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cookie":"MSO=SID&1579350070",
        "Referer":"keep-alive",
        "Connection":"keep-alive",
    }
    try:
        r = requests.get(url="http://127.0.0.1:1080/WebTours/nav.pl?in=home",headers=headers)
        regex = re.compile(r"name=userSession value=(.*?)>")
        return regex.findall(r.text)[0]
    except Exception as e:
        print(e)

request_tm = []
Pass = []
Fail = []

def login(event,i):
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"MSO=SID&1579351869",
        "Content-Length":"128"
    }
    body = {
        "userSession":get_session(),
        "username":"13720673941",
        "password":"111111",
        "login.x":"61",
        "login.y":"7",
        "JSFormSubmit":"off"
    }

    thread = threading.Thread()

    print("线程 {} 初始化完毕，随时可以启动...\n".format(i))

    event.wait()

    time.sleep(5)

    print("线程 {} 开始执行...\n".format(i))
    time.sleep(5)
    try:

        r = requests.post(url="http://127.0.0.1:1080/WebTours/login.pl",headers=headers,data=body)
        request_tm.append(r.elapsed.total_seconds())

        if r.status_code == 200:
            Pass.append(r.status_code)
            print("第 {thread_num} 线程请求成功！协议状态码：{status_code}\n".format(thread_num=i,status_code=r.status_code))
        else:
            Fail.append(r.status_code)
            print("第 {thread_num} 线程请求异常！协议状态码：{status_code}\n".format(thread_num=i,status_code=r.status_code))
    except Exception as e:
        print(e)

thread_list = []

def run(thread_num):

    for i in range(1,thread_num+1):
        thread_list.append(threading.Thread(target=login,args=(event,i)))

    event.clear()
    for thread in thread_list:
        thread.start()

    event.set()
    for thread in thread_list:
        thread.join()


thread_num = 20

run(thread_num)

