#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air>
#
# Distributed under terms of the MIT license.

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        
        l = 0
        r = n * n
        
        # bfs
        def bfs(mid):
            if grid[0][0] > mid:
                return False
            
            q = []
            q.append(0)
            seen = [0 for i in range(n * n)]
            seen[0] = 1
            
            while q:
                a1 = q.pop(0)
                # 1d to 2d 
                x = a1 // n
                y = a1 % n
                
                # if reach to 右下
                if x == n - 1 and y == n - 1:
                    return True
                
                # EXTEND
                for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if a < 0 or b < 0 or a >= n or b >= n or grid[a][b] > mid:
                        continue
                    
                    # 2d to 1d
                    key = a * n + b
                    if seen[key]:
                        continue
                    
                    # marked as visited
                    seen[key] = 1
                    q.append(key)
            return False
        
        # binary search 
        while(l < r):
            mid = l + (r - l) // 2
            
            if bfs(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
