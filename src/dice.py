#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @CreateTime : 2026/07/07 23:15
# @Author     : wephiles@wephiles
# @IDE        : PyCharm
# @ProjectName: data_visualization
# @FileName   : data_visualization/dice.py
# @Description: This is description of this script.
# @Interpreter: python 3.0+
# @Motto      : You must take your place in the circle of life!
# @AuthorSite : https://github.com/wephiles or https://gitee.com/wephiles

# Copyright (c) 2026 wephiles.
# This software is licensed under the MIT license.
# See the LICENSE file for details.

"""
模拟一个骰子的情况
"""

from random import randint


class Dice:
    """表示一个骰子的类"""

    def __init__(self, num_sides: int = 6):
        """骰子默认为 6 面的"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个介于 1 和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
