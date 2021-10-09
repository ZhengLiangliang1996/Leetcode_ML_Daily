#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def findClosestElements(self, nums, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0 
        r = len(nums) - k
        while l < r:
            mid = l + ((r - l) >> 1)
            # 比较区间两端的数值和x的距离，如果左边离得远了，就向右边走；如果右边离得远了，就像左边走。
            # 等于的情况下是往左靠
            if x - nums[mid] > nums[mid+k] - x:
                l = mid + 1
            else:
                r = mid
            
        return nums[l:l+k]
