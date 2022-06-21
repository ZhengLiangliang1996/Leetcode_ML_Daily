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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0 
            
            return dfs(root.left) + dfs(root.right) + root.val
        
        s_all = dfs(root)
        self.res = 0
        def dfs1(root):
            if not root:
                return 0
            # will use the return of left and right sum 
            l_sum = dfs1(root.left)
            r_sum = dfs1(root.right)
                
            self.res = max(self.res, (s_all-l_sum)*l_sum, (s_all-r_sum)*r_sum)

            return l_sum + r_sum + root.val
        dfs1(root)
        return self.res % (10**9 + 7)
