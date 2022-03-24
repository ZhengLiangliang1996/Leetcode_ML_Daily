#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        res = 0
        d = collections.defaultdict(set)
        for i in range(0, len(rings)-1, 2):
            d[rings[i+1]].add(rings[i])
        
        for k in d.keys():
            if len(d[k]) == 3:
                res += 1
            
        
        return res 
            
