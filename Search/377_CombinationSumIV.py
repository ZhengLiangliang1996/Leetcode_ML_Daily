#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        n = len(nums)
        def helper(target):
            if target < 0: return 0
            if target == 0: return 1
            if target in memo: return memo[target]
            res = 0
            for i in range(n):
                res += helper(target - nums[i])
            memo[target] = res
            return memo[target]

        return helper(target)
def main():
    pass


if __name__ == "__main__":
    main()

