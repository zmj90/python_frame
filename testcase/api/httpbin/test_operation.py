"""

"""
from utils.utils import request, data_assert


def test_operation(operation_fixture):
    code, json_ = request(operation_fixture[0])
    data_assert(operation_fixture[1].get("status"), code, lambda a, b: a == b)
