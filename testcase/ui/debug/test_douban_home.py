"""
登录豆瓣
"""
import logging

import pytest

from data.ui.debug import dou_ban_book
from ui.core import perform_excel
from utils.utils import sleep


class TestHome:
    @pytest.mark.parametrize("data", dou_ban_book, ids=lambda i: i.get("id"))
    def test_click_book(self, key_no_sign, data):
        perform_excel(key_no_sign, data)
        sleep(1)

    def test_baidu(self, key_no_sign):
        key_no_sign.get("https://www.baidu.com/")
        # key_no_sign.input_text("id", "kw", "python标准库")
        res = key_no_sign.expect_ele_visibility("id", "kw1")
        logging.info(res)
