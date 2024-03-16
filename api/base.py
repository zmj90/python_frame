"""

"""
import logging

from common.config import settings
from common.sql import sql
from utils.utils import db, SeqHelper


class DataUnit:
    def __init__(self, fmt=True):
        """

        :param fmt:
        """
        self.db = db(settings.DB[0], fmt)

    def query_values(self, sql_p, args=None, key=None, index=None):
        """

        :param sql_p: sql名称或sql语句
        :param args:
        :param key:
        :param index:
        :return:
        """
        sql_p = getattr(sql, sql_p, sql_p)
        r_all = self.db.fetch(sql_p, args=args, flags=-1)
        if isinstance(r_all[0], dict):
            # dict
            g_ = SeqHelper.get_values(r_all, key=key)
        else:
            # tuple
            g_ = SeqHelper.get_values(r_all, index=index)
        logging.debug(f"{g_}:{type(g_)}")
        l_ = [str(i) for i in g_]
        # l_ = list(g_)
        logging.debug(l_)
        return l_
