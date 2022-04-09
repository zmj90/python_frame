import os.path as path

BASE_DIR = path.dirname(path.dirname(__file__))
# print(BASE_DIR)
# D:\doing\study\demo\python_frame
DB = [
    {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "test",
        "charset": "utf8"
    },
    {
        "host": "localhost",
        "port": 3307,
        "user": "root",
        "password": "123456",
        "database": "test",
        "charset": "utf8"
    }
]

domain = {
    "domain": "httpbin.org"
}

headers = {
    "user_id": "45969",
    "user_agent": "chrome"
}

