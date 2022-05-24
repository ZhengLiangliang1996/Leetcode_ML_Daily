#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def surfaceArea(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        
        for i in range(len(g)):
            for j in range(len(g[0])):
                # if no neighbor
                s = 4 * g[i][j] + 2 if g[i][j] > 0 else 0
                
                if i > 0:
                    s -= min(g[i][j], g[i-1][j]) 
                if i != len(g) - 1:
                    s -= min(g[i][j], g[i+1][j]) 
                if j > 0:
                    s -= min(g[i][j], g[i][j-1])
                if j != len(g[0]) - 1:
                    s -= min(g[i][j], g[i][j+1])
                res += s 
        
        return res 
