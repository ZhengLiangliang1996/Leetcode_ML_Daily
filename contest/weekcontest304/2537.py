#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        while sum(nums) > 0:
            m = min([x for x in nums if x > 0])
            nums = [x-m for x in nums if x > 0]
            cnt += 1
        
        return cnt 
