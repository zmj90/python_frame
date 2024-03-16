"""
基础对象
"""
import json
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common.config.settings import BASE_DIR
from utils.utils import singleton


class Url:
    url_home = "https://www.douban.com/"


class Node:
    # frame_node = '//div[@class="login"]/iframe'  # xpath
    frame_node = '.login>iframe'  # css
    # pw_login_node = '//li[text()="密码登录"]'  # xpath
    pw_login_node = '.account-tab-account'  # css

    book_link_node = "豆瓣读书"


class Expect:
    title_expect = "豆瓣"

    book_title_expect = "豆瓣读书"


url, node, expect = Url, Node, Expect


# @singleton
def browser() -> WebDriver:
    _ = webdriver.ChromeOptions()
    _.add_argument("--start-maximized")  # 窗口最大化
    if sys.platform == "linux":
        _.add_argument("--headless")  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        _.add_argument("--no-sandbox")  # 解决DevToolsActivePort文件不存在的报错,以最高权限运行
        _.add_argument("--disable-gpu")  # 谷歌文档提到需要加上这个属性来规避bug
        _.add_argument("--disable-dev-shm-usage")  # The /dev/shm partition is too small in certain
        # VM environments, causing Chrome to fail or crash (see http://crbug.com/715363).
        # Use this flag to work-around this issue (a temporary directory will always be used to
        # create anonymous shared memory files).
    driver = webdriver.Chrome(options=_)
    driver.implicitly_wait(10)
    return driver


class BasePage:
    def __init__(self, d) -> None:
        self.driver: webdriver.Chrome = d

    def save_cookies(self) -> None:
        self.driver.get(url.url_home)
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, node.frame_node))
        self.driver.find_element(By.CSS_SELECTOR, node.pw_login_node).click()
        input("手动输入用户名和密码登录后，输入任意字符保存cookies信息>")
        with open(os.path.join(BASE_DIR, "local", "cookies.json"), "w") as f:
            json.dump(self.driver.get_cookies(), f)
        self.quit()

    def login_cookies(self) -> None:
        self.driver.get(url.url_home)
        with open(os.path.join(BASE_DIR, "local", "cookies.json"), "r") as f:
            for i in json.load(f):
                self.driver.add_cookie(i)

    def quit(self) -> None:
        input("输入任意字符退出：")
        self.driver.quit()


if __name__ == '__main__':
    BasePage(browser()).save_cookies()
