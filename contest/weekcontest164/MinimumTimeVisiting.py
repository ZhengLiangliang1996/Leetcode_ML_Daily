#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        res = 0
        for i in range(len(p)-1):
            res += max(abs(p[i][0] - p[i+1][0]), abs(p[i][1] - p[i+1][1]))
        return res 
