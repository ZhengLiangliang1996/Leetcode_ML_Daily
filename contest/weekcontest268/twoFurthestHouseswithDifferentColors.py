#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(colors)):
            for j in range(len(colors) - 1, i - 1, -1):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
                    break
        return res
