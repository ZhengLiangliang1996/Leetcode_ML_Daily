#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if any([not obstacleGrid, obstacleGrid[-1][-1] == 1, obstacleGrid[0][0] == 1]): 
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # initialization
        # first column 
        flag = False 
        for i in range(m):
            if flag or obstacleGrid[i][0]:
                flag = True
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        flag = False
        # first row 
        for j in range(n):
            if flag or obstacleGrid[0][j]:
                flag = True
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
