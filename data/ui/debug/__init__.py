import os

from utils.utils import excel_parse

_ = os.path.dirname(__file__)
dou_ban_book = excel_parse(os.path.join(_, "dou_ban_book.xlsx"))


if __name__ == '__main__':
    print(dou_ban_book)
