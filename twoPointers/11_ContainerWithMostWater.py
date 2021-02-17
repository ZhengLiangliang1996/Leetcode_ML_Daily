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
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(n) space:O(1)
        res = float('-inf')
        l = 0
        r = len(height) - 1

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return res
def main():
    pass


if __name__ == "__main__":
    main()

