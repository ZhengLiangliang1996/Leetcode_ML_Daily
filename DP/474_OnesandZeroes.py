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
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # 背包问题 dp[m][n] 代表用m个1和n个0可以找到了最大subset个数
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            cp = Counter(s)
            c_1 = cp['1']
            c_0 = cp['0']

            for i in range(m, c_0-1, -1):
                for j in range(n, c_1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-c_0][j-c_1] + 1)

        return dp[m][n]

def main():
    pass


if __name__ == "__main__":
    main()

