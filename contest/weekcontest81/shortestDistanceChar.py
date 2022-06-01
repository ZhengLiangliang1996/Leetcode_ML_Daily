#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        for i in range(len(s)):
            l,r = float('inf'), float('inf')
            if c in s[i:]:
                l = s[i:].index(c)
            if c in s[:i+1]:
                r = s[:i+1][::-1].index(c)
            res.append(min(l, r))
        return res 
