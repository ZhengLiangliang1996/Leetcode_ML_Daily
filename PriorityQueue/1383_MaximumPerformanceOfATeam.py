#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maxPerformance(self, n, s, e, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        engineers = list(zip(e, s))
        # define minumum priority queue to store last minumum speed 
        minHeap = []
        sumSpeed = 0
        ans = 0
        
        for e, s in sorted(engineers)[::-1]:
            sumSpeed += s
            heappush(minHeap, s)
            
            if len(minHeap) > k:
                sumSpeed -= heappop(minHeap)
        
            ans = max(ans, sumSpeed * e)
        
        return ans % MOD
            
        
        
