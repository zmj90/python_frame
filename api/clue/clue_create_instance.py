"""

"""
import random

from common.config.settings import VBS_DOMAIN, DOMAIN, HEADERS
from common.config.enum import clue_type, source
from utils.utils import fake


class ClueCreatePayload:
    def __init__(self, *args, **kwargs):
        self.method = "post"
        self.url = f'{DOMAIN["domain"]}/post'
        self.headers = HEADERS
        self.json = vars(ClueCreateJson(*args, **kwargs))


class ClueCreateJson:
    def __init__(self,
                 permission_set, file_id=None, file_name="", cover_type=5, save_type=1):
        fake_cn = fake()
        self.title = fake_cn.country() + fake_cn.uuid4()
        self.domainId = VBS_DOMAIN
        if file_id:
            self.fileId = file_id
            self.fileName = file_name
        self.description = f"<div>{fake_cn.text()}</div>"
        self.permissionSet = permission_set  # "公开" or "秘密"
        self.clueType = random.choice(clue_type)
        self.source = random.choice(source)
        self.coverType = cover_type
        self.saveType = save_type


if __name__ == '__main__':
    print(vars(ClueCreatePayload(permission_set="公开")))
