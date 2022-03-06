import random
import time
from concurrent.futures import ThreadPoolExecutor


def get(k):
    time.sleep(2)
    print(f"{k}{time.time()}")
    return k


def save(res):
    print(res)


d1 = {
    "n1": "qwe1",
    "n2": "qwe2",
    "n3": "qwe3",
    "n4": "qwe4",
    "n5": "qwe5",
    "n6": "qwe6",
}

# pool = ThreadPoolExecutor(3)
# for key, value in d1.items():
#     future = pool.submit(get, key)
#     future.add_done_callback(save)


