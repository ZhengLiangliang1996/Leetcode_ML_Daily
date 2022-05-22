#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        if n == 0: return 0
        d = collections.defaultdict(list)
        
        for i in range(len(manager)):
            d[manager[i]].append(i)
        res = informTime[headID]
        # BFS traversal all 
        
        q, res = [(headID, 0)], 0
        while q:
            newQ = []
            for (idx, time) in q:
                res = max(res, time)
                for k in d[idx]:
                    newQ += [(k, time + informTime[idx])]
            q = newQ
        return res
