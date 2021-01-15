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
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        if n <= 1:
            return n

        num = [0] * (n+1)
        num[1] = 1
        step = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                num[i] = num[step]
                step += 1
            else:
                num[i] = num[step-1] + num[step]


        return max(num)

def main():
    pass


if __name__ == "__main__":
    main()

