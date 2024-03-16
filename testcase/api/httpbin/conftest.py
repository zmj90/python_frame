"""

"""
import logging

import pytest

from common.config.settings import DOMAIN, HEADERS
from utils.utils import singleton, YamlHelper
from data.api.yaml_data import operation, operation_case


@pytest.fixture(autouse=True)
def com_down():
    logging.info(f"测试开始")
    yield
    logging.info(f"测试结束\n")


@pytest.fixture(scope="class")
def first_entry():
    return "a"


@pytest.fixture(scope="class")
def order(first_entry):
    return []


@pytest.fixture(scope="class", autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


@pytest.fixture(scope="module")
# @singleton
def get_big_id_and_contest_id():
    logging.debug("big and contest")
    return 2022, [{"id": 1001}, {"id": 1002}, {"id": 1003}]


@pytest.fixture(params=operation_case, ids=lambda i: i.get("case_id"))
def operation_fixture(request, get_big_id_and_contest_id):
    logging.debug(request.param)
    big_id_d = get_big_id_and_contest_id[1][request.param.get("no")]
    payload = YamlHelper.yaml_load(
        operation,
        **DOMAIN,
        **HEADERS,
        contest_id=request.param.get("contest_id", None) or get_big_id_and_contest_id[0],
        **big_id_d
    )
    expect = request.param.get("expect")
    yield payload, expect
    # 恢复数据
    if request.param.get("reset", 0) == 1:
        logging.debug("数据恢复正常")


def temp_handle(p):
    if p.get("xfail", None):
        return pytest.param(p, marks=pytest.mark.xfail)
    return p


# @pytest.fixture(params=list(map(temp_handle, operation_case)), ids=lambda i: i.get("case_id"))
# def operation_fixture(request, get_big_id_and_contest_id):
#     logging.debug(request.param)
#     big_id_d = get_big_id_and_contest_id[1][request.param.get("no")]
#     payload = YamlHelper.yaml_load(
#         operation,
#         **settings.DOMAIN[0],
#         **settings.HEADERS,
#         contest_id=request.param.get("contest_id", None) or random.choice(get_big_id_and_contest_id[0]),
#         **big_id_d
#     )
#     expect = request.param.get("expect")
#
#     yield payload, expect
#
#     # 恢复数据
#     du = DataUnit()
#     if request.param.get("reset", 0) == 1:
#         du.db.execute(revert_innovation_contest_id.format(big_id_d.get("id")))
#     elif request.param.get("reset", 0) in (2, 3):
#         du.db.execute(revert_innovation_contest_id_null.format(big_id_d.get("id")))
#     if request.param.get("reset", 0) == 2:
#         du.db.execute(revert_idea_innovation_contest_id.format(big_id_d.get("id")))
#     du.db.close()
