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
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) == 1:
            return True

        i = ord('a')
        odr_dict = {}
        for o in order:
            odr_dict[o] = chr(i)
            i+=1


        order_found = True

        new_words = []
        for w in words:
            path = ''
            for s in w:
                path += odr_dict[s]
            new_words.append(path)

        sort_words = new_words[:]
        sort_words.sort()
        print(sort_words)
        print(new_words)
        for i in range(len(new_words)):
            if new_words[i] != sort_words[i]:
                return False

        return True


if __name__ == "__main__":
    main()

