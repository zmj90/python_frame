"""

"""
import logging
import time
from functools import wraps

import pymysql.cursors


class DataBase:
    def __init__(self, date_base):
        self.db = pymysql.connect(**date_base)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.db.close()

    def execute(self, sql, args=None, flag=True):
        try:
            if flag:
                logging.info(self.cursor.mogrify(sql, args))
                self.cursor.execute(sql, args=args)
            else:
                for arg in args:
                    logging.info(self.cursor.mogrify(sql, arg))
                self.cursor.executemany(sql, args=args)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logging.exception(e)


db = DataBase


def consume_time(test_func):
    @wraps(test_func)
    def wrapper(*args):
        start = time.time()
        test_func(*args)
        end = time.time()
        logging.info(f"执行时间：{end-start}")
    return wrapper
