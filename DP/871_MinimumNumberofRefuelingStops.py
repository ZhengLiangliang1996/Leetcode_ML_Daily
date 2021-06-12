#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minRefuelStops(self, target, startFuel, s):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        '''
        One of the solution use dynamic programming. Let dp[i][j] be a maximum amount of fuel we can have, when we reached station number i and refueled j times before this station (not included). Let us also add two more points to our stops: starting one and ending one. Then, how we can update dp[i][j]: we can

Either refuel on previous station, than we have dp[i-1][j-1] minus distance we covered between i-1 and i stations and plus amount of fuel we get at last station.
Or it can be dp[i-1][j] plus distance we covered between i-1 and i stations.
If we have cand < 0 in our code, than it means we can not reach position i with j refuels, so we leave it equal to minus infinity. Finally, in the end we check last station and find the smallest index where value is not negative and return it.
        '''
        s = [[0, startFuel]] + s + [[target, 0]]
        n = len(s)
        ##   (#fules to next statio)         (# of fules left)
        t = [(s[i-1][0] - s[i][0], s[i-1][1] + s[i-1][0] - s[i][0]) for i in range(1, n)]
        dp = [[-float("inf")] * n for _ in range(n)]
        dp[0][0] = 0
        
        for i in range(1, n):
            for j in range(1, i+1):
                # choose betwen (dp[i-1][j]+distance we covered between i-1 to i stations)
                # and (prevous station dp[i-1][j-1])
                cand = max(dp[i-1][j] + t[i-1][0], dp[i-1][j-1] + t[i-1][1])
                if cand >= 0: dp[i][j] = cand
        
        for i, elem in enumerate(dp[-1]):
            if elem >= 0: return i - 1
                    
        return -1
                    
