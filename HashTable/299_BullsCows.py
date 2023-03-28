#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def getHint(self, s: str, g: str) -> str:
        s_s, s_g = collections.defaultdict(list), collections.defaultdict(list)
        count_s, count_g = collections.defaultdict(int), collections.defaultdict(int)
        for i, x in enumerate(s):
            count_s[x] += 1
            s_s[x].append(i) 
        
        for i, x in enumerate(g):
            count_g[x] += 1
            s_g[x].append(i) 

        res_b, res_c = 0, 0
        for v in count_s.keys():
            if v in count_g.keys():
                res_c += min(count_s[v], count_g[v])
                for idx in s_s[v]:
                    if idx in s_g[v]:
                        res_b += 1
        
        return f"{res_b}A{res_c-res_b}B" if res_c > res_b else f"{res_b}A{res_c-res_b}B"

