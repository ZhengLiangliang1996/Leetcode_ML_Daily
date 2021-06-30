#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP, pathQ = self.findpath(root, p), self.findpath(root, q)
        ans = None
        if pathP and pathQ:
            length = min(len(pathQ), len(pathP))
            ans = None
            for i in range(length):
                if pathP[i] != pathQ[i]:
                    break
                ans = pathP[i]
        return ans
    
    def findpath(self, root, key):
        if not root:
            return
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack[-1]
                if tmp.right and tmp.right != lastVisit:
                    root = tmp.right
                else:
                    if tmp.val == key.val:
                        return stack
                    else:
                        lastVisit = stack.pop()
                        root = None
