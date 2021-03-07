#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
class MyHashSet(object):

    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        t = self.eval_hash(key)
        return key in self.arr[t]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
def main():
    pass


if __name__ == "__main__":
    main()

