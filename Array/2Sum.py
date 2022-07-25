#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    # Time: O(N^2) Space: O(1)
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
    
    # Time: O(N), Space O(N)
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d  = {}
        for idx, n in enumerate(nums):
            if target - n in d.keys():
                return [d[target-n], idx]
            else:
                d[n] = idx

        return [-1, -1]
    
    # if the list is sorted 
    # TIME: O(NlogN) for the sorting SPACE: O(1)
    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # double pointer 
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]

   

nums = [2,7,11,15]
target = 9

s = Solution()
print(s.twoSum_1(nums, target))
print(s.twoSum_2(nums, target))
print(s.twoSum_3(nums, target))
