import yaml


# class Hero:
#     def __init__(self, name, hp, sp):
#         self.name = name
#         self.hp = hp
#         self.sp = sp
#
#     def __repr__(self):
#         return "%s(name=%r, hp=%r, sp=%r)" % (
#             self.__class__.__name__, self.name, self.hp, self.sp)
#
#
# a = yaml.load("""
# !!python/object:__main__.Hero
#     name: Welthyr Syxgon
#     hp: 1200
#     sp: 0
# """, Loader=yaml.CLoader)
# print(a)
from string import Template
with open("qwe.yaml", "r") as f:
    # a = yaml.safe_load(f)
    # print(a, type(a))
    a = f.read()
    # print(b, type(b))
s = Template(a)
# s = Template('$name likes $what')
# print(s)
d = {"name": "python"}
s1 = s.safe_substitute(d)
print(s1, type(s1))
d1 = yaml.safe_load(s1)
print(d1,  type(d1))
