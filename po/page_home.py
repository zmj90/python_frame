"""
豆瓣登录
"""
import json
import os.path as path

from selenium.webdriver.common.by import By

from base.base_page import BasePage, browser
from support.home_value import PV
from config.settings import BASE_DIR


class PageLogin(BasePage):
    def login_(self):
        # Loads a web page
        self.driver.get(PV.URL_HOME)
        # 切换frame
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, PV.FRAME_NODE))
        self.driver.find_element(By.CSS_SELECTOR, PV.PW_LOGIN_NODE).click()

        input("手动输入用户名和密码登录后，输入任意字符保存cookies信息>")
        self._save_cookies()

    def _save_cookies(self):
        with open(path.join(BASE_DIR, "cookies.json"), "w") as f:
            json.dump(self.driver.get_cookies(), f)

    def login(self):
        # Loads a web page
        self.driver.get(PV.URL_HOME)
        # 免密登录
        self.cookies_login()
        # 刷新页面
        self.driver.refresh()


if __name__ == '__main__':
    driver = browser()
    pl = PageLogin(driver)
    # pl.login_()
    pl.login()
    pl.quit()
