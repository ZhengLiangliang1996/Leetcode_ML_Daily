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
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        '''
        Simulate the push/pop operation.

Push element from |pushed sequence| onto stack s one by one and pop when top of the stack s is equal the current element in the |popped sequence|.

        Time complexity: O(n)

        Space complexity: O(n)
        '''
        s = []
        i = 0
        for e in pushed:
            s.append(e)
            while s and s[-1] == popped[i]:
                s.pop()
                i += 1
        return i == len(popped)
def main():
    pass


if __name__ == "__main__":
    main()

