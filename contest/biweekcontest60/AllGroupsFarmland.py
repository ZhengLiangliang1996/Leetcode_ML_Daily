#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findFarmland(self, l):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        m, n = len(l), len(l[0])
        d = [0, -1, 0, 1, 0]
        visited = set()
        
        def dfs(x, y, c):
            if (x, y) in visited:
                return 
            l[x][y] = 0
            visited.add((x, y))
            c[0] = min(x, c[0])
            c[1] = min(y, c[1])
            
            c[2] = max(x, c[2])
            c[3] = max(y, c[3])
            
            for i in range(4):
                x1 = x + d[i]
                y1 = y + d[i+1]
                
                if 0 <= x1 < m and 0 <= y1 < n and l[x1][y1] == 1:
                    dfs(x1, y1, c)
        
        for i in range(m):
            for j in range(n):
                if l[i][j] == 1 and (i, j) not in visited:
                    c = [float('inf'), float('inf'), float('-inf'), float('-inf')]
                    dfs(i, j, c)
                    res.append(c)
        return res 
