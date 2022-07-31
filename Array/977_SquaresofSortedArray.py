#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import math
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = [x*x for x in nums]
        n.sort()
        return n

    def sortedSquares_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in range(len(nums))]
        l, r = 0, len(nums)-1
        for idx in reversed(range(len(nums))):
            l_v = nums[l]
            r_v = nums[r]
            
            if abs(l_v) >= abs(r_v):
                res[idx] = l_v * l_v
                l += 1
            else:
                res[idx] = r_v * r_v
                r -= 1
        
        return res 
                
