#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/11 9:47
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/python_repos.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

import requests

url = 'https://api.github.com/search/repositories' + '?q=language:python+sort:stars+stars:>10000'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print(f"\n Keys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
