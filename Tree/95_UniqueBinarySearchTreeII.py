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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        @lru_cache(None)
        def dfs(left, right):
            if left > right: return [None] 
            if left == right: return [TreeNode(left)]
            res = []
            for root in range(left, right+1):
                leftNodes = dfs(left, root-1)
                rightNodes = dfs(root+1, right)
                for l in leftNodes:
                    for r in rightNodes:
                        t = TreeNode(root, l, r)
                        res.append(t)
                        
            return res
        return dfs(1, n) 
    
        
