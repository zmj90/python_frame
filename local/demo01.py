from api.yam import RA, YamlParamHandler


class AB:
    @classmethod
    def fun1(cls):
        print("fun1")

    @staticmethod
    def fun2():
        print("fun2")

    def fun3(self):
        print("fun3")


if __name__ == '__main__':
    a = b"\u6210\u90fd".decode("unicode_escape")
    b = r"\u6210\u90fd".encode().decode("unicode_escape")
    print(a)
    print(b)
