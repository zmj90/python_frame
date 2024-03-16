"""

"""
import logging

import pytest


@pytest.mark.parametrize("data", [{"id": "api_test_pytest.001", "value": 2}], ids=lambda i: i.get("id"))
def test_string_only(order, first_entry, data):
    order.append(data.get("value"))
    assert order == [first_entry, 2]


def test_string_and_int(order, first_entry):
    assert order == [first_entry]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("6*9", 42, marks=pytest.mark.xfail),
    ],
    ids=["api_test_pytest.003", "api_test_pytest.004"]
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


def f():
    raise SystemExit(1)


@pytest.mark.parametrize("_", [1], ids=["api_test_pytest.005"])
# @pytest.mark.parametrize("_", ["1"])
def test_my(_):
    with pytest.raises(SystemExit):
        f()


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)],
                ids=["api_test_pytest.006", "api_test_pytest.007", "api_test_pytest.008"])
def data_set(request):
    return request.param


def test_data(data_set):
    logging.info(data_set)


@pytest.mark.parametrize("a, b", [{"1a": 2, "3b": 4}])
def test_params(a, b):
    logging.info(a)
    logging.info(b)
