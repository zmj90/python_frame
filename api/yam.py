"""

"""
import re

from api.base import DataUnit
from common.config.settings import DOMAIN, HEADERS
from common.sql import sql
from utils.utils import YamlHelper, fake


class YamlPayLoader:
    @staticmethod
    def load(reader, **kwargs):
        return YamlHelper.yaml_load(reader, **DOMAIN, **HEADERS, **kwargs)


class YamlParamHandler(DataUnit):
    def __init__(self, params):
        super().__init__()
        self.params = params

    def sql(self):
        r = {}
        for _0 in self.params.get("sql"):
            _0[0] = getattr(sql, _0[0])
            r |= self.db.fetch(*_0)
        return r

    def sql_one(self):
        r = {}
        for _0 in self.params.get("sql_one"):
            key, sa = _0
            ra = RA(one_kvs=sa)
            r |= {key: ra.kvs_one().get(key)}
        return r

    def sql_choice(self):
        r = {}
        for _0 in self.params.get("sql_choice"):
            _0[0] = getattr(sql, _0[0])
            r |= self.db.fetch(*_0, flags=-1)
        return r

    def text(self):
        r = {}
        for _0 in self.params.get("text"):

            r |= {_0[1]: getattr(fake(), _0[0])()}
        return r


class AssertHandler(DataUnit):
    def __init__(self, r_text):
        super().__init__()
        self.r_text = r_text

    def re_parse(self, pattern):
        return self.re_parses(pattern)[0]

    def re_parses(self, pattern):
        r = re.findall(pattern, self.r_text)
        r = list(map(lambda i: i.encode().decode("unicode_escape"), r))
        return r

    @staticmethod
    def sql_one(l_param):
        key, sa = l_param
        ra = RA(one_kvs=sa)
        return ra.kvs_one().get(key)

    def sql(self, l_param, key):
        l_param[0] = getattr(sql, l_param[0])
        return self.db.fetch(*l_param).get(key)

    def re_searches(self, pattern, l_index):
        s = re.search(pattern, self.r_text)
        r = s.group(*l_index)
        return list(r)


class RA:
    _instance = None
    one_kvs = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            db = DataUnit().db
            cls.one_kvs = cls.get_one_kvs(db, kwargs.get("one_kvs"))
            db.close()
        return cls._instance

    @classmethod
    def get_one_kvs(cls, db, args):
        args[0] = getattr(sql, args[0])
        return db.fetch(*args)

    def kvs_one(self):
        return self.one_kvs
