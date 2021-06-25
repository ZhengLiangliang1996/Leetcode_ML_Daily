#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def findRoot(x, tree):
            if tree[x] == -1: return x
            else:
                root = findRoot(tree[x], tree)
                tree[x] = root
                return root
                
        # Union Find 
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = findRoot(edge[0], tree)
            b = findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge
