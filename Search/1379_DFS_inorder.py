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
    def getTargetCopy(self, o, c, t):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        res = None

        def inorder(root1, root2):
            if root1:
                inorder(root1.left, root2.left)
                if root1 is t:
                    self.res = root2
                inorder(root1.right, root2.right)

        inorder(o, c)
        return self.res

def main():
    pass


if __name__ == "__main__":
    main()

