#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse


def findMaxForm(strs, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for s in strs:
        zeros, ones = 0, 0
        for c in s:
            if c == '0':
                zeros += 1
            if c == '1':
                ones += 1

        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

    return dp[m][n]

def main():
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    a = findMaxForm(strs, m, n)
    print(a)

if __name__ == "__main__":
    main()

