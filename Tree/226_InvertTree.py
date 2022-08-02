#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# O(N), O(N)
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         if not root:
#             return None
        
#         tmp = TreeNode(0)
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp
        
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)
        return root

# Recursion Time: O(N), Space: O(depth of tree)
class Solution1(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

 
