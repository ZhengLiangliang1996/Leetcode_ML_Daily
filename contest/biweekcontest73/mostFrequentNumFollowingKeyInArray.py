#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                d[nums[i+1]] += 1
                
        mv = max(d.values())
        
        for k in d.keys():
            if d[k] == mv:
                return k
