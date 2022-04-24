#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        p_max = [-p for p in piles]
        heapq.heapify(p_max)
        for _ in range(k):
            m = -heapq.heappop(p_max)
            heapq.heappush(p_max, -(m - m/2))
        
        return -sum(p_max)
            
