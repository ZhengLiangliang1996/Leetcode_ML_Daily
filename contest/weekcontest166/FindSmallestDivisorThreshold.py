#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def helper(self,nums,m):
        Sum = 0
        for n in nums:
            Sum += math.ceil(n/m)
        return Sum
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1, max(nums)
        while l < r:
            mid = (l+r)//2
            Sum = self.helper(nums,mid)
            if Sum > threshold:
                l = mid + 1
            else:
                r = mid     
        return l
