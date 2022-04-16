import re

import pytest
import requests
from requests import session
import yaml
import logging

from ddt import con_control
from config.pattern import pattern_vend_id

rs = session()


# @pytest.mark.skip("不想执行")
@pytest.mark.parametrize("payload,expect", con_control.Vendors().load())
def test_get_vendors(payload, expect):
    # 查询有哪些供应商
    logging.info(f"输入数据:{payload};预期结果:{expect}")
    res = requests.request(**payload)
    text = res.text
    logging.debug(f"text：{text}")
    # _ = re.findall(pattern_vend_id, text)
    _ = re.findall(r'\"vend_id\": (\d+)', text)
    logging.info(f"{_}:{type(_)}")
    # content = res.content
    # logging.debug(f"content：{content}")
    res = res.json()
    logging.info(f"响应数据：{res}")
    print(f"{__name__=}")
    # 方式一：
    # try:
    #     assert expect["url"] in res["url"]
    # except Exception as e:
    #     logging.exception(e)
    #     logging.debug(type(e))
    #     raise e
    # 方式二：
    assert expect["url"] in res["url"], \
        logging.error(f"实际结果：{res['url']}, 没有包含预期结果：{expect['url']}") \
        or f"assert '{expect['url']}' in '{res['url']}'"
    assert expect["ids"] == _, \
        logging.error(f"实际结果：{_}, 不等于预期结果：{expect['ids']}") \
        or f"assert '{expect['ids']}' in '{_}'"


@pytest.mark.skip("不想执行")
@pytest.mark.parametrize("payload,expect", con_control.GetDate().load())
def test_get_method(payload, expect):
    logging.info(f"输入数据:{payload};预期结果:{expect}")
    res = requests.request(**payload)
    # logging.debug(res.text)
    # logging.debug(res.content)
    res = res.json()
    logging.info(f"响应数据：{res}")
    print(f"{__name__=}")
    # 方式一：
    # try:
    #     assert expect["url"] in res["url"]
    # except Exception as e:
    #     logging.exception(e)
    #     logging.debug(type(e))
    #     raise e
    # 方式二：
    assert expect["url"] in res["url"], \
        logging.error(f"实际结果：{res['url']}, 没有包含预期结果：{expect['url']}") \
        or f"assert '{expect['url']}' in '{res['url']}'"
