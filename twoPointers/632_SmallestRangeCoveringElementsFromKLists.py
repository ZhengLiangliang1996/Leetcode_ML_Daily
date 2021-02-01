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
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        #与76相同,76是找s中range cover t中的最小range
        #这道题目变成每个list至少被包含一次,所以scount
        #是要统计list的index而不是list中element的出现频次!!
        v  = []
        for i in range(len(nums)):
            for num in nums[i]:
                v.append((num, i))
        v.sort()
        l, r, n = 0, 0, len(v)
        d = collections.defaultdict(int)
        k = len(nums)
        cnt = 0
        res = [0, 0]
        diff = float('inf')
        while r < n:
            if d[v[r][1]] == 0:
                cnt += 1
            d[v[r][1]] += 1
            while l <= r and cnt == k:
                if v[r][0] - v[l][0] < diff:
                    diff = v[r][0] - v[l][0]
                    res = [v[l][0], v[r][0]]
                d[v[l][1]] -= 1
                if d[v[l][1]] == 0:
                    #del d[v[l][1]]
                    cnt -= 1
                l += 1
            r += 1
        return res


def main():
    pass


if __name__ == "__main__":
    main()

