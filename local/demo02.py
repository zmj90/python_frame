# l1 = [1, 2, 3]
# print(l1.pop())
# print(l1)
# d = {"1a": 2, "3b": 4}
# print(list(d))
g1 = map(lambda i: i + 1, [1, 2, 3])
print(type(g1), g1)
# r1 = tuple(g1)
r1 = list(g1)
print(type(r1), r1)
s1 = {[1, 2, 3], 123}
print(s1, type(s1))
import string
