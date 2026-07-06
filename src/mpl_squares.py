#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/06 21:03
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/mpl_squares.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.


import matplotlib.pyplot as plt

print(plt.style.available)

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# fig 表示由生成的一系列绘图构成的整个图形。
# ax 表示图形中的绘图，在大多数情况下，使用这个变量来定义和定制绘图。

# 应用 matplotlib 的内置样式
# plt.style.use('seaborn-v0_8')
plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()

# linewidth 决定了 plot() 绘制的线条的粗细
ax.plot(input_values, squares, linewidth=3)

# 设置图题并给坐标轴加上标签
# set_title 指定图表的标题
ax.set_title('Square numbers', fontsize=23)

# 为 x 和 y 轴设置标题
ax.set_xlabel('Value', fontsize=18)
ax.set_ylabel('Square of nums', fontsize=18)

# tick_params() 方法设置刻度标记的样式，它在这里将两条轴上的刻度标记的字号都设置为 10
ax.tick_params(labelsize=10)

plt.show()
