"""
- id: douban_home_001
  handle:
    - method: unique
  actions:
    - action: get
      param:
        url: "https://www.douban.com/"
      log:
    - action: click_blank
      param:
        by: "link text"
        value: "豆瓣读书"
      log:
    - action: title
      expect: "豆瓣读书"
      log:
"""
import logging

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common import TimeoutException

from ui.base import BasePage
from utils.utils import fake, YamlHelper
from res.ui import file_path


class Key(BasePage):
    window_handles = None

    def get(self, url) -> None:
        """
        进入页面
        :Usage:
            ::
                get("https://python.org")
        :param url: 访问地址
        :return: None
        """
        self.driver.get(url)

    def find_element(self, by, value=None) -> WebElement:
        """
        将定位元素红框显示
        :param by: 定位方法
        :param value: 定位表达式
        :return: WebElement
        """
        ele = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((by, value)))
        self.driver.execute_script("arguments[0].style.border='2px solid red';", ele)
        return ele

    def click(self, by, value) -> None:
        """
        单击
        :param by: 定位方法
        :param value: 定位表达式
        :return: None
        """
        self.find_element(by, value).click()

    def _switch_to_window(self) -> None:
        """
        切换
        :return: None
        """
        _ = self.driver.window_handles
        self.driver.switch_to.window(_[-1])

    def click_blank(self, by, value) -> None:
        """
        点击并新开
        :param by: 定位方法
        :param value: 定位表达式
        :return: None
        """
        self.click(by, value)
        self._switch_to_window()

    def clicks(self, by, value) -> None:
        """
        点击多个
        :param by: 定位方法
        :param value: 定位表达式
        :return: None
        """
        for ele in self.driver.find_elements(by, value):
            self.driver.execute_script("arguments[0].style.border='2px solid red';", ele)
            ele.click()

    def move_click(self, by, value, x: int, y: int) -> None:
        """
        定位点击
        :param by: 定位方法
        :param value: 定位表达式
        :param x: 偏移量
        :param y: 偏移量
        :return: None
        """
        ele = self.find_element(by, value)
        ActionChains(self.driver).move_to_element_with_offset(ele, x, y).click().perform()

    def wait_be_click(self, by, value):
        """
        等待元素可用并点击
        :param by:
        :param value:
        :return:
        """
        # 适用ELEMENT_NOT_INTERACTABLE = [60, 'element not interactable']
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((by, value))).click()

    def relative_click(self, by, using, method, element_or_locator):
        """
        通过相对定位点击
        :param by: 传入By的值
        :param using: 用于查找元素的搜索词
        :param method: 相对方法
        :param element_or_locator: 依赖元素
        :return:
        """
        if isinstance(element_or_locator, (WebElement, dict)):
            ele = element_or_locator
        else:
            ele = self.find_element(*element_or_locator)
        self.find_element(getattr(locate_with(by, using), method)(ele)).click()

    def input_text(self, by, value, text):
        """
        输入
        :param by:
        :param value:
        :param text:
        :return:
        """
        # self.driver.find_element(by, value).send_keys(text)
        webdriver.ActionChains(self.driver).send_keys_to_element(self.find_element(by, value), text).perform()

    def u_editor(self, frame_ref, by, value, text):
        """
        富文本输入
        :param frame_ref:
        :param by:
        :param value:
        :param text:
        :return:
        """
        self.driver.switch_to.frame(frame_ref)
        self.input_text(by, value, text)
        self.driver.switch_to.default_content()

    def send_keys(self, by, value, key, flag=False):
        """
        发送
        :param by:
        :param value:
        :param key:
        :param flag:
        :return:
        """
        if isinstance(key, (tuple, list)):
            key = file_path(key[0])
        if flag:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((by, value))).send_keys(key)
        else:
            self.find_element(by, value).send_keys(key)

    def scroll_to_element(self, by, value):
        """
        If the element is outside the viewport, scrolls the bottom of the element to the bottom of the viewport.
        :param by:
        :param value:
        :return:
        """
        ActionChains(self.driver).scroll_to_element(self.find_element(by, value)).perform()

    def execute_script(self, script, args=None):
        """
        执行js

        :Usage:
            ::
            args = (By.XPATH, "//h3[text()='为你推荐']")
            将该模块与浏览器顶部对齐
            driver.execute_script('arguments[0].scrollIntoView();', args)
            将该模块与浏览器底部对齐
            driver.execute_script('arguments[0].scrollIntoView(false);', args)

        :param script:
        :param args:
        :return:
        """
        if args:
            self.driver.execute_script(script, self.find_element(*args))
        else:
            self.driver.execute_script(script)

    def current_url(self):
        """
        获取当前页面url
        :return:
        """
        return self.driver.current_url

    def title(self):
        """
        获取title
        :return:
        """
        return self.driver.title

    def text(self, by, value):
        """
        获取文本
        :param by:
        :param value:
        :return:
        """
        return self.find_element(by, value).text

    def close(self):
        """
        关闭
        :return:
        """
        self.driver.close()
        self._switch_to_window()

    def expect_ele_visibility(self, by, value, timeout=5) -> bool:
        """
        within timeout, element visibility return True; element invisibility return False
        """
        try:
            if WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((by, value))):
                return True
        except TimeoutException:
            return False

    def wait_ele_invisible(self, by, value) -> None:
        """
        等待元素不可见
        """
        try:
            WebDriverWait(self.driver, 6).until_not(ec.visibility_of_element_located((by, value)))
        except TimeoutException as e:
            logging.error(e)


class YamlHandler:
    def __init__(self):
        self.fake = fake()

    @staticmethod
    def load(reader, **kwargs):
        return YamlHelper.yaml_load(reader, **kwargs)

    def unique(self):
        return {"unique": self.fake.country() + self.fake.uuid4()}


if __name__ == '__main__':
    fake = fake()
    print(fake.uuid1())
