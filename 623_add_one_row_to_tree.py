#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):


        if not root: return root
        if d == 1:
            left = TreeNode(v)
            left.left = root
            root = left
        elif d == 2:
            left = TreeNode(v)
            right = TreeNode(v)
            left.left = root.left
            right.right = root.right
            root.left = left
            root.right = right
        else:
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)
        return root




def main():
    pass


if __name__ == "__main__":
    main()

