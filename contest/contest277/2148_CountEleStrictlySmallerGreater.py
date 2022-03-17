#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)

        res = 0
        if len(cnt.keys()) <= 2:
            return res 
        for k in cnt.keys():
            
            if k != min(nums) and k != max(nums):
                res += cnt[k]
        
        return res 
    
    def countElements_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            if nums[i] != min(nums) and nums[i] != max(nums):
                res += 1 
        
        return res 
