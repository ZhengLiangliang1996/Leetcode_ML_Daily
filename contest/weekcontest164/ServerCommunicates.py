#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        
        def check_servers(r,c):
            
            for i in range(m):
                if i !=r:
                    if g[i][c] ==1:
                        return True
            for j in range(n):
                 if j !=c:
                    if g[r][j] ==1:
                        return True
            
            return False
        
        res = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1 and check_servers(i, j):
                    res += 1
        
        return res 
