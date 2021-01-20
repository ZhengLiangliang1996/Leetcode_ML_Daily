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
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=[]
        a=['(','{','[']
        for i in range(len(s)):
            if s[i] in a:
                v.append(s[i])
                continue
            elif s[i]==')':
                if len(v)==0 or v.pop()!='(':
                    return False
            elif s[i]==']':
                if len(v)==0 or v.pop()!='[':
                    return False
            elif s[i]=='}':
                if len(v)==0 or v.pop()!='{':
                    return False
        return len(v)==0
def main():
    pass


if __name__ == "__main__":
    main()

