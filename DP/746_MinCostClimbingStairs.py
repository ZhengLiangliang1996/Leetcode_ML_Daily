#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp1 and dp2 are the minimum costs to reach step before current step and step which is two steps before current step. 
        dp1, dp2 = 0, 0
        for i in range(len(cost)):
            dp2, dp1 = dp1, cost[i] + min(dp1, dp2)
        
        return min(dp1, dp2)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] minimum coset of reach to step i
        if not cost: return 0
        if len(cost) <= 2: return min(cost)
        cost.append(0)
        dp = [0 for _ in range(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return dp[-1]
