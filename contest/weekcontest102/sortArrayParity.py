#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                res = [nums[i]] + res
            else:
                res = res + [nums[i]]
        
        return res 
