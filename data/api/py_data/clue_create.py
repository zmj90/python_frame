"""

"""
data = [
    {
        "id": "clue_001",
        "params": {"permission_set": "公开", "cover_type": 2, "save_type": 1},
        "assert": {"expect": "http://192.168.1.163:8090/post", "actual": '"url": "(.*?)"'}
    },
    {
        "id": "clue_002",
        "params": {"permission_set": "私密", "cover_type": 1, "save_type": 2},
        "assert": {"expect": "http://192.168.1.163:8090/post", "actual": '"url": "(.*?)"'}
    }
]
