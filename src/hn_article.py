#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/11 10:23
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/hn_article.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

import requests
import json

# 执行 API 调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
# 探索数据的结构
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
