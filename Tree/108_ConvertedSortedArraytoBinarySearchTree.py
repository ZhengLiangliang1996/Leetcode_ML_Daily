#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None 
        mid = len(nums)//2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

        # transform the index 
        def buildBST(l, r):
            if l > r: return None 
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = buildBST(l, m-1)
            root.right = buildBST(m+1, r)
            return root 
        
        return buildBST(0, len(nums)-1)       
