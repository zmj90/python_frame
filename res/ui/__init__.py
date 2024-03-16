import os

_ = os.path.dirname(__file__)


def file_path(f):
    return os.path.join(_, f)
