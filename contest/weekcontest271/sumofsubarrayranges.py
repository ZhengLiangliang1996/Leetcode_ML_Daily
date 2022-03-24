#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        n = len(nums)
        res = 0
        for i in range(n): #O(n)
            maxheap = [-nums[i]]
            minheap = [nums[i]]
            for j in range(i+1, n): # O(n)
                heapq.heappush(maxheap, -nums[j]) # O(lgn)
                heapq.heappush(minheap, nums[j]) # O(lgn)
                res += -maxheap[0] - minheap[0]
                
        return res
