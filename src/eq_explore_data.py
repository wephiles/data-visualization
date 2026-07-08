#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/08 20:52
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/eq_explore_data.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from pathlib import Path
import json

import pandas as pd
import plotly.express as px

# 将数据作为字符串读取并反序列化为 Python 对象
path = Path(__file__).parent.parent / 'eq_data' / 'eq_data_30_day_m1.geojson'

try:
    contents = path.read_text()
except Exception as _:
    contents = path.read_text(encoding='utf-8')

all_data = json.loads(contents)

# 查看数据集中的所有地震
all_eq_dicts = all_data['features']

# 提取震级等数据
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(zip(lons, lats, titles, mags, ), columns=['经度', '纬度', '位置', '震级'])

# 绘制地震散点图
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)

fig.write_html('../global_eq_scatter.html')
fig.show()
