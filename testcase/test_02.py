import logging

import pytest


@pytest.mark.skip
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("3+5", 8),
        pytest.param("6*9", 42, marks=pytest.mark.xfail),
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


def f():
    raise SystemExit(1)


@pytest.mark.skip
def test_my():
    with pytest.raises(SystemExit):
        f()


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


@pytest.mark.skip
def test_data(data_set):
    logging.info(data_set)
