#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""
merge sort 
"""

def mergeSort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) >> 2
    L_num = nums[:mid]
    R_num = nums[mid:]

    return merge(mergeSort(L_num), mergeSort(R_num))

def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))

    if not left:
        res += right
    if not right:
        res += left

    return res

def main():
    A = [3, 1, 0, -1, 6, 9]
    A_sort = mergeSort(A)
    print(A_sort)

if __name__ == "__main__":
    main()
