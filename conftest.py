"""
https://docs.python.org/zh-cn/3/library/logging.html
"""
import logging
import logging.handlers
import os
import time

import config.settings as settings


def _Logger():
    # 创建记录器
    logger_ = logging.getLogger()
    logger_.setLevel(logging.DEBUG)

    # 创建console处理器
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)

    # 创建TimeRotatingFileHandler
    log_file = os.path.join(settings.BASE_DIR, "log", f"{time.strftime('%Y-%m-%d', time.localtime())}.log")
    th = logging.handlers.TimedRotatingFileHandler(log_file, when="d", interval=1)
    th.setLevel(logging.DEBUG)

    # 创建格式器
    fmt, date_fmt = \
        "%(levelname)-8s:%(asctime)s:%(filename)-10s:%(funcName)s:%(name)s:line%(lineno)4d:%(message)s",\
        "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt, date_fmt)

    # 处理器设置格式器
    # ch.setFormatter(formatter)
    th.setFormatter(formatter)

    # 记录器添加处理器
    # logger_.addHandler(ch)
    logger_.addHandler(th)

    return logger_


logger = _Logger()
