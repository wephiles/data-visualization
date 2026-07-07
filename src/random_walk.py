#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/07 21:34
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/random_walk.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

from random import choice


class RandomWalk:
    """一个生成随机游走数据的类"""

    def __init__(self, num_points: int = 5000):
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有随机游走都始于 (0, 0)
        self.values_x = [0]
        self.values_y = [0]

    def fill_walk(self):
        """计算包含随机游走的所有点"""

        # 不断游走, 直到列表到达指定的长度
        while len(self.values_x) < self.num_points:
            # 决定前进的方向和在这个方向前进的距离
            x_directions = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_directions * x_distance

            y_directions = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_directions * y_distance

            # 去掉在原点的数据
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            x = self.values_x[-1] + x_step
            y = self.values_y[-1] + y_step

            self.values_x.append(x)
            self.values_y.append(y)
