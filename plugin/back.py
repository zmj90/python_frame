"""

"""
import os
import re
import sys

import requests
from bs4 import BeautifulSoup


class BackCloudTest:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lib", "report.html")

    def get_results(self):
        f = open(self.file_path, encoding="utf8")
        soup = BeautifulSoup(f, "lxml")
        t_body = soup("tbody")
        for node in t_body:
            td = node("td")
            # 测试结果
            result = 0 if td[0].string == "Passed" else 1
            # 测试用例
            number = re.findall(r"\[(.*?)]", td[1].string)[0]
            print(number)
            # 日志
            log = td[-1].get_text()


if __name__ == '__main__':
    b = BackCloudTest()
    b.get_results()
