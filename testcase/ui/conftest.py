"""

"""
import os
import time

import pytest
import requests
import allure
from selenium.webdriver.common.by import By
from private_mj.pdata.w3un import key as un_key, cipher as un_cipher
from private_mj.pdata.w3pw import key as pw_key, cipher as pw_cipher
from private_mj.private.crypto import de_crypt

from common.config.settings import URL_HOME, USERNAME, PASSWORD, LOGIN
from ui.base import browser
from ui.yam import Key
from utils.utils import sleep, YamlHelper

_: Key


def request_get_cookies():
    _ = os.path.dirname(__file__)
    login_yaml = os.path.join(_, "login.yaml")
    payload = YamlHelper.yaml_load(
        (login_yaml,),
        login_account=de_crypt(un_key, un_cipher),
        password=de_crypt(pw_key, pw_cipher)
    )
    res = requests.request(**payload)
    return res.cookies


@pytest.fixture(scope="session")
def key():
    global _
    _ = Key(browser())
    _.get(URL_HOME)

    # 方式1
    # _.send_keys(By.ID, USERNAME, de_crypt(un_key, un_cipher))
    # _.send_keys(By.NAME, PASSWORD, de_crypt(pw_key, pw_cipher))
    # _.click(By.NAME, LOGIN)

    # 方式2
    for ck in request_get_cookies():
        if ck.name in ("JSESSIONID", "login_huawei_com_login1_sticky"):
            continue
        _.driver.add_cookie(vars(ck))
    _.driver.refresh()

    time.sleep(5)

    yield _
    sleep(5)
    _.driver.quit()


@pytest.fixture(scope="session")
def key_no_sign():
    global _
    _ = Key(browser())
    yield _
    sleep(1)
    _.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 执行所有其他钩子以获取报表对象
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_.driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
