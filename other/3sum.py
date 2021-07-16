#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                lastNumber = target - nums[i] - nums[j]
                if lastNumber in seen:
                    arr = sorted([nums[i], nums[j], lastNumber])
                    ans.add((arr[0], arr[1], arr[2]))
            seen.add(nums[i])
        return ans
