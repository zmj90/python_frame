"""
工具助手
"""
import datetime
import json
import logging
import random
import time
from functools import wraps
from string import Template
import sys
from typing import (
    Tuple
)

import pymysql.cursors
import requests
import yaml
from faker import Faker
from faker.providers import BaseProvider
from pymongo import MongoClient
from openpyxl import load_workbook

from common.config.settings import EXPECT, URL_HOME

__author__ = "钟马俊 WX996578 <zhongmajun@h-partners.com>"


class DataBase:
    """
    操作数据库
    """

    def __init__(self, date_base: dict, fmt=True) -> None:
        """

        :param date_base: 数据库
        :param fmt: 查询时，返回() or ((),()) or {} or [{}, {}]
        """
        self.db = pymysql.connect(**date_base)
        self.cursor = self.db.cursor(
            cursor=pymysql.cursors.DictCursor if fmt else pymysql.cursors.Cursor
        )

    def close(self) -> None:
        """
        关闭数据库连接和操作对象
        :return: None
        """
        self.cursor.close()
        self.db.close()

    def execute(self, sql: str, args=None, flag=True) -> int:
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

    def fetch(self, sql, args=None, flags=0, num=None) -> tuple | Tuple[tuple] | dict | list[dict]:
        """
        查询结果
        :param sql: sql
        :param args: 可有可无，使用format也行
        :param flags: 为0，查询1条；为1查询多条；其他查询所有
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

    def call_proc(self, procedure, args=()):
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

    @staticmethod
    def get_time_interval(**kwargs):
        start, end = DTHelper.get_time("%Y/%m/%d", **kwargs), DTHelper.get_time("%Y/%m/%d")
        return f"{start}-{end}"


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
    def get_values(seq_target, key=None, index=None):
        """
        获取元素中的某个值
        :param seq_target: [{}, {}] or ((), ())
        :param key: 字典的key
        :param index: 序号
        :return: generate
        """
        if isinstance(seq_target[0], dict):
            return map(lambda ele: ele.get(key), seq_target)
        else:
            return map(lambda ele: ele[index], seq_target)


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
    def yaml_load(reader, mapping=None, **kwargs):
        """

        :param reader:
        :param mapping:
        :param kwargs:
        :return:
        """
        if mapping is None:
            mapping = {}
        if isinstance(reader, str):
            _ = yaml.safe_load(Template(reader).safe_substitute(mapping, **kwargs))
        elif isinstance(reader, (dict, list)):
            _ = yaml.safe_load(Template(json.dumps(reader)).safe_substitute(mapping, **kwargs))
        else:
            with open(reader[0], "r", encoding="utf8") as f:
                _ = yaml.safe_load(Template(f.read()).safe_substitute(mapping, **kwargs))
        logging.debug(f"yaml文件序列化为python对象：{_}")
        return _


class ReHelper:
    def __init__(self):
        pass


def request(payload, flag=True):
    """

    :param payload:
    :param flag:
    :return:
    """
    logging.info(f"输入数据：{payload}")
    _ = requests.request(**payload)
    # r_json = _.json()
    # _.encoding = "unicode_escape"
    # r_text = _.text
    r_text, r_json = _.text, _.json()
    logging.info(f"返回json：{r_json}")
    logging.info(f"返回text：{r_text}")
    if flag:
        return _.status_code, r_json
    return _.status_code, r_text, r_json


def com_assert_except(code, r_json, expect=EXPECT):
    """

    :param code:
    :param r_json:
    :param expect:
    :return:
    """
    try:
        assert code == 200
        assert r_json["status"] == expect["status"]
        assert r_json["errorCode"] == expect["error_code"]
        assert r_json["errorMsg"] == expect["error_msg"]
    except Exception as e:
        logging.exception(e)
        logging.info(type(e))
        raise e


def com_assert(code, r_json, expect=EXPECT):
    """

    :param code:
    :param r_json:
    :param expect:
    :return:
    """
    assert code == 200, logging.error(
        f"实际结果：{code}，没有等于预期结果：200"
    ) or f"assert '{code} == 200'"
    assert r_json['status'] == expect['status'], logging.error(
        f"实际结果：{r_json['status']}，没有等于预期结果：{expect['status']}"
    ) or f"assert '{r_json['status']}' == '{expect['status']}'"
    assert r_json['errorCode'] == expect['error_code'], logging.error(
        f"实际结果：{r_json['errorCode']}，没有等于预期结果：{expect['error_code']}"
    ) or f"assert '{r_json['errorCode']}' == '{expect['error_code']}'"
    assert r_json['errorMsg'] == expect['error_msg'], logging.error(
        f"实际结果：{r_json['errorMsg']}，没有等于预期结果：{expect['error_msg']}"
    ) or f"assert '{r_json['errorMsg']}' == '{expect['error_msg']}'"


def data_assert(expect, actual, fun):
    logging.info(f"预期结果：{expect}")
    logging.info(f"实际结果：{actual}")
    assert fun(expect, actual), logging.error(
        f"实际结果：'{actual}'，与预期结果'{expect}'不符"
    ) or f"assert 实际结果：'{actual}'，与预期结果'{expect}'不符"


def singleton(func):
    _instance_d = {}

    def wrapper(*args, **kwargs):
        if func not in _instance_d:
            _instance_d[func] = func(*args, **kwargs)
        return _instance_d.get(func)
    return wrapper


class MyProvider(BaseProvider):
    @staticmethod
    def uuid1():
        import uuid
        return uuid.uuid1(random.getrandbits(48))


@singleton
def fake():
    fake_cn = Faker("zh_CN")
    fake_cn.add_provider(MyProvider)
    return fake_cn


def y_safe_load(file):
    with open(file, "r", encoding="utf8") as f:
        # d = f.read()
        return yaml.safe_load(f)


def sleep(sec):
    if sys.platform == "win32":
        time.sleep(sec)


class MongoDB:
    """
    操作mongodb
    """
    def __init__(self, url, data_base):
        self.client = MongoClient(url)
        self.db = self.client[data_base]

    def col(self, collection):
        return self.db[collection]

    def close(self):
        self.client.close()


def excel_parse(excel_file: str) -> list[dict]:
    """
    解析excel
    :param excel_file:
    :return:
    """
    wb = load_workbook(excel_file)
    cases = []
    for s in wb:
        case = dict()
        case["name"] = s["B1"].value
        case["id"] = s["B2"].value
        case["actions"] = _excel_parse(s.values)
        cases.append(case)
    return cases


def _excel_parse(values):
    """
    生成器
    :param values:
    :return:
    """
    for v in values:
        if isinstance(v[0], int):
            step = dict()
            step["log"] = v[1]
            step["action"] = v[2]
            if v[3] is None:
                j_o = None
            else:
                j_o = json.loads(v[3])
                if j_o.get("url"):
                    j_o["url"] = f'{URL_HOME}{j_o["url"]}'
            step["param"] = j_o
            step["expect"] = v[4]
            yield step


class Compare:
    @staticmethod
    def equal(left, right):
        return left == right

    @staticmethod
    def contain(left, right):
        return left in right
