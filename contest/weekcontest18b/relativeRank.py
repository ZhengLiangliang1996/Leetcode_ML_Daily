#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findRelativeRanks(self, s: List[int]) -> List[str]:
        res = []
        s_r = sorted(s)[::-1]
        for i in s:
            if s_r.index(i) == 0:
                res.append("Gold Medal")
            elif s_r.index(i) == 1:
                res.append("Silver Medal")
            elif s_r.index(i) == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(s_r.index(i)+1))
        
        return res 
