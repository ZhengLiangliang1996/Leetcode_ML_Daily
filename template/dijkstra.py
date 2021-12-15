#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

import heapq
class Solution(object):
    def minimumEffortPath(self, h):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        d = [0,1,0,-1,0]
        def neighbor(x, y, m, n):
            res = [] 
            for k in range(4):
                x1 = x + d[k]
                y1 = y + d[k+1]
                if 0 <= x1 < m and 0 <= y1 < n:
                    # define your own distance here
                    res.append(((x1, y1), h[x1][y1]))
            return res 
        
        def dijkstra(start, target, graph):
            q = [(0, start)]
            visited = set()
            
            while q: 
                curr_dist, curr_node = heapq.heappop(q)
                
                if curr_node == target:
                    return curr_dist
                
                if curr_node in visited: continue 
                visited.add(curr_node)
                
                for ngh_node, ngh_dist in graph[curr_node]:
                    # define your own dist accumulation way here 
                    # could be max diff, default is +  
                    heapq.heappush(q, (curr_dist+ngh_dist, ngh_node))
                    
            return -1 
                              
        m, n = len(h), len(h[0])
        # graph[node] = [(ngh, ngh_dist))]
        graph = {}
        for i in range(m):
            for j in range(n):
                graph[(i, j)] = neighbor(i, j, m, n)
                

        res = dijkstra((0, 0), (m-1, n-1), graph)
        return res 
        
            
        
        
        
        
        
        

