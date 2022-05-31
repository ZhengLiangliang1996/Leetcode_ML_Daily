#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maxDistance(self, g: List[List[int]]) -> int:
        n = len(g)
        q = collections.deque()
        d = 0
        
        # all 0 or all 1
        if sum([sum(row) for row in g]) == 0 or sum([sum(row) for row in g]) == n*n:
            return -1
        
        for i in range(n):
            for j in range(n):
                if g[i][j] == 1:
                    q.append((i, j, d))
                    
        dirs = [0, -1, 0, 1, 0]
        while q:
            x, y, d = q.popleft()
            for k in range(4):
                nx, ny = x+dirs[k], y+dirs[k+1]
                if 0<=nx<n and 0<=ny<n and g[nx][ny]==0:
                    g[nx][ny] = 1
                    q.append((nx, ny, d+1))
    
        return d
