"""

"""
from common.config.settings import DOMAIN, HEADERS
from utils.utils import DTHelper


class ClueQueryPayload:
    def __init__(self, *args, **kwargs):
        self.method = "post"
        self.url = f'{DOMAIN["domain"]}/post'
        self.headers = HEADERS
        self.json = vars(ClueQueryJson(*args, **kwargs))


class ClueQueryJson:
    def __init__(self,
                 f_key="", status="", domain_id="all", pro_level="1,2", days=None, page=1,
                 size=12, tor_order="desc", tor_param="createTime"):
        """
        payload
        :param f_key: str: "关键字" or "描述"
        :param status: str: ENUM_WAIT_SUBMIT,ENUM_WAIT_REVIEW,ENUM_PUBLISHED,ENUM_SOLVING,
        ENUM_WAIT_CLOSE_AUDIT,ENUM_CLOSE
        :param domain_id: str: "all" or "4bb599b0-96a0-4c6d-82b5-64e52ed89e7a,85554a00-5003-425e-b152-4513a623acda"
        :param pro_level: str: "1,2"
        :param days: int
        :param page: int
        :param size: int
        :param tor_order: str: "desc" or "asc"
        :param tor_param: str: "card" or "list"
        """
        self.filter = f_key
        self.filterCondition = {
            "type": 2,
            "status": status,
            "domainId": domain_id,
            "proLevel": pro_level,
            "createTime": DTHelper.get_time_interval(days=days) if days is not None else ""
        }
        self.page = page
        self.size = size
        self.torOrder = tor_order
        self.torParam = tor_param


if __name__ == '__main__':
    ...
