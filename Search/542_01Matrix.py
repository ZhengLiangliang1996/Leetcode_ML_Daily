#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        
        q = collections.deque()
        dist = [[float("inf") for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        dirs = [0,-1,0,1,0]
        while q:
            qSize = len(q)
            for j in range(qSize):

                x, y = q.popleft()

                for i in range(4):
                    a = x + dirs[i]
                    b = y + dirs[i+1]
                    if  0<=a<n and 0<=b<m and dist[a][b] - dist[x][y] > 1:
                        dist[a][b] = dist[x][y] + 1
                        q.append((a, b))
        
        return dist
