#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
from sortedcontainers import SortedList

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        # 1 . TLE Solution
        '''
        res = 0

        if len(instructions) <= 2:
            return 0

        def calculate(a):
            c_less = 0
            c_great = 0
            for i in range(len(a)-1):
                if a[i] == a[len(a)-1]:
                    continue
                if a[i] < a[len(a)-1]:
                    c_less += 1
                if a[i] > a[len(a)-1]:
                    c_great += 1
            return c_less, c_great

        for i in range(2, len(instructions)):
            c_less, c_great = calculate(instructions[:i+1])
            res = res + min(c_less, c_great)
        return res
        '''
        res = 0
        iList = SortedList()
        for num in instructions:
            # equal dose not count, use binary search to count
            res += min(iList.bisect_left(num), len(iList) -iList.bisect_right(num))
            #Since the answer may be large, return it modulo 109 + 7
            res %= 10**9 + 7
            iList.add(num)

        return res
def main():
    pass


if __name__ == "__main__":
    main()

