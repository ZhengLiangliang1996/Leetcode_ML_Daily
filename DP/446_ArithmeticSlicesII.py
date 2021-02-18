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
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        ''' dp[i][diff], end with element A[i] and the with diff
        [2, 4, 6, 8, 10]
        dp[2][2] = 1               [2,4,6]
        dp[3][2] = dp[2][2] + 1    [2,4,6,8](在之前的状态下加上8) + [4,6,8]
        '''

        ans = 0
        dp = defaultdict(int)
        for i in range(1, len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                ans += dp[(j, delta)]
                dp[(i, delta)] += dp[(j, delta)] + 1

        return ans
def main():
    pass


if __name__ == "__main__":
    main()

