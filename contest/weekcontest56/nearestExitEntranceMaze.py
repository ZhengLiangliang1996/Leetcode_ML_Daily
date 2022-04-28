#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        step = 0
        m,n = len(maze), len(maze[0])
        if m == 1 and n == 1: return -1 
        dirs = [0, 1, 0, -1, 0]
        
        q = [(entrance[0], entrance[1])]
        visited = set()
                      
        for i in range(m):
            for j in range(n):
                if maze[i][j] == '+':
                      visited.add((i, j))
        visited.add((entrance[0], entrance[1]))
        while q:
            newQ = []
            step += 1
            print(q)
            for qSize in range(len(q)):
                x,y = q.pop()
                
                for i in range(4):
                    x1 = x + dirs[i]
                    y1 = y + dirs[i+1]
                    if (x1, y1) not in visited:
                        if (x1 == 0 and 0<=y1<n) or (0<=x1<m and y1 == 0) or (x1 == m-1 and 0<=y1<n) or (0<=x1<m and y1 == n-1):
                            return step
                        elif 0<=x1<m and 0<=y1<n:
                            newQ.append((x1, y1))
                            visited.add((x1, y1))
            q = newQ
                      
        return -1 
