#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(g), len(g[0])
        visited = set()
        d = [0, -1, 0, 1, 0]
        
        def dfs(x, y):
            if (x, y) in visited:
                return 
            
            g[x][y] = '2'
            visited.add((x, y))
            
            for i in range(4):
                x1 = x + d[i]
                y1 = y + d[i+1]
                if 0<=x1<m and 0<=y1<n and g[x1][y1] == '1':
                    dfs(x1, y1)
        res = 0 
        for i in range(m):
            for j in range(n):
                if g[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        
        return res
