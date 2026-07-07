#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/07 21:50
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/rw_visual.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from matplotlib import pyplot as plt

from random_walk import RandomWalk

# 创造数据
rw = RandomWalk(50_000)
rw.fill_walk()

# =========================================================================================
# 如果知道当前系统的分辨率，可通过参数 dpi 向 plt.subplots() 传递该分辨率
fig, ax = plt.subplots(figsize=(15, 9), dpi=100)  # <--- 看这里 figsize 指示屏幕尺寸，单位为英寸

point_numbers = range(rw.num_points)

# ax.plot(rw.values_x, rw.values_y, linewidth=2, color='black')
# edgecolors='none' 以删除每个点的轮廓
ax.scatter(rw.values_x, rw.values_y, c=point_numbers, s=1, cmap=plt.cm.Blues, edgecolors='none')

# 默认情况下，Matplotlib 独立地缩放每个轴，而这将水平或垂直拉伸绘图
# 而 set_aspect('equal') 指定两条轴上刻度的间距必须相等
ax.set_aspect('equal')

# # 突出起点和终点
# ax.scatter(rw.values_x[0], rw.values_y[0], c='black', s=100, edgecolors='none')
# ax.scatter(rw.values_x[-1], rw.values_y[-1], c='red', s=100, edgecolors='none')

# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
