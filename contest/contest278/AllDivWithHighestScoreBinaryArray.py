#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        #cnt = collections.Counter(nums)
        d = collections.defaultdict(list)
        res = sum(nums)
        d[res].append(0)
        for i in range(len(nums)):
            if nums[i] == 0:
                res += 1
            if nums[i] == 1:
                res -=1 
            d[res].append(i+1)
        
        max_key = max(d.keys())
        return d[max_key]
            
