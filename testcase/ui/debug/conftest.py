"""
123
"""
import pytest

from ui.base import browser
from ui.yam import Key
from utils.utils import sleep


@pytest.fixture(scope="package")
def key():
    _ = Key(browser())
    yield _
    # sleep(5)
    _.quit()
