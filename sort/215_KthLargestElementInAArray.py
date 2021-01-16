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
    def findKthLargest(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(arr) == 0 or k == 0:
            return 0

        left = 0
        right = len(arr) - 1

        def partition(arr, left, right):
            i = left - 1
            pivot = arr[right]

            for j in range(left, right):
                if arr[j] >= pivot: # //reverse the comparision sign for kth smallest element, also standard quick sort partition in this case
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i+1], arr[right] = arr[right], arr[i+1]
            return i+1


        while True:
            pi = partition(arr, left, right)
            if pi + 1 == k:
                return arr[pi]
            elif pi + 1 > k:
                right = pi - 1
            else:
                left = pi + 1

    def solution2(self, arr, k):
        arr.sort()
        return arr[k-1]

def main():
    pass


if __name__ == "__main__":
    main()

