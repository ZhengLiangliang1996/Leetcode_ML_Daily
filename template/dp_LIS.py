#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

def numofLIS(nums):
    if not nums:
        return 0

    k = len(nums)
    dp = [1] * k
    dp_n = [1] * k
    for i in range(1, k):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    dp_n[i] = dp_n[j]
                elif dp[j] + 1 == dp[i]:
                    dp_n[i] += dp_n[j]

    max_a = max(dp)
    total = 0
    for i in range(k):
        if dp[i] == max_a:
            total += dp_n[i]

    return total

def lengthOfLIS(nums):
    if not nums:
        return 0

    k = len(nums)
    dp= [1] * k
    for i in range(1, k):
        for j in range(i):
            if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

def main():
    A = [10, 9, 2, 5, 3, 7, 101, 18]
    a = lengthOfLIS(A)
    b = numofLIS(A)
    print(a)
    print(b)

if __name__ == "__main__":
    main()

