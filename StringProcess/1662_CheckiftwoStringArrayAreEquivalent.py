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
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # 知识点: list of string to single string "".join()
        '''
            list1 = ['1','2','3']
            s = "-"

            # joins elements of list1 by '-'
            # and stores in sting s
            s = s.join(list1)

            output: 1-2-3

        '''
        return "".join(word1) == "".join(word2) main():
    pass


if __name__ == "__main__":
    main()

