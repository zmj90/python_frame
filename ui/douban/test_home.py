"""
登录豆瓣
"""
import pytest

from base.base_page import browser
from po.page_home import PageLogin


class TestHome:
    driver = browser()

    def test_login(self):
        pl = PageLogin(self.driver)
        pl.login()
