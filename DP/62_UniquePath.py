#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] means number of possible unique paths reach to bottom right 
        if m == 1 or n == 1: return 1
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                print(i, j)
                dp[i][j] =  dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]
