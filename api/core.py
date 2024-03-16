"""

"""
from utils.utils import request, com_assert


class YamlDriver:
    def __init__(self, loader, utils, data):
        self.loader = loader
        self.utils = utils
        self.data = data

    def processor(self):
        """
        数据处理
        :return:
        """
        hl = getattr(self.loader, self.data["handle"])
        if self.data.get("params", None):
            phl = getattr(self.loader, self.data["phl"])
            phl = phl(self.data["params"])
            r = {}
            for _0 in self.data["params"].keys():
                r |= getattr(phl, _0)()
            phl.db.close()
            return hl.load(self.data["payload"], **r)
        else:
            return hl.load(self.data["payload"])

    def invoker(self):
        """
        调接口
        :return:
        """
        return request(self.processor(), flag=False)

    def r_assert(self):
        """
        断言
        :return:
        """
        status_code, r_text, r_json = self.invoker()
        # com_assert(status_code, r_json)
        if self.data.get("assert", None):
            at = getattr(self.utils, self.data.get("assert"))
            ahl = getattr(self.loader, self.data["ahl"])(r_text)
            for ele in self.data["compare"]:
                # print(ele)
                if isinstance(ele[0], dict):
                    key = tuple(ele[0])[0]
                    expect = getattr(ahl, key)(**ele[0].get(key))
                else:
                    expect = ele[0]
                actual = getattr(ahl, ele[1][0])(ele[1][1])
                at(expect, actual, lambda x, y: eval(f"x {ele[2]} y"))
            ahl.db.close()


def request_and_assert(loader, utils, data):
    YamlDriver(loader, utils, data).r_assert()

