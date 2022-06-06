#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        res = []
        for i, g in enumerate(groupSizes):
            if g == 1:
                res.append([i])
            elif (g not in d) or (g in d and len(d[g]) < g-1):
                d[g].append(i)
            elif g in d and len(d[g]) == g-1:
                d[g].append(i)
                res.append(d[g])
                d[g] = []
                
        
        return res 
