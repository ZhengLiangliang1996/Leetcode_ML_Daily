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
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(root):
            if not root:
                return 0
            else:
                return max(maxDepth(root.left), maxDepth(root.right)) + 1

        md = maxDepth(root)
        #print(md)
        self.res = 0
        def dfs(root, depth):
            #print(depth)
            if not root.left and not root.right and depth == md:
                self.res += root.val

            if root.left:
                dfs(root.left, depth+1)

            if root.right:
                dfs(root.right, depth+1)

        dfs(root, 1)
        return self.res
def main():
    pass


if __name__ == "__main__":
    main()

