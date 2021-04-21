#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

#from functools import lru_cache
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        #@lru_cache(None)
#         def dp(level, index):
#             if level == len(triangle) - 1: return triangle[level][index]
#             return min(dp(level+1, index), dp(level+1, index+1)) + triangle[level][index]

#         return dp(0, 0)


        bottom = list(triangle[-1])
        for row in reversed(triangle[:-1]):
            for j in range(len(row)):
                bottom[j] = row[j] + min(bottom[j], bottom[j+1])
        return bottom[0]
def main():
    pass


if __name__ == "__main__":
    main()

