#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = [False] * n, [False] * n
        left_max, right_min = 0, float('inf')
        
        for i in range(n):
            if left_max < nums[i]:
                left[i] = True
                left_max = nums[i]
            
            
        for i in range(n - 1, -1, -1):
            if right_min > nums[i]:
                right[i] = True
                right_min = nums[i]

        res = 0
        for i in range(1, n - 1):
            if left[i] and right[i]:
                res += 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                res += 1
        return res
        
        
