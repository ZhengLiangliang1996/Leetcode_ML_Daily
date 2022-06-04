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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return ""
        
        def dfs(root, r):
            if not root:
                return 
            
            if root and not root.left and not root.right:
                res.append(r[::-1])
            
            if root.left:
                dfs(root.left, r + chr(root.left.val + ord('a')))
            if root.right:
                dfs(root.right, r + chr(root.right.val + ord('a')))
        dfs(root, chr(root.val + ord('a')))
        s = sorted(res)
        return s[0]
        
