#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # explain: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/discuss/1833560/Java-O(N)-Explanation-with-Diagrams
        # 1. Get number of 1s
        # 2. Sliding window of size cnt_1
        # 3. sliding the (i + cnt - 1) % n (because of circular), and the least zeros is the ans  
        
        n = len(nums)
        
        cnt_1= sum(nums)
        cur = 0 
        if cnt_1 == 0:
            return 0
        # first window # of zeros 
        for i in range(cnt_1):
            if nums[i] == 0:
                cur += 1
        res = cur 
        for i in range(1, n):
            if nums[i-1] == 0:
                cur -= 1
            if nums[(i + cnt_1 - 1) % n] == 0:
                cur += 1
            res = min(res, cur)
        
        return res 
            
