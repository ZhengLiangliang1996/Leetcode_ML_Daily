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
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        '''
        Use a stack to track the best solution so far, pop if the current number is less than the top of the stack and there are sufficient numbers left. Then push the current number to the stack if not full.

        Time complexity: O(n)
        Space complexity: O(k)
        '''

        ans = [None] * k
        n = len(nums)
        c = 0
        for i, x in enumerate(nums):
            while c and ans[c - 1] > x and c + n - i - 1 >= k:
                c -= 1
            if c < k:
                ans[c] = x
                c += 1
        return ans
def main():
    pass


if __name__ == "__main__":
    main()

