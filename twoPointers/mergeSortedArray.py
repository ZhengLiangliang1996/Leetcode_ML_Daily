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
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        '''
        Easy problem if you know the trick, but not so easy if you see this type of idea first time. Here we need to use two observations:

It is definitely 2 pointers approach, we need to iterate through nums1 and nums2 and build solution, using merge.
Also, we need to start from end of our lists, and this is essential, if you start from the beginning of lists, you can accidentely rewrite you data, so you need to think where to put it first and it will be extra space.
So, all we do is:

define p1 = m - 1 and p2 = n - 1: pointers for nums1 and nums2.
We start from i = m + n - 1 and move in backward direction: we compare nums1[p1] and nums2[p2], write biggest number to nums1[i] and move one of the pointers: p1 or p2.
This is not all: it can happen, that when we reached p1 = 0, there are still some numbers we need to copy from nums2 to nums1, and in next step we do this.

        '''
        # double pointers
        p1, p2 = m - 1, n - 1

        for i in range(m + n - 1, -1, -1):
            if p1 < 0 or p2 < 0: break

            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i -= 1

def main():
    pass


if __name__ == "__main__":
    main()

