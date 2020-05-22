# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project        zk3
   File Name:     logHandler
   Description :  日志操作模块
   Author :       Xdao
   date:          2020/5/22 11:00
-------------------------------------------------
                  
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))  # abs绝 --> 相
print(os.path.abspath(__file__))
print(CURRENT_PATH)
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)  # os.pardir() 获取当前目录的父目录（上一级目录）
print(os.pardir)
print(ROOT_PATH)

LOG_PATH = os.path.join(ROOT_PATH, 'log')

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class LogHander(logging.Logger):
    """
    LogHandler
    """

    def __init__(self, name, level=DEBUG, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __setFileHandler__(self, level=None):
        file_name = os.path.join(LOG_PATH, f'{self.name}.log')
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1)  # backupCount 默认为0，不会自动删除文件
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)

        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        set stream handler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def resetName(self, name):
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()

