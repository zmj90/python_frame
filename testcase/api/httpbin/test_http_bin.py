"""

"""
import pytest

import api
from data.api.yaml_data import http_bin_01, http_bin_02, http_bin_03
from utils import utils
from api.core import request_and_assert


class TestHttpBin:
    @pytest.mark.parametrize("data", http_bin_01, ids=lambda i: i.get("id"))
    def test_api_demo1(self, data):
        request_and_assert(api, utils, data)

    @pytest.mark.parametrize("data", http_bin_02, ids=lambda i: i.get("id"))
    def test_api_demo2(self, data):
        request_and_assert(api, utils, data)

    @pytest.mark.parametrize("data", http_bin_03, ids=lambda i: i.get("id"))
    def test_api_demo3(self, data):
        request_and_assert(api, utils, data)
