#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

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
def main():
    pass


if __name__ == "__main__":
    main()

