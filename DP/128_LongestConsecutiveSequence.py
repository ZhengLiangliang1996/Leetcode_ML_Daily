#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        ans = 0
        max_rcd = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                max_rcd += 1
            elif nums[i] - nums[i-1] == 0:
                continue
            else:
                max_rcd = 0
            ans = max(ans, max_rcd)
        
        return ans + 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        @lru_cache(None)
        def dp(x):
            if x - 1 in seen:
                return dp(x - 1) + 1
            return 1

        ans = 0
        for x in seen:
            ans = max(ans, dp(x))
        return ans
