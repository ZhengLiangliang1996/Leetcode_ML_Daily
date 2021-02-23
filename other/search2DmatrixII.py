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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
#         for row in matrix:
#             if target in row:
#                 return True

#         return False

        #found from the top right
        x, y = len(matrix[0]) - 1, 0
        while x >= 0 and y < len(matrix):
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            else:
                return True
        return False
def main():
    pass


if __name__ == "__main__":
    main()

