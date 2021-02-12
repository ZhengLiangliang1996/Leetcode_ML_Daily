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
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            step += 1

        return step
def main():
    pass


if __name__ == "__main__":
    main()

