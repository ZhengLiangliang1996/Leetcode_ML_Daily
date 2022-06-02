#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def numTilePossibilities(self, t: str) -> int:
        self.res = 0
        
        if not t:
            return 0
        used = [0] * len(t)
        
        def backtrack(path):
            if path:
                self.res += 1
                #return
            
            for i in range(len(t)):
                if i > 0 and t[i] == t[i - 1] and not used[i - 1]:
                    continue
                if used[i]:
                    continue
                used[i] = 1
                backtrack(path + t[i])
                used[i] = 0
        t = sorted(t)
        backtrack('')
        
        return self.res
