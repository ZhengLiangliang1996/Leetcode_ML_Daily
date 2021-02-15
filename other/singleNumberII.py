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
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        c = collections.Counter(nums)

        for k in c:
            if c[k] == 1:
                return k

        return -1
        '''
        return (3*sum(set(nums)) - sum(nums)) // 2
def main():
    pass


if __name__ == "__main__":
    main()

