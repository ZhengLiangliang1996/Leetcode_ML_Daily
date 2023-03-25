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
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #input n aim amount,the dp array will return the fewest amount of coins
        #min coins to make up j amount using first i types of coins
        #dp[-1][0]=0,dp[-1][j]=inf
        dp=[float('inf')] * (amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]

def main():
    pass


if __name__ == "__main__":
    main()

