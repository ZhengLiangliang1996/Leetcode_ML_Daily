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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS 
        q = [root]
        step, res, m_s = 0, 0, float('-inf')
        while q:
            qSize = len(q)
            s = 0
            step += 1
            for i in range(qSize):
                r = q.pop(0)
                s += r.val
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            
            if s > m_s:
                res = step 
                m_s = s
        
        return res 
            
