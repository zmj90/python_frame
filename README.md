# python_frame



-   api

    接口逻辑处理

-   common

    公共配置


-   data

    测试数据

-   lib

    库

-   local

    本地

-   log

    日志

-   plugin

    插件

-   report

    报告

-   temp

    临时文件

-   testcase

    测试用例

-   ui

    web逻辑处理

-   utils

    工具

    ​


# yaml_file

```yaml
-
  id: 用例编号
  payload:
    method: get
    url: url
    params:
      key: $value
    headers:
      user-id: "${user_id}"
      user-agent: $user_agent
    data:
      - {id: 1, name: python}
  handle: YamlPayLoader  # 请求类
  phl: YamlParamHandler  # 请求参数处理类
  params:
    sql:  # 方法
      - [query_city, ["Kabul", "AFG"]]  # [sql, params]
    text: # 方法
      - [word, value]  # [方法, $value]
    sql_one: # 方法
      - [name, [query_name_district]]  # [$name, [sql, params]]
  assert: data_assert  # 断言方法
  ahl: AssertHandler  # 断言处理类
  compare:
  	# [{方法: 字典参数}, [方法, 正则表达式], 比较符]
    - [{query_ids: { sql_p: query_vendors, key: vend_id }}, [ re_parses, '"vend_id": (\d+)' ], "==" ]
    # [{方法: {key: [$district, [sql, params]]}}, [方法, 正则表达式], 比较符]
    - [{sql_one: { l_param: [ district, [ query_name_district ] ] }}, [ re_parse, '"district": "(.*?)"' ], == ]
    # [参数, [方法, 正则表达式], 比较符]
    - [ http://192.168.1.163:8090/post, [ re_parse, '"url": "(.*?)"' ], in ]
    - [ "172.17.0.1", [ re_parse, '"origin": "(.*?)"' ], == ]
```



```python
necessity

special.py

zwx996578.pth
	# /opt/zwx996578_pack
	D:\doing\zwx996578_pack
        
Python311\Lib\necessity

Python311\Lib\site-packages\special.py

Python311\Lib\site-packages\zwx996578.pth

Python311\zwx996578_pack


python3 -V
echo $runParam
pytest test_case/tech_inno/api/test_IdeaManageService || true
python3 driver/tech_inno/back_cloudtest.py $runParam

```



## 隐私

```python
# 敏感信息放入数据库 or 服务器
```



```
框架设计:逻辑层、设计层、数据层
目录
data
info
resources
bin
etc
usr
dev
conf
lib
help
plugins
doc
drivers
logs
tools
temp
share
bll

```

