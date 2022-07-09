"""
基础对象
"""
import json
import os.path as path

from selenium import webdriver
from selenium.webdriver.common.by import By

from config.settings import BASE_DIR


def browser():
    _ = webdriver.ChromeOptions()
    # 无头模式
    # _.headless = True
    _.add_argument("--start-maximized")
    # _.add_argument('--no-sandbox --start-maximized')
    driver = webdriver.Chrome(options=_)
    driver.implicitly_wait(10)
    return driver


class BasePage:
    def __init__(self, d):
        self.driver: webdriver.Chrome = d

    def quit(self):
        input("输入任意字符退出：")
        self.driver.quit()

    def cookies_login(self):
        with open(path.join(BASE_DIR, "cookies.json"), "r") as f:
            for i in json.load(f):
                self.driver.add_cookie(i)
