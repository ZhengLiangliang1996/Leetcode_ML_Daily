#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findPaths(self, m, n, N, i, j):
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dfs(N, i, j):
            # reached to the boundry
            if i == m or j == n or i < 0 or j < 0: return 1
            if N == 0: return 0
            return sum(dfs(N-1,i+x,j+y) for x,y in [[-1,0],[1,0],[0,-1],[0,1]])%MOD
        
        return dfs(N, i, j)
