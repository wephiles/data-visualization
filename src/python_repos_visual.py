#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/11 9:58
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/python_repos_visual.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories' + '?q=language:python+sort:stars+stars:>10000'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
response_dict = r.json()

print(f"Status code: {r.status_code}")
# 处理有关仓库的信息
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
repo_links = []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
# 可视化
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.show()
