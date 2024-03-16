"""
解析ini/toml

"""
import os
import configparser
import logging

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "common.ini"), encoding="utf8")

# applicable.scope
tech_plan_project = config["applicable.scope"]["tech_plan_project"]

try:
    import special
    import tomllib


    def parse(file):
        with open(file, "rb") as f1:
            return tomllib.load(f1)


    config_tom_file = os.path.join(os.path.dirname(__file__), "config.toml")
    config_tom = parse(config_tom_file)
except ModuleNotFoundError as e:
    logging.warning(e)
