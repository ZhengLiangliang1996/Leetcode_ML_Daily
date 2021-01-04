#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            # print(p)
            p = p[c]
        p['#'] = True
        print(p)
        print(self.root)
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find(word)
        return node is not None and '#' in node


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        return p


def main():
    obj = Trie()
    obj.insert("apple")

if __name__ == "__main__":
    main()

