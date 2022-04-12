"""

"""
import json
import logging
from string import Template

import yaml

from config import settings
from config.sql.sql import query_city
from utils.utils import db


class GetDate:
    def __init__(self):
        self.db = db(settings.DB[0])

    def _get_date(self, args):
        # self.db.execute(query_city, args=args)
        self.db.execute(query_city, args=args, flag=False)
        _ = self.db.cursor.fetchone()
        logging.info(f"fetchone:{_}")
        return _

    def date_get(self):
        with open(f"{settings.BASE_DIR}/ddt/get.yaml", "r") as f:
            o_ = yaml.safe_load_all(f.read())
            logging.debug(f"yaml文件序列化为python对象：{o_}")
            unpack = tuple(o_)
            logging.debug(f"获取生成器对象数据：{unpack}")
        payload, case, expect = unpack
        l_ = []
        for i in case:
            _ = Template(json.dumps(payload)).safe_substitute(
                **settings.domain,
                **settings.headers,
                **self._get_date(i)
            )
            l_.append((yaml.safe_load(_), expect))
        self.db.close()
        logging.debug(f"测试用例输入数据和预期结果：{l_}")
        return l_
