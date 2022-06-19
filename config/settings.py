import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# D:\doing\study\demo\python_frame
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

domain = {
    "domain": "192.168.1.163:8090"
}

headers = {
    "user_id": "45969",
    "user_agent": "chrome"
}

