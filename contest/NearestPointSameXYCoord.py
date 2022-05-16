#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res = []
        
        for x1, y1 in points:
            if x1 == x or y == y1:
                d = abs(x1 - x) + abs(y1 - y)
                res.append(d)
            else:
                res.append(float('inf'))
        
        if min(res) == float('inf'): return -1 
        return res.index(min(res))
