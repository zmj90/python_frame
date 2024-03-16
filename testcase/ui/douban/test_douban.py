"""
登录豆瓣
"""
import pytest

from data.ui.yaml_data.douban.home import home_value
from data.ui.yaml_data.douban.book import popular_book
from ui.core import perform
from utils.utils import sleep


class TestHome:
    @pytest.mark.parametrize("data", home_value, ids=lambda i: i.get("id"))
    def test_click_book(self, key_no_sign, data):
        perform(key_no_sign, data)
        sleep(5)

    @pytest.mark.parametrize("data", popular_book, ids=lambda i: i.get("id"))
    def test_click_popular_book(self, key_no_sign, data):
        perform(key_no_sign, data)
        sleep(5)

    def test_baidu(self, key_no_sign):
        key_no_sign.get("https://www.baidu.com/")
        key_no_sign.input_text("id", "kw", "python标准库")
