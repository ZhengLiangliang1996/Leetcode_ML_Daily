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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        # Solution 1: Brute Force (Time: O(n * 128)) Space: O(128)
        # inputs are ascii, only 128 unique
        # characters, so max length = 128
        n = len(s)
        res = 0
        j = 0
        #seen = 128 * [0]
        for i in range(n):
            #因为是要连续的，所以i设定扫描起始点
            j = i
            #起始点回归，重新开始计数
            seen = 128 * [0]
            while j < n and not seen[ord(s[j])]:
                seen[ord(s[j])] = 1
                j = j + 1
            res = max(res, j - i)

        return res


        '''

        # time: O(n) space: O(128)
        n = len(s)
        res = 0
        #idx所在的位置的值代表该字符在之前出现过的位置
        idx = [-1] * 128
        i = 0
        for j in range(n):
            # 确定左界，
            i = max(i, idx[ord(s[j])] + 1)
            res = max(res, j - i + 1)
            #更新
            idx[ord(s[j])] = j

        return res



if __name__ == "__main__":
    main()

