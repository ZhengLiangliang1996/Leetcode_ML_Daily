#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1, res2 = [], []
        def preorder(root, res):
            if not root:
                return 
            if root and not root.left and not root.right:
                res.append(root.val)
            if root.left:
                preorder(root.left, res)
            if root.right:
                preorder(root.right, res)
        preorder(root1, res1)
        preorder(root2, res2)
        return res1 == res2            
