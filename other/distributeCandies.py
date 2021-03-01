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
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        num = int(math.ceil(len(candyType) / 2))
        unique = set(candyType)
        return min(num, len(unique))
def main():
    pass


if __name__ == "__main__":
    main()

