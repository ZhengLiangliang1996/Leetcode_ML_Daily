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
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True

        # tricks here, starting from index 0, the left side is definitely bigger than k.
        # set it to k and it's easier to do the for loop
        dist = k
        for num in nums:
            if num == 0: dist += 1
            elif num == 1 and dist >= k: dist = 0
            else: return False


        return True

def main():
    pass


if __name__ == "__main__":
    main()

