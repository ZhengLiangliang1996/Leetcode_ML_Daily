#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def flipgame(self, f: List[int], b: List[int]) -> int:
        res = []
        imp = []
        for i in range(len(f)):
            if f[i] == b[i]:
                imp.append(f[i])
        for i in range(len(f)):
            if f[i] not in imp:
                res.append(f[i])
            if b[i] not in imp:
                res.append(b[i])        
        
        return 0 if not res else min(res)
