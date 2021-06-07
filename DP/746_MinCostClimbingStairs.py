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
