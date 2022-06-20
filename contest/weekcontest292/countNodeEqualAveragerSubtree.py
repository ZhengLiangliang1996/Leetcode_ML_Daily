#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return (0, 0)
            l, r = dfs(root.left), dfs(root.right)
            sumS = l[0] + r[0] + root.val
            cntS = l[1] + r[1] + 1
            if sumS//cntS==root.val: self.res += 1
            return (sumS, cntS)
        dfs(root)
        return self.res
