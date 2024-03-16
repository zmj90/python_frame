from common.config import config_tom
from common.config.settings import PRODUCT_LINE
from utils.utils import MongoDB


class TechDomainConfigRef(MongoDB):
    def __init__(self,
                 url=config_tom["url"]["gamma86.url"],
                 data_base=config_tom["gamma86.url.db"]["idea_tech_plan_compute"]):
        super().__init__(url, data_base)

    def get_index_no(self):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["tech_domain_config"])
        d = col.find_one({"parentId": None}, projection={"_id": 0, "indexNo": 1}, sort=[("indexNo", -1)])
        return d["indexNo"] + 1

    def latest_tech_domain_sub(self):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["tech_domain_config"])
        return col.find_one({"parentId": {"$ne": None}}, sort=[("_id", -1)])

    def delete_root_tech(self, name):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["root_tech"])
        col.delete_many({"rootTechNumber": {"$in": name}})

    def get_index_no(self):
        col = self.col(config_tom["idea_config_gama.col"]["institute"])
        d = col.find_one({"productLine": PRODUCT_LINE}, {'_id': 0, 'indexNo': 1}, sort=[("indexNo", -1)])
        return d["indexNo"] + 1

    def all_institute(self):
        col = self.col(config_tom["idea_config_gama.col"]["institute"])
        r_list = col.find({"productLine": PRODUCT_LINE}, {'_id': 1, 'indexNo': 1})
        r_target = []
        for i in r_list:
            i["id"] = str(i["_id"])
            del i["_id"]
            r_target.append(i)
        return r_target

    def get_root_tech(self):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["root_tech"])
        _ = col.find_one(projection={"_id": 1, "rootTechNumber": 1, "rootTechName": 1, "createTime": 1},
                         sort=[("_id", -1)])
        _["_id"] = str(_["_id"])
        return _

    def get_domain_id_and_name(self):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["tech_domain_config"])
        _ = col.find_one({"productLineCode": PRODUCT_LINE, "techDomainApplicableScope": {"$regex": "ROOT_TECH"},
                          "parentId": None}, {"_id": 1, "techDomain": 1}, sort=[("indexNo", 1)])
        _["_id"] = str(_["_id"])
        return _

    def get_not_exist_competence_center_name_of_id(self):
        col = self.col(config_tom["idea_tech_plan_compute.col"]["competence_center"])
        _ = col.find_one({"productLine": PRODUCT_LINE, "competenceCenterName": {"$exists": False},
                          "domainId": self.get_domain_id_and_name()["_id"]}, {"_id": 1})
        _["_id"] = str(_["_id"])
        return _
