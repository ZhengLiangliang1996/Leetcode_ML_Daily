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
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        Fill the entire string with ‘a’, k-=n, then fill in reverse order, replace ‘a’ with ‘z’ until not enough k left.
        '''
        res = ['a'] * n
        k -= n
        i = n - 1
        while k:
            d = min(k, 25) # when k is bigger than 25, take 25 and form 'z'
            res[i] = chr(ord(res[i]) + d) # turn a to z
            k -= d
            i -= 1

        return ''.join(res)


def main():
    pass


if __name__ == "__main__":
    main()

