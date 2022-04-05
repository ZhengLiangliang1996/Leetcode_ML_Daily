#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                nums[j] = (nums[j] + nums[j+1]) % 10
            
        
        return nums[0]
