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
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans, bal = 0, 0
        for i, s in enumerate(S):
            bal = bal + 1 if s == "(" else bal - 1
            if i > 0 and S[i-1:i+1] == "()":
                ans += 1 << bal
        return ans

def main():
    pass


if __name__ == "__main__":
    main()

