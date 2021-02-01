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
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 求出每个位置所有可能的候选值，并放到一个数组 cc 中。
        #对于奇数x，它可以变换成2x,x; 对于偶数x，它可以变换成x, x/2, x/4, ... 直至变成一个奇数。我们将每个数和它的变换数看作是一组
        c = []
        for i in range(n):
            c.append((nums[i], i))
            if (nums[i] % 2 == 1):
                c.append((nums[i]*2, i))
            else:
                while nums[i] %2 == 0:
                    nums[i] /= 2
                    c.append((nums[i], i))


        c.sort()
        d = collections.defaultdict(int)
        count = 0
        res = float('inf')
        k = len(nums)
        l, r, n = 0, 0, len(c)

        while r < n:
            if d[c[r][1]] == 0:
                count += 1
            d[c[r][1]] += 1

            while l <= r and count == k:
                # The deviation of the array is the maximum difference between any two elements in the array.
                # after sorting, we could use this to calculate the deviation
                res = min(res, c[r][0] - c[l][0])

                d[c[l][1]] -= 1
                if d[c[l][1]] == 0:
                    del d[c[l][1]]
                    count -= 1

                l += 1

            r += 1

        return res


def main():
    pass


if __name__ == "__main__":
    main()

