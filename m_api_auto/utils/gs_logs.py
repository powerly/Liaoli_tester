# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注:添加日志方法
import logging
import os

from config import env_constant


class Mylogger(object):
    def __init__(self, api):
        self.api = api

    def logger(self, message):
        logger = logging.getLogger(self.api)
        logger.setLevel(logging.DEBUG)
        # 消息格式化
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y/%m/%d %H:%M:%S')
        path = os.path.join(os.path.dirname(os.getcwd()))+'\logs\{}api_logs.log'.format(env_constant.ENVIORNMENT)
        # print(path)
        # 本地调试每次删除log文件后新生成log文件
        if not os.path.exists(path):
            open(path, 'w')
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setFormatter(formatter)
        logger.addHandler(fh)  # 给logger对象添加 handler
        logger.info(message)
        logger.removeHandler(fh)


if __name__ == '__main__':
    boss_logger = Mylogger('liaoli')
    boss_logger.logger('2021.03.03')
