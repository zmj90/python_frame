import os
import sys

import pytest

if __name__ == '__main__':
    r = pytest.main()
    # print(r)
    os.system("allure generate ./temps -o report --clean")
    sys.exit(r)

