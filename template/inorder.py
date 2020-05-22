#! /usr/bin/env python
"""
Author: LiangLiang ZHENG
Date:
File Description
"""

from __future__ import print_function
import sys
import argparse
import numpy as np

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct_Tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])

    root.left = construct_Tree(preorder[1:index+1], inorder[:index])
    root.right = construct_Tree(preorder[index+1:], inorder[index+1:])
    return root

# recursion of inorder
def inorder_recursion(root):
    if not root:
        return
    inorder_recursion(root.left)
    print(root.val)
    inorder_recursion(root.right)

# iteration of inorder
def inorder_iterative(root):
    res = []
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        left = stack.pop()
        print(left.val)
        root = left.right

def main():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    root = construct_Tree(preorder, inorder)

    inorder_recursion(root)
    inorder_iterative(root)
if __name__ == "__main__":
    main()

