#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
from functools import lru_cache
class Solution(object):
    def beautifulArray(self, N):
        """
        :type n: int
        :rtype: List[int]
        """
        @lru_cache(None)
        def dfs(N):
            if N == 1: return (1,)
            t1 = dfs((N+1)//2)
            t2 = dfs(N//2)
            return [i*2-1 for i in t1] + [i*2 for i in t2]
        
        return dfs(N)
