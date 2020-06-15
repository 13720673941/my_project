# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/18 21:24


import threading
import requests
import time
from logging模块 import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Pass = []
Fail = []
restime = []

event = threading.Event()

class Multi_thread():
    def get_info(self, sumget, i, URL2, param):
        for n in range(sumget):

            try:
                r = requests.get(URL2, params=param, timeout=10)
                restime.append(r.elapsed.total_seconds())

                if r.status_code == 200:
                    # print (res.text)
                    # print(res.status_code)
                    Pass.append(r.status_code)
                    logger.info(str((i + 1)) + '线程的第' + str(n + 1) + '次请求，请求成功，状态码' + str(r.status_code))
                else:
                    # print (res.status_code)
                    Fail.append(r.status_code)
                    logger.info(str(i * n) + '请求异常，状态码' + str(r.status_code))
                # time.sleep(10)
                # get_info()

            except Exception as e:
                print(e)

    def start(self, sumthread, sumget, URL2, param):
        threads = []
        n_t = 1
        for i in range(sumthread):
            threads.append(threading.Thread(target=Multi_thread.get_info(sumget, i, URL2, param), args=()))
        for t in threads:
            time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()

    def statistics(self, sumthread, sumget, URL2, param):
        Multi_thread.start(sumthread, sumget, URL2, param)
        print('请求通过次数：', len(Pass))
        print('请求异常次数：', len(Fail))
        print('总响应最大时长：', max(restime))
        print('总响应最小时长：', min(restime))
        print('总响应时长：', sum(restime))
        print('平均响应时长：', sum(restime) / len(restime))

        if (len(Fail)) == 0:
            print(str(sumthread) + '个线程，每个线程压力请求' + str(sumget) + '次,共计' + str(sumthread * sumget) + '次，没有请求异常')
        else:
            print('存在' + str(len(Fail)) + '个，请求异常')
            print(Fail)


if __name__ == '__main__':
    Multi_thread = Multi_thread()
    URL2 = 'http://www.kuaidi100.com/query'  # 地址
    param = {'type': 'zhongtong', 'postid': '73116039505988'}  # 参数
    sumthread = 10  # 线程数
    sumget = 1  # 每个线程请求次数

    Multi_thread.statistics(sumthread, sumget, URL2, param)
    input('Press Enter to exit...')