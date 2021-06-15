#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def makesquare(self, nums):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        # Same as 698 and 416
        # Use DFS (backtracking)
        
        k = 4
        if not nums or len(nums) < k: return False
        _sum = sum(nums)
        div, mod = divmod(_sum, k)
        if _sum % k or max(nums) > _sum / k: return False
        nums.sort(reverse = True)
        # target is div 
        target = [div] * k
        return self.dfs(nums, k, 0, target)
        
    def dfs(self, nums, k, index, target):
        # 防守，end condition 
        if index == len(nums): return True
        num = nums[index]
        # choices 4 side, backtracking
        for i in range(k):
            if target[i] >= num:
                target[i] -= num
                if self.dfs(nums, k, index + 1, target): return True
                target[i] += num
        return False
