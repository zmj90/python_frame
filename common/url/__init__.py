#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

idea_manage_tom_file = os.path.join(os.path.dirname(__file__), "idea_manage_service.toml")
common_idea_tech_plan_service = os.path.join(os.path.dirname(__file__), "common_idea_tech_plan_service.toml")

try:
    import special
    import tomllib


    def parse(file):
        with open(file, "rb") as f1:
            return tomllib.load(f1)


    url_path = parse(idea_manage_tom_file) | parse(common_idea_tech_plan_service)
except ModuleNotFoundError as e:
    logging.warning(e)


if __name__ == '__main__':
    ...
