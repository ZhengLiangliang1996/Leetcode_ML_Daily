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
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        只需要找到临接的数比方 3,2,2,2,2,  或1,2,2,2,2 因为是subsequence 不是连续的,可以直接算counter
        '''

        C = collections.Counter(nums)
        res = 0
        for n in C:
            if C[n+1] != 0:
                res = max(res, C[n] + C[n+1])
        return res
def main():
    pass


if __name__ == "__main__":
    main()

