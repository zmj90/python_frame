"""

"""
import json
import logging
import os
import random
from string import Template

import yaml

from config import settings
from config.sql.sql import *
from utils.utils import db, SeqHelper, YamlHelper


class ProContest:
    def __init__(self, fmt=True):
        """

        :param fmt:
        """
        self.db = db(settings.DB[0], fmt)

    def load(self):
        pass

    def query__ids(self, sql, args=None):
        """

        :param sql:
        :param args:
        :return:
        """
        _ = self.db.fetch(sql, args=args, flags=-1)
        if isinstance(_, list):
            # dict
            _ = SeqHelper.get_values(_, lambda item, tp: str(item[tp[0]]))
        else:
            # tuple
            _ = SeqHelper.get_values(_, lambda item: str(item[0]))
        logging.debug(f"{_}:{type(_)}")
        _ = list(_)
        logging.debug(_)
        return _


class GetDate(ProContest):
    def __init__(self, fmt=True):
        """

        :param fmt:
        """
        super().__init__(fmt=fmt)
        self.file = os.path.join(settings.BASE_DIR, "ddt", "get.yaml")

    def load(self):
        """

        :return:
        """
        payload, case, expect = YamlHelper.yaml_loads(self.file)
        l_ = []
        for i in case:
            _ = Template(json.dumps(payload)).safe_substitute(
                **settings.domain,
                **settings.headers,
                **self.db.fetch(query_city, args=i, flags=0),
                vendors=random.choice(self.query__ids(query_vendors))
            )
            l_.append((yaml.safe_load(_), expect))
        self.db.close()
        return l_


class Vendors(ProContest):
    def __init__(self, fmt=True):
        """

        :param fmt:
        """
        super().__init__(fmt=fmt)
        self.file = os.path.join(settings.BASE_DIR, "ddt", "get_vendors.yaml")

    def load(self):
        """

        :return:
        """
        payload, expect = YamlHelper.yaml_loads(self.file)
        expect |= {"ids": self.query__ids(query_vendors)}
        _ = Template(json.dumps(payload)).safe_substitute(
            **settings.domain,
            **settings.headers,
            all="郫都"
        )
        payload = yaml.safe_load(_)
        self.db.close()
        return [(payload, expect)]
