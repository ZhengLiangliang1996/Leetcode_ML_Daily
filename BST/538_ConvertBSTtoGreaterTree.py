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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0

        def recursion(root):
            if not root: return None
            recursion(root.right)
            self.sum += root.val
            root.val = self.sum
            recursion(root.left)

        recursion(root)

        return root
def main():
    pass


if __name__ == "__main__":
    main()

