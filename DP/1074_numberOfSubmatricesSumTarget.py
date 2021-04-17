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
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(np.cumsum(matrix[k]))
            for i, j in combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i,j,k-1), 0) + t[j] - t[i]

        for i, j in combinations(range(n+1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1

        return ans
def main():
    pass


if __name__ == "__main__":
    main()

