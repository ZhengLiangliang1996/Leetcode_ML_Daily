#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        第一条规则说明单纯的乱序不影响判断两个字符串是否close。只要两个字符串排序后是一样的，那么就是close。

    第二条规则说明两个问题：首先两个字符串必须包含相同种类的字母，因为规则二本身无法创造出新的字母。如果两个字符串的字母种类不同，那么规则二是无法使得他们一致的（即使是乱序）。其次，同一个字符串中不同种类的字符可以互换彼此的频次，因此必然要求这两个字符串的字母频次分布也一致。因此一个close的必要条件就是将两个字符串的频次数组都分别排序，查验它们是否相同。
        '''

        c1, c2 = Counter(word1), Counter(word2)
        return all([len(word1) == len(word2),
                    c1.keys() == c2.keys(),
                    sorted(c1.values()) == sorted(c2.values())])
def main():
    pass


if __name__ == "__main__":
    main()

