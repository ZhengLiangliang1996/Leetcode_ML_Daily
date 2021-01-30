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
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 滑动窗口　题解
        # 先算t里面的频次，用dict
        # 再用滑动　窗口对s进行计算，
        # 当count==len(t)并且　sdict中频次==tdict
        # 找到可能解, 取最小的range

        m = len(s)
        n = len(t)

        # frequency count dict
        scount = collections.defaultdict(int)
        # first count the frequncy
        tcount = collections.Counter(t)

        l, r, count = 0, 0, 0
        minLen = float('inf')
        res = ""

        # search in s
        # first move right pointer
        while r < m:
            # only when fre of elements in scount is
            # not reached as much as in tcount
            # the count will be increased
            scount[s[r]] += 1
            if s[r] in tcount and scount[s[r]] <= tcount[s[r]]:
                count += 1

            while l <= r and count == n:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    res = s[l:r+1]

                # since moved l,
                scount[s[l]] -= 1
                #左移l过程中移动的是range的值
                #那么count -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    count -= 1
                #左移
                l += 1

            r += 1

        return res
def main():
    pass


if __name__ == "__main__":
    main()

