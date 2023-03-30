#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        if not s: return 0
        s = [-1*x for x in s]
        heapq.heapify(s)

        while len(s) > 1:
            s1 = heapq.heappop(s)
            s2 = heapq.heappop(s)
            if s1 != s2:
                s1 *= -1
                s2 *= -1
                s1 -= s2 
                heapq.heappush(s, -s1)
        
        return -s[0] if s else 0
