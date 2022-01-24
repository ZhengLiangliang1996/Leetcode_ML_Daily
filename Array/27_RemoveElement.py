#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
#         n = len(nums)
#         idx = 0
#         for i in range(n):
#             if nums[i] != val:
#                 nums[idx] = nums[i]
#                 idx += 1
        
#         return idx
        if not nums: return 0
    
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            while i < j and nums[i] != val:
                i += 1
            while i < j and nums[j] == val:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        if nums[i] == val:
            return i 
        else:
            return i + 1
                
            
        
        
