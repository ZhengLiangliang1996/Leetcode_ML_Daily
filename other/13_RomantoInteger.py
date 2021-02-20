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
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

        last, res = m[s[-1]], 0
        for i in s[::-1]:
            if m[i] < last:
                res -= m[i]
            else:
                res += m[i]
                last = m[i]

        return res
def main():
    pass


if __name__ == "__main__":
    main()

