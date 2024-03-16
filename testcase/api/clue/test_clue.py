"""

"""
import pytest
import requests

from data.api.py_data.clue_create import data as create_data
from data.api.py_data.clue_query import data as query_data
from api.clue.clue_create_instance import ClueCreatePayload
from api.clue.clue_query_instance import ClueQueryPayload
from api.py import AssertHandler
from utils.utils import request, data_assert


class TestClue:
    @pytest.mark.parametrize("p", create_data, ids=lambda i: i.get("id"))
    def test_clue_create(self, p):
        payload = vars(ClueCreatePayload(**p["params"]))
        status_code, r_text, r_json = request(payload, flag=False)
        ahl = AssertHandler(r_text)
        assert status_code == 200
        data_assert(p["assert"]["expect"], ahl.re_parse(p["assert"]["actual"]), lambda a, b: a == b)

    @pytest.mark.parametrize("p", query_data, ids=lambda i: i.get("id"))
    def test_clue_query(self, p):
        payload = vars(ClueQueryPayload(**p["params"]))
        status_code, r_json = request(payload)
        assert status_code == 200
