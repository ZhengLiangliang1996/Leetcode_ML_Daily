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
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            # After the while, l and r are 1 more step outside(total 2 steps), the length cal should be r-l+1, in this
            # case, r-l+1-2
            # return the length e a b c b a d
            #                   l           r
            # so return r - l - 1
            return r - l - 1

        start = 0
        length = 0
        for i in range(n):
            # odd and even situation
            cur = max(getLen(i, i), getLen(i, i+1))

            if cur <= length: continue
            length = cur
            # Reasons why here is (cur - 1). convenient for both case to find the start index
            # return the length e a b c b a d (odd)  i = 3 len = 5  start = 3 - (5 - 1) // 2 = 1
            #                       <-i ->
            # return the length e a b c c b a d (even) i = 3 len = 6 start = 3 - (6 - 1) // 2 = 1
            #                         i i+1
            #
            start = i - (cur - 1) // 2

        return s[start:start+length]

def main():
    s = Solution()
    print(s.longestPalindrome("babad"))

if __name__ == "__main__":
    main()

