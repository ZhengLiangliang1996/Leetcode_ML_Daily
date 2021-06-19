#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # define dp[n][k] dp[i][j]: 1-i there are j inverse pair 
        # transition function: it depends on the place it put 
        # [X X X X X] 6 -> [6 X X X X X] -> 5 pairs  dp[6][j] will be equal to dp[5][j-5]
        #               -> [X 6 X X X X] -> 4 pairs  dp[6][j] will be equal to dp[5][j-4]
        #               -> [X X 6 X X X] -> 3 pairs  
        # TLE 
        '''
        dp = [[0]*(k+1) for _ in range(n+1)]
        # initialization 
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                for x in range(i):# to i-1
                    if j >= x:
                        dp[i][j] += dp[i-1][j-x]
                        dp[i][j] %= MOD 
                    
        return dp[n][k]
        '''
        
        # 运用裂项公式
        #dp[i][j] = dp[i-1][j-0] + dp[i-1][j-1] + ... + dp[i-1][j-(i-2)] + dp[i-1][j-(i-1)]
        #dp[i][j-1] = dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-(i-1)] + dp[i-1][j-(i)]
        #dp[i][j] - dp[i][j-1] = dp[i-1][j] - dp[i-1][j-i]
        #dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        # initialization 
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                if i <= j:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                dp[i][j] %= MOD
                    
        return dp[n][k]
        
