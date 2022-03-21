#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        cost.sort(reverse=True)
        for i in range(2, len(cost), 3):
            cost[i] = 0

        print(cost)
        return sum(cost)
        
