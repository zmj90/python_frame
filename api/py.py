"""

"""
import re

from api.base import DataUnit
from common.config.settings import DOMAIN, HEADERS
from common.sql import sql
from utils.utils import YamlHelper


class PyParamHandler(DataUnit):
    def __init__(self):
        super(PyParamHandler, self).__init__()


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
