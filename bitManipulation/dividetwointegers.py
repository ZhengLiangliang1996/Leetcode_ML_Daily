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
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        div = divisor
        left = dividend

        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans += Q
            Q+=Q
            div += div
            if left < div:
                Q = 1
                div = divisor

        if not neg:
            return min(ans,2147483647)
        else:
            return max(-ans,-2147483648)
def main():
    pass


if __name__ == "__main__":
    main()

