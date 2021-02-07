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
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ans = []
        es = []
        s1 = s
        for i in range(len(s)):
            if s[i] ==  c:
                es.append(i)

        for i in range(len(s)):
            dis = float('inf')
            if s[i] == c:
                ans.append(0)
            else:
                for j in es:
                    dis = min(dis, abs(i-j))
                ans.append(dis)

        return ans
def main():
    pass


if __name__ == "__main__":
    main()

