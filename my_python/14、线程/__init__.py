# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/18 20:14

import threading,requests,re,time
from selenium import webdriver

def get_session():

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cookie":"MSO=SID&1579350070",
        "Referer":"keep-alive",
        "Connection":"keep-alive",
    }
    r = requests.get(url="http://127.0.0.1:1080/WebTours/nav.pl?in=home",headers=headers)
    regex = re.compile(r"name=userSession value=(.*?)>")
    return regex.findall(r.text)[0]

class MyThread(threading.Thread):

    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        print("线程{}已初始化完成，随时准备启动....".format(self.name))
        # 设置线程等待
        self.event.wait()
        print("{}开始执行...".format(self.name))
        time.sleep(1)
        d = webdriver.Chrome()
        d.maximize_window()



        # time.sleep(5)
        #
        # headers = {
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "Cookie": "MSO=SID&1579351869",
        #     "Content-Length": "128"
        # }
        # body = {
        #     "userSession": get_session(),
        #     "username": "13720673941",
        #     "password": "111111",
        #     "login.x": "61",
        #     "login.y": "7",
        #     "JSFormSubmit": "off"
        # }
        # try:
        #
        #     r = requests.post(url="http://127.0.0.1:1080/WebTours/login.pl", headers=headers, data=body)
        #     # request_tm.append(r.elapsed.total_seconds())
        #
        #     if r.status_code == 200:
        #         # Pass.append(r.status_code)
        #         print("\n第 {thread_num} 线程请求成功！协议状态码：{status_code}".format(thread_num=self.name, status_code=r.status_code))
        #     else:
        #         # Fail.append(r.status_code)
        #         print("\n第 {thread_num} 线程请求异常！协议状态码：{status_code}".format(thread_num=self.name, status_code=r.status_code))
        # except Exception as e:
        #     print(e)

if __name__ == '__main__':

    event = threading.Event()
    threads = []

    for i in range(1,20):
        threads.append(threading.Thread(target=MyThread(event).run))
    # 必须在子线程start之前先清空所有的event设置，让子线程的event.wait生效
    event.clear()
    [t.start() for t in threads]
    # 设置event事件，事件设置后将通知所有设置了事件对象的线程激活
    event.set()
    [t.join() for t in threads]