
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


def level_order_without_level_output(root):
    res = []
    q = [root]

    while q:
        node = q.pop(0)
        print(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
# use collections.deque() with popleft will be faster
# this is also BFS, BFS will have a visted in graph
def level_order_with_level_output(root):
    res = []
    q = [root]

    while q:
        res.append([node.val for node in q])

        Q = []
        while q:
            node = q.pop(0)

            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        q = Q

    print(res)


def main():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    root = construct_Tree(preorder, inorder)

    level_order_without_level_output(root)
    level_order_with_level_output(root)
if __name__ == "__main__":
    main()

