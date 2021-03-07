#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
class MyHashMap(object):

    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for _ in range(1<<15)]


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t][i] = (k, value)
                return
        self.arr[t].append((key, value))


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key: return v
        return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.arr[t]):
            if k == key:
                self.arr[t].remove((k,v))



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
def main():
    pass


if __name__ == "__main__":
    main()

