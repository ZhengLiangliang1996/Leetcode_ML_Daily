#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse


def left_bound(nums, target):
	l = 0
	r = len(nums)
	while l < r:
		mid = l + (r - l) // 2
		if nums[mid] >= target:
			r = mid
		elif nums[mid] < target:
			l = mid + 1

	return l

def right_bound(nums, target):
	l = 0
	r = len(nums)
	while l < r:
		mid = l + (r - l) // 2
		if nums[mid] <= target:
			l = mid + 1
		else:
			r = mid

	return l - 1

def main():
    nums = [5,7,7,8,8,10]
    print("The left bound is", left_bound(nums, 6))
    print("The right bound is", right_bound(nums, 8))



if __name__ == "__main__":
    main()

