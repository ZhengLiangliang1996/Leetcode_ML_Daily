#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air.localdomain>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        evenIdx, oddIdx = 0, 1
        while evenIdx < n and oddIdx < n:
            
            if nums[evenIdx] % 2 != 0 and nums[oddIdx] %2 == 0:
                tmp = nums[evenIdx]
                nums[evenIdx] = nums[oddIdx] 
                nums[oddIdx] = tmp 
                
                evenIdx += 2
                oddIdx += 2
            elif nums[evenIdx] % 2 != 0 and nums[oddIdx] %2 != 0:
                oddIdx += 2
            elif nums[evenIdx] % 2 == 0 and nums[oddIdx] %2 == 0:
                evenIdx += 2
            else: 
                evenIdx += 2
                oddIdx +=2 
        
        return nums
                
