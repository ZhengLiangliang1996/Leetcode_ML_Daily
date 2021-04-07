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
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        s1_vowel = 0

        for i in s1:
            if i in vowel:
                s1_vowel +=1
        for j in s2:
            if j in vowel:
                s1_vowel -= 1

        return s1_vowel == 0

def main():
    pass


if __name__ == "__main__":
    main()

