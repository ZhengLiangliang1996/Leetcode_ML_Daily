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
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        t = 0
        while k != 0 and len(arr) > 0:
            t = t + 1
            if arr[0] == t:
                arr.pop(0)
            else:
                k = k - 1


        if len(arr) == 0 and k != 0:
            t = t + k

        return t
def main():
    pass


if __name__ == "__main__":
    main()

