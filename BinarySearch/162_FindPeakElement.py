#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            
            if nums[mid] >= nums[mid+1]:
                r = mid 
            else:
                l = mid + 1
            
        return l
