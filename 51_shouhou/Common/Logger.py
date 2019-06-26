# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

import logging

def logFormat(logFile):
    # logging.basicConfig(level=logging.INFO,  # 设置日志级别
    #                     # 指定输出格式及内容
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     #filemode='w'  # 指定日志的打开方式一般默认为'w'/'a'
    #                     )

    if logFile==None:
        pass
    else:
        #输出日志到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s[%(filename)s(line:%(lineno)d)]%(levelname)s:%(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

def setFormatter(logFile):

    global logger,fh,ch
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(logFile,'w')

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()

    # 定义handler的输出格式format
    format1 = logging.Formatter('%(asctime)s[%(filename)s(line:%(lineno)d)]%(levelname)s: %(message)s')
    format2 = logging.Formatter('[%(filename)s-(line:%(lineno)d)]%(levelname)s:%(message)s')
    fh.setFormatter(format1)
    ch.setFormatter(format2)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

def removeHandler():
    #避免日志重复
    logger.removeHandler(fh)
    logger.removeHandler(ch)



'''
# 这个是日志保存本地的路径
log_path = "E:\\MyWork\\Super_shouhou\\Log\\"
class Log:

    def __init__(self):
         # 文件的命名
         self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d %H %M %S'))
         self.logger = logging.getLogger()
         self.logger.setLevel(logging.DEBUG)
         # 日志输出格式
         self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    def __console(self, level, message):
        #创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("输入密码")
    log.warning("----测试结束----")
'''
# logging.info('aaa')