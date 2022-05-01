#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce 
        res = []
        def subset(path, start):
            res.append(path)
            
            for i in range(start, len(nums)):
                subset(path + [nums[i]], i+1)
        
        subset([], 0)
        rsl = 0 
        for r in res:
            if len(r) == 1:
                rsl += r[0]
            else:
                tmp = reduce(lambda x, y: x ^ y, r)
                rsl += tmp 
        return rsl 
