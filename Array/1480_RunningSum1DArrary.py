#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        results = [nums[0]]
        for i in range(1, len(nums)):
            results.append(nums[i] + results[i-1])
            
        return results 

