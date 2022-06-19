#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def numofConnectedComponent(self, n: int, c: List[List[int]]) -> int:
        # at least n-1 edges 
        e = len(c)
        if e < n-1: return -1
        
        # create graph 
        graph = collections.defaultdict(set)
        visit = set()
        for u,v in c:
            graph[u].add(v)
            graph[v].add(u)
        
        
        def dfs(g, v, i):
            # mark as visited 
            v.add(i)
            if i in g:
                for j in g[i]:
                    if j not in visit:
                        dfs(g, v, j)
            
        res = 0
        for i in range(n):
            if i not in visit:
                # iterating over all nodes as start point 
                dfs(graph, visit, i)
                res += 1
                
        # res operations = Number of connected components - 1
        return res
