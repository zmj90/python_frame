import json
import re
import tomllib

s1 = """{
        "sn_lfgist": "dsf",
        "fgdf": 213,
        "fg": 56
    }
    {
    "sn_list": [
        "asd",
        "gfdg",
        "weqwr",
        "fsdaf"
    ]
}"""
# r1 = json.loads(s1)
r1 = re.findall()
print(r1, type(r1))

