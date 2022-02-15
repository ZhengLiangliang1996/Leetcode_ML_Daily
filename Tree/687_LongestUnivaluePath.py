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
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Could refer to # 543 Diameter of Binary Tree
        self.res = 0
        
        def dfs(root):
            if not root:
                 return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            pl, pr = 0, 0 
            if root.left and root.val == root.left.val:
                pl = l + 1
            if root.right and root.val == root.right.val:
                pr = r + 1
            
            self.res = max(pl+pr, self.res)
            
            return max(pl, pr) 
        
        dfs(root)
        
        return self.res
            
            
