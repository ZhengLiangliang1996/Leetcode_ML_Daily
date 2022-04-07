#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0 
        for i in range(len(nums)-1):
            # after deletion res += 1, i becomes i - res 
            if (i - res) % 2 == 0:
                if nums[i] == nums[i + 1]:
                    res += 1
        
        if (n - res) % 2 != 0:
            return res + 1
        
        return res 
        
