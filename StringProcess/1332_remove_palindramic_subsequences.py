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
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        if s == s[::-1]:
            return  1

        return 2
def main():
    pass


if __name__ == "__main__":
    main()

