#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, max_rcd):
            if not root:
                return 0
            
            good = 1 if root.val>=max_rcd else 0
            
            #Checking if current node is greater than max_so_far 
            max_rcd = max(max_rcd, root.val)
            
            #returning total of current good , no. of good nodes in left and right
            return good + dfs(root.left, max_rcd) + dfs(root.right, max_rcd)
        
        return dfs(root, float('-inf'))
