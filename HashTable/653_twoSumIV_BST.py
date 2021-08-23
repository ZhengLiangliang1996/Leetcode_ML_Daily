#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        def inorder(root):
            if not root:
                return
            else:
                res.append(root.val)

            if root.left:
                inorder(root.left)

            if root.right:
                inorder(root.right)

        inorder(root)

        # creat dict
        a = {value:index for index, value in enumerate(res)}

        for idx1, val1 in enumerate(res):
            val2 = k - val1
            if val2 in a and idx1 != a[val2]:
                return True

        return False:
