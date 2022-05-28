#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countNegatives(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] < 0:
                    res += 1
        return res 
