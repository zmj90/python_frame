import requests
from requests.sessions import session

s = session()


def test01():
    res = s.request("get", "https://httpbin.org/get", headers={"flag": "123"})

    print(res.request.headers)


def test02():
    res = s.request("get", "https://httpbin.org/get")

    print(res.request.headers)
