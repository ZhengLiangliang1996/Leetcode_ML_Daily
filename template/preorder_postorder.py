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

def construct_Tree(postorder, inorder):
    if not postorder or not inorder:
        return None

    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])

    root.left = construct_Tree(postorder[:index], inorder[:index])
    root.right = construct_Tree(postorder[index:-1], inorder[index+1:])
    return root

# recursion of postorder
def postorder_recursion(root):
    if not root:
        return
    postorder_recursion(root.left)
    postorder_recursion(root.right)
    print(root.val)

# recursion of preorder
def preorder_recursion(root):
    if not root:
        return
    print(root.val)
    preorder_recursion(root.left)
    preorder_recursion(root.right)


# iteration of preorder
def postorder_iterative(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()

        if node:
            res.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    res.reverse()
    print(res)

# iteration of preorder
def preorder_iterative(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        if not node:
            continue
        res.append(node.val)

        #if node.right:
        stack.append(node.right)
        #if node.left:
        stack.append(node.left)
    print(res)


def main():
    postorder = [9,15,7,20,3]

    inorder = [9,3,15,20,7]

    root = construct_Tree(postorder, inorder)

    postorder_recursion(root)
    postorder_iterative(root)

    preorder_recursion(root)
    preorder_iterative(root)
if __name__ == "__main__":
    main()

