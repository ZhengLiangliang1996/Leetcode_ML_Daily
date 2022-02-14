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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return None 
        
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue 
            res.append(node)
            stack.append(node.right)
            stack.append(node.left)
        
        for i in range(len(res)-1):
            res[i].left = None 
            res[i].right = res[i+1]
        
        return res[0]
        
        
