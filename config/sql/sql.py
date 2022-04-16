"""

"""
__all__ = ["query_city", "query_vendors"]
query_city = "select id, district from city where `name` = %s and countrycode = %s;"
query_vendors = "select vend_id from vendors limit 3;"
