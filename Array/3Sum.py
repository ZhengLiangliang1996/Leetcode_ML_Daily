#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    # Time:O(N^2)  Space: O(N)
    def ThreeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                     res.append([nums[i], nums[l], nums[r]])
                     l += 1
                elif nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res
   

nums = [-1,0,1,2,-1,-4]
target = 0

s = Solution()
print(s.ThreeSum(nums, target))
