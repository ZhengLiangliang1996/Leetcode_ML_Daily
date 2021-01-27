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
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1
        #res =  ""
        #for i in range(1, n+1):
        #    res += bin(i)[2:]

        #return int(res, 2) % (10 ** 9 + 7)

        # Solution 2
        s = 0
        for i in range(1, n+1):
            s = (s << i.bit_length() | i) % 1000000007

        return s
def main():
    pass


if __name__ == "__main__":
    main()

