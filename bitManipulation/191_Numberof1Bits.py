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
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        LeetCode给出的另一种巧妙解法。

        当n&(n-1)!=0时说明n中至少包含一个1.

        通过不停的n=n&(n-1)的方法可以将最后的一个1消掉。

        res = 0
        while n:
            res += 1
            n &= n - 1

        return res
        '''
        #转为2进制 算里面的1的个数
        return bin(n).count("1")
def main():
    pass


if __name__ == "__main__":
    main()

