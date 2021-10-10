#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        n+1 number, all number in [1, n], definitely one duplicate
        Requirement:
        1. don't change the original list (no sorting, on extra space)
        2. lower than O(n^2), can not use brute force 
        
        Solution: Binary Search 
        Search in [1, n], count midian, iterate the list and count all numbers that is lower or equal to mid, then it means the duplicate appear in [mid+1, n], otherwise it will be in [1, mid) 
        Bound: l -> 1 staring number 
               r -> len(nums)  e.g. [3,1,3,4,2] -> 5 
               search space [l, r) -> [1, 4]
        '''
        l = 1
        r = len(nums)
        
        while l < r:
            mid = l + ((r - l) >> 1)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if mid >= cnt: 
                l = mid + 1
            else:
                r = mid 
        
        return l
