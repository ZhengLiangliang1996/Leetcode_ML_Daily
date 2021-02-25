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
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        head, tail = float('inf'), float('-inf')
        maxVal, minVal = nums[0], nums[-1]

        for i in range(n+1):
            # Find tail.
            if nums[i] < maxVal:
                tail = i
            else:
                maxVal = nums[i]
            # Find head.
            if nums[n-i] > minVal:
                head = n-i
            else:
                minVal = nums[n-i]

        return tail-head+1 if head < tail else 0
def main():
    pass


if __name__ == "__main__":
    main()

