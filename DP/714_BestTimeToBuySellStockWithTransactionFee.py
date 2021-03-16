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
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0

        dp_0, dp_1 = 0, float('-inf')
        for i in range(n):
            temp = dp_0
            dp_0= max(dp_0, dp_1 + prices[i]  - fee)
            dp_1 = max(dp_1, temp - prices[i])
        return dp_0
def main():
    pass


if __name__ == "__main__":
    main()

