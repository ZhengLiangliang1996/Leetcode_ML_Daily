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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(pathSum, root):
            
            if not root:
                return None 
            pathSum += root.val
            if not root.left and not root.right:
                return None if pathSum < limit else root
            
            root.left = dfs(pathSum, root.left)
            root.right = dfs(pathSum, root.right)
            # If after this process an interior node becomes a leaf (loses all of its children), then you know wasn't any descendant leaf with a "sufficient" path to the root, so the interior node gets deleted as well (the second return None if ...).
            return None if not root.left and not root.right else root
    
        return dfs(0, root)
            
