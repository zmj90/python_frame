"""
数据驱动
"""
import logging

from ui.yam import YamlHandler, Key
from utils.utils import Compare


class YamlDriver:
    def __init__(self, yam_data) -> None:
        self.yam_data = yam_data
        self.yhl = YamlHandler()

    def processor(self):
        """
        数据处理
        :return:
        """
        if self.yam_data.get("handle", None):
            r = {}
            for _ in self.yam_data["handle"]:
                if _.get("param", None):
                    r |= getattr(self.yhl, _["method"])(*_["param"])
                else:
                    r |= getattr(self.yhl, _["method"])()
            return self.yhl.load(self.yam_data["actions"], **r)
        else:
            return self.yhl.load(self.yam_data["actions"])


def perform(key, yam_data):
    yd = YamlDriver(yam_data)
    for ele in yd.processor():
        if ele.get("param"):
            r = getattr(key, ele["action"])(**ele["param"])
        else:
            r = getattr(key, ele["action"])()
        if ele.get("log"):
            logging.info(ele.get("log"))
        if r:
            assert getattr(Compare, ele["symbol"])(ele["expect"], r), r


def perform_excel(key: Key, data: dict) -> None:
    logging.info(f'用例名称：{data.get("name")}')
    logging.info(f'用例编号：{data.get("id")}')
    for ele in data.get("actions"):
        if ele.get("log"):
            logging.info(ele.get("log"))
        if ele.get("param"):
            r = getattr(key, ele["action"])(**ele["param"])
        else:
            r = getattr(key, ele["action"])()
        if r:
            assert ele["expect"] in r, logging.error(f"实际结果：[{r}], 与预期结果：[{ele['expect']}]不匹配") or \
                f"实际结果：[{r}]，与预期结果：[{ele['expect']}]不匹配"
