import json

post_test = {
    "title": None,
    "content": None,
    "city": [
        {
            "name": None,
            "area": None
        },
        {
            "test": None,
            "lang": None
        }
    ]
}

s = json.dumps(post_test, indent=4)
print(s)