#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def traverse(root):
            if not root:
                return

            res.append(root.val)
            for child in root.children:
                traverse(child)
        traverse(root)
        print(res)
        return res
def main():
    pass


if __name__ == "__main__":
    main()

