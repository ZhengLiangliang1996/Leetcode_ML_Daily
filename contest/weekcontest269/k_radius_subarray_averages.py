#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        roll_sum = 0
        r = 2*k + 1
        if n < r:
            return [-1] * n
        
        for i in range(r):
            roll_sum += nums[i]
        
        res = [] 
        res.append(roll_sum // r)
        left, right = 0, r
        while right < n:
            roll_sum -= nums[left]
            roll_sum += nums[right]
            
            res.append(roll_sum // r)
            left += 1
            right += 1
    
        return k*[-1] + res + k*[-1]
            
