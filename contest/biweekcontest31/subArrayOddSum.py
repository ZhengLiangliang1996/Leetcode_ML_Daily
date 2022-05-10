#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # prefix sum [1,3,5]-> [1,4,9]
        # all even -> 0
        # all odd -> 
        # some odd some even -> 
        MOD = (10 ** 9) + 7 
        prefix_sum = arr
        for i in range(1,len(arr)):
            prefix_sum[i] += prefix_sum[i-1]
        
        d = defaultdict(int)
        d[0], res = 1, 0

        for i in prefix_sum:
            res += d[0 if i%2 == 1 else 1]
            d[i%2] += 1
            
        return res % MOD 
