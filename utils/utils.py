"""

"""
import datetime
import logging
import re
import time
from functools import wraps
from string import Template

import pymysql.cursors
import requests
import yaml

from config.settings import EXPECT


class DataBase:
    """
    操作数据库
    """

    def __init__(self, date_base, fmt=True):
        """

        :param date_base: 数据库
        :param fmt: 查询时，返回() or ((),()) or {} or [{}, {}]
        """
        self.db = pymysql.connect(**date_base)
        self.cursor = self.db.cursor(
            cursor=pymysql.cursors.DictCursor if fmt else pymysql.cursors.Cursor
        )

    def close(self):
        """
        关闭数据库连接和操作对象
        :return: None
        """
        self.cursor.close()
        self.db.close()

    def execute(self, sql, args=None, flag=True):
        """

        :param sql: sql
        :param args: sql中的替代值，也可以不需要
        :param flag: if true 执行1条sql
        :return: Number of affected rows
        """
        try:
            if flag:
                logging.debug(f"sql语句:{self.cursor.mogrify(sql, args)}")
                rows = self.cursor.execute(sql, args=args)
            else:
                for arg in args:
                    logging.debug(f"sql语句:{self.cursor.mogrify(sql, arg)}")
                rows = self.cursor.executemany(sql, args=args)
            self.db.commit()
            return rows
        except Exception as e:
            self.db.rollback()
            logging.exception(e)

    def fetch(self, sql, args=None, flags=0, num=None):
        """
        查询结果
        :param sql: sql
        :param args: 可有可无，使用format也行
        :param flags: 为0，查询1条；为查询多条；其他查询所有
        :param num: 查询数量
        :return: () or ((),()) or {} or [{}, {}]
        """
        self.execute(sql, args=args)
        if flags == 0:
            res = self.cursor.fetchone()
        elif flags == 1:
            res = self.cursor.fetchmany(num)
        else:
            res = self.cursor.fetchall()
        logging.debug(f"查询结果：{res}，类型：{type(res)}")
        return res

    def call_proc(self,procedure, args=()):
        self.cursor.callproc(procedure, args=args)


db = DataBase


class DTHelper:
    @staticmethod
    def get_time(date_fmt=None, flag=True, *, days=0, seconds=0, minutes=0, hours=0):
        """
        获取格式化的时间（相当于当前时间的时间点）
        :param date_fmt: 格式，格式不为None，以该格式为准
        :param flag: true，默认显示年月日；false，显示年月日时分秒
        :param days: 天
        :param seconds: 秒
        :param minutes: 分
        :param hours: 时
        :return: str
        """
        dt = datetime.datetime.now() + datetime.timedelta(
            days=days, seconds=seconds, minutes=minutes, hours=hours
        )
        if date_fmt:
            return datetime.datetime.strftime(dt, date_fmt)
        if flag:
            return datetime.datetime.strftime(dt, "%Y-%m-%d")
        return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")


def consume_time(test_func):
    """
    计算运行test_func的时间
    :param test_func: 方法或函数
    :return:
    """
    @wraps(test_func)
    def wrapper(*args):
        start = time.time()
        test_func(*args)
        end = time.time()
        logging.info(f"执行时间：{end-start}")
    return wrapper


class SeqHelper:
    @staticmethod
    def get_values(seq_target, func):
        """
        获取元素中的某个值
        :param seq_target: [{}, {}] or ((), ())
        :param func: lambda表达式
        :return: generate
        """
        for i in seq_target:
            if isinstance(i, dict):
                yield func(i, tuple(i))
            else:
                yield func(i)


class YamlHelper:
    @staticmethod
    def yaml_loads(file):
        """

        :param file:
        :return:
        """
        with open(file, "r", encoding="utf8") as f:
            o_ = yaml.safe_load_all(f)
            logging.debug(f"yaml文件序列化为python对象：{o_}")
            unpack = tuple(o_)
            logging.debug(f"获取生成器对象数据：{unpack}")
        return unpack

    @staticmethod
    def yaml_load(file, mapping=None, **kwargs):
        """

        :param file:
        :param mapping:
        :param kwargs:
        :return:
        """
        if mapping is None:
            mapping = {}
        with open(file, "r", encoding="utf8") as f:
            _ = Template(f.read()).safe_substitute(mapping, **kwargs)
            _ = yaml.safe_load(_)
        logging.debug(f"yaml文件序列化为python对象：{_}")
        return _


class ReHelper:
    def __init__(self):
        pass


def request(payload, expect=EXPECT, flag=True):
    """

    :param payload:
    :param expect:
    :param flag:
    :return:
    """
    logging.info(f"输入数据：{payload}；预期结果：{expect}")
    _ = requests.request(**payload)
    text_, json_ = _.text, _.json()
    logging.info(f"相应数据：{json_}")
    logging.info(f"text：{text_}")
    if flag:
        return _.status_code, json_
    return _.status_code, text_, json_


def com_assert_bak(code, json_, expect=EXPECT):
    """

    :param code:
    :param json_:
    :param expect:
    :return:
    """
    try:
        assert json_["status"] == expect["status"]
        assert json_["errorCode"] == expect["error_code"]
        assert json_["errorMsg"] == expect["error_msg"]
    except Exception as e:
        logging.exception(e)
        logging.debug(type(e))
        raise e


def com_assert(code, json_, expect=EXPECT):
    """

    :param code:
    :param json_:
    :param expect:
    :return:
    """
    assert code == 200, logging.error(
        f"实际结果：{code}，没有等于预期结果：200"
    ) or f"assert '{code} == 200'"
    assert json_['status'] == expect['status'], logging.error(
        f"实际结果：{json_['status']}，没有等于预期结果：{expect['status']}"
    ) or f"assert '{json_['status']}' == '{expect['status']}'"
    assert json_['errorCode'] == expect['error_code'], logging.error(
        f"实际结果：{json_['errorCode']}，没有等于预期结果：{expect['error_code']}"
    ) or f"assert '{json_['errorCode']}' == '{expect['error_code']}'"
    assert json_['errorMsg'] == expect['error_msg'], logging.error(
        f"实际结果：{json_['errorMsg']}，没有等于预期结果：{expect['error_msg']}"
    ) or f"assert '{json_['errorMsg']}' == '{expect['error_msg']}'"


def data_assert(actual, expect, fun):
    """

    :param actual:
    :param expect:
    :param fun:
    :return:
    """
    assert fun(actual, expect), logging.error(
        f"实际结果：'{actual}'，与预期结果'{expect}'不符"
    ) or f"assert 实际结果：'{actual}'，与预期结果'{expect}'不符"
