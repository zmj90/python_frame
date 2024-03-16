"""
公共配置
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
URL_HOME = "https://www.douban.com"
USERNAME, PASSWORD = None, None
LOGIN = None
PRODUCT_LINE = "045969"

DB = [
    {
        "host": "192.168.1.163",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "test",
        "charset": "utf8"
    },
    {
        "host": "192.168.1.163",
        "port": 3307,
        "user": "root",
        "password": "123456",
        "database": "test",
        "charset": "utf8"
    }
]

DOMAIN = {
    "domain": "http://192.168.1.163:8090"
}

HEADERS = {
    "user_id": "45969",
    "user_agent": "chrome"
}

VBS_DOMAIN = "4bb599b0-96a0-4c6d-82b5-64e52ed89e7a"
EXPECT = {}


if __name__ == '__main__':
    print(BASE_DIR)
    # D:\doing\study\demo\python_frame
