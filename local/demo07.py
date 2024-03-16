import time
from datetime import datetime


def f1(s):
    return time.mktime(time.strptime(s, "%Y/%m/%d"))


def f2(s):
    t = datetime.strptime("2023/12/15", "%Y/%m/%d")
    if datetime.strptime(s, "%Y/%m/%d") > t:
        return "大于"
    elif datetime.strptime(s, "%Y/%m/%d") == t:
        return "等于"
    return "小于"


if __name__ == '__main__':
    print(f1("2023/12/14"), type(f1("2023/12/14")))
    print(f1("2023/12/16") == f1("2023/12/16"))

    print(f2("2023/12/14"), type(f2("2023/12/14")))
    print(f2("2023/12/15"))
    print(f2("2023/12/16"))
