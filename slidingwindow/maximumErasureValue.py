#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0 
        res, l = 0, 0
        window = set()
        for r in range(n):
            while window and nums[r] in window:
                window.remove(nums[l])
                m -= nums[l]
                l += 1
                
            m += nums[r]
            window.add(nums[r])
            res = max(m, res)
        
        return res 
