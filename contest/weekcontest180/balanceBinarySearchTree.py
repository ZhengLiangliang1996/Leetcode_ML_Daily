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
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        eles = []
        # get all the sorted elements using inorder 
        def inorder(root):
            if not root:
                return None 
            inorder(root.left)
            eles.append(root.val)
            inorder(root.right)
        inorder(root)
        
        def buildBST(l, r):
            mid = (l + r) // 2
            buildBST()
            
        
