#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/08 19:01
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/dice_visual.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

import plotly.express as px
from plotly.graph_objs.layout.scene import xaxis

from dice import Dice

dice = Dice()
dice_1 = Dice()

# 掷几次骰子并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = dice.roll() + dice_1.roll()
    results.append(result)

frequencies = []
max_result = dice.num_sides + dice_1.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = '掷 1000 次两枚骰子的结果'
labels = {'x': '点数', 'y': '出现次数'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# xaxis_dtick 指定 x 轴上刻度标记的间距
fig.update_layout(xaxis_dtick=1)
fig.show()
