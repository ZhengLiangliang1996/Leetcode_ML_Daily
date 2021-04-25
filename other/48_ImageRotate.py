#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
import numpy as np
class Solution(object):
    def rotate(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''
        1,2,3 -> 7,4,1

        4,5,6 -> 8,5,2

        7,8,9 -> 9,6,3

        In this case we need to change groups 1 -> 7 -> 9 - > 3 -> 1, 2 -> 4 -> 8 -> 6 -> 2 and 5 -> 5.
        '''
        n = len(M) - 1
        for i in range((n+2)//2):
            for j in range((n+1)//2):
                M[i][j], M[j][n-i], M[n-i][n-j], M[n-j][i] = M[n-j][i], M[i][j], M[j][n-i], M[n-i][n-j]
def main():
    pass


if __name__ == "__main__":
    main()

