import pytest
import requests
from requests import session
import yaml
import logging

import config.settings as settings
from ddt import get

rs = session()


# @pytest.mark.skip("不想执行")
@pytest.mark.parametrize("payload,expect", get.GetDate().date_get())
def test_get01(payload, expect):
    """

    :return:
    """
    logging.info(f"测试开始")
    logging.info(f"输入数据:{payload};预期结果:{expect}")
    res = requests.request(**payload).json()
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
    logging.info(f"测试结束\n")


@pytest.mark.skip
def test_post():
    """

    :return:
    """
    method = "get"
    url = "http://httpbin.org/get"
    res = rs.request(method, url)
    return res
