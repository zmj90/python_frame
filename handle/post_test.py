import json
import random

import requests


class PostTest:
    def __init__(self, title, id, key, user="wx996578", pro="045969"):
        self.title = title
        self.url = "http://httpbin.org/post"
        self.id = id
        self.key = key
        self.user = user
        self.pro = pro

    def __params(self):
        return {"id": self.id, "key": self.key}

    def __header(self):
        return {"user": self.user, "pro": self.pro}

    def __body(self):
        return {
            "title": None,
            "content": None,
            "city": [
                {
                    "name": None,
                    "area": None
                },
                {
                    "test": None,
                    "lang": None
                }
            ]
        }

    def api(self):
        return self.url, self.__params(), self.__header(), self.__body()


p = PostTest("qwe", 1, "ads")
print(p.api())
# r = requests.post("http://httpbin.org/post", params=params, json=post_test)
# print(r.text)
