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
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubsequence(s, t):
            if s == "":
                return True
            if s != "" and t =="":
                return False

            j = 0
            for letter in t:
                if j < len(s) and s[j] == letter:
                    j += 1

            return j == len(s)

        res = ""

        for w in d:
            if isSubsequence(w, s):
                res = min(res, w, key = lambda x: (-len(x), x))

        return res

def main():
    pass


if __name__ == "__main__":
    main()

