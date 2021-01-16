#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse


def partition(arr, left, right):
    i = left - 1
    # pivot is the last element
    pivot = arr[right]
    # j will scan from left to right - 1
    for j in range(left, right):
        # where i is actually the final position of all the elemnts that
        # are lower than the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # after scanning, move the pivot back to i+1
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1




# recursive way
def quicksort(arr, left, right):
    if len(arr) == 1:
        return arr

    if left < right:
        # pi is the partition index, arr[p] is now at the right place
        pi = partition(arr, left, right)

        # separately sort elements before and after the pi
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),

if __name__ == "__main__":
    main()

