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
    def convert(self, s, r):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        1、zigzag = ['' for i in range(numRows)]表示产生numRows个为''的数组。

        2、row表示行数，step是一个标志表示下一步是向上走还是向下走。 if row == 0:  step = 1  if row == numRows - 1:  step = -1表示到第一行时向下走，走到最后一行开始向上走。

        3、''.join((zigzag))表示把zigzag的数组组合起来
        '''
        if r <= 1:
            return s

        zigzag = ['' for i in range(r)]

        row = 0
        step = 1
        for c in s:
            if row == 0:
                #往下走
                step = 1
            if row == r - 1:
                #往上走
                step = -1

            zigzag[row] += c
            row += step

        return ''.join((zigzag))
def main():
    pass


if __name__ == "__main__":
    main()

