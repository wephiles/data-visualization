#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/06 21:34
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/scatter_squares.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.


from pathlib import Path

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [i ** 2 for i in x_values]

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots()
# s 设置绘图时使用的点的尺寸
# ax.scatter(x_values, y_values, s=10, color='black')

# 还可以使用 RGB 颜色模式定制颜色。此时传递参数 color，并将其设置为一个元组，
# 其中包含三个 0～1 的浮点数，分别表示红色、绿色和蓝色分量。
# !!! 值越接近 0，指定的颜色越深；值越接近 1，指定的颜色越浅。
# ax.scatter(x_values, y_values, s=10, color=(0, 0.8, 0))

# 参数 c 类似于参数 color，但用于将一系列值关联到颜色映射。
# 这里将参数 c 设置成了一个 y 坐标值列表，并使用参数 cmap 告诉pyplot 使用哪个颜色映射。
# 这些代码将 y 坐标值较小的点显示为浅蓝色，将 y 坐标值较大的点显示为深蓝色
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置标题并加上标签
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=10)
ax.set_ylabel('Square of values', fontsize=10)

# 设置刻度标记的样式
ax.tick_params(labelsize=10)

# axis() 方法指定每个坐标轴的取值范围
# axis() 方法要求提供四个值：x轴和 y 轴各自的最小值和最大值。
# 这里将 x 轴的取值范围设置为 0～1100，将 y 轴的取值范围设置为 0～1 100 000

ax.axis((0, 1100, 0, 1_100_000))

ax.ticklabel_format(style='plain')

# plt.show()

save_path = Path(__file__).parent.parent / 'assets' / 'my_scatter.png'

# 第二个实参指定将绘图多余的空白区域裁剪掉。
# 如果要保留绘图周围多余的空白区域，只需省略这个实参即可。
# 你还可以在调用 savefig() 时使用 Path 对象，将输出文件存储到系统上的任何地方。
plt.savefig(save_path, bbox_inches='tight')
