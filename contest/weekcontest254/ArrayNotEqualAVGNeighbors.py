#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        res = []
        # first part 0~n//2 
        s = 0
        # second part n//2+1~n always greater than first part
        # put into the odd part 
        l = (n+1) // 2
        for i in range(n):
            if i & 1 == 0:
                res.append(nums[s])
                s += 1
            else:
                res.append(nums[l])
                l += 1
        
        return res 
            
