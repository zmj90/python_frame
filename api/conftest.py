"""

"""
import logging

import pytest


@pytest.fixture(autouse=True)
def com_down():
    logging.info(f"测试开始")
    yield
    logging.info(f"测试结束\n")
