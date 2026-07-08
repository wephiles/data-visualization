#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/08 20:34
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/valley_highs_lows.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.


import csv
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

path = Path(__file__).parent.parent / 'weather_data' / 'death_valley_2021_simple.csv'
lines = path.read_text().splitlines()

reader = csv.reader(lines)
head_row = next(reader)

# 提取最高温度
highs = []
dates = []
lows = []

for row in reader:
    try:
        high = int(row[3])
        date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[4])
    except ValueError:
        print(f'当前行缺少数据: {row}')
    else:
        lows.append(low)
        dates.append(date)
        highs.append(high)

# 根据最高温绘图
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# 设置绘图格式
ax.set_title("2018 年每日最高气温", fontsize=18)

# fig.autofmt_xdate() 来绘制倾斜的日期标签，以免它们彼此重叠
ax.set_xlabel('日 期', fontsize=14)
fig.autofmt_xdate()

ax.set_ylabel("温度 (华氏摄氏度)", fontsize=14)
ax.tick_params(labelsize=14)  # 设置刻度线

plt.show()
