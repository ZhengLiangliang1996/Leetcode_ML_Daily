#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max((nums[0] * nums[1] * nums[-1]), 
                   (nums[0] * nums[-2] * nums[-1]), 
                   nums[-1] * nums[-2] * nums[-3], 
                   nums[0] * nums[1] * nums[2])
