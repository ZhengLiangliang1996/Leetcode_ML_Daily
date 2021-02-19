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
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """


        n = len(s)
        l = 0

        ls = list(s)
        count = 0
        for i in range(n):
            if s[i] == '(':
                l += 1
            elif s[i] == ')':
                if l == 0:
                    ls.pop(i-count)
                    count += 1
                else:
                    l -= 1

        for i in range(len(ls)-1, -1, -1):
            if l == 0:
                break
            if ls[i] == '(' and l > 0:
                ls.pop(i)
                l -= 1

        return "".join(ls)
def main():
    pass


if __name__ == "__main__":
    main()

