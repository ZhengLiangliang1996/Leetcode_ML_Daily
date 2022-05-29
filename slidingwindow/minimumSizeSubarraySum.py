#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        sum1 = 0
        res = float('inf')
        for r in range(n):
            sum1 += nums[r]
            while l <= r and sum1 >= target:
                res = min(res, r - l + 1)
                sum1 -= nums[l]
                l += 1
        return 0 if res == float('inf') else res 
