class C:
    def __init__(self):
        self._x = "123"

    @property
    def x(self):
        """I'm the 'x' property."""
        print("get")
        return self._x

    # @x.setter
    # def x(self, value):
    #     print("call setter方法")
    #     self._x = value

    @x.setter
    def x(self, _):
        print("call setter方法")
        _ = f"装饰{_}"
        self._x = _

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    c = C()
    r1 = c.x
    print(r1)
    c.x = "qwe"
    r2 = c.x
    print(r2)

