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
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1


def main():
    pass


if __name__ == "__main__":
    main()

