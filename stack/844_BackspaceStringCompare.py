#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_a, res_b = [], []
        for i in range(len(s)):
            if s[i] == '#':
                if res_a:
                    res_a.pop()
            else:
                res_a.append(s[i])
        
        for i in range(len(t)):
            if t[i] == '#':
                if res_b:
                    res_b.pop()
            else:
                res_b.append(t[i])
        
        return ''.join(res_a) == ''.join(res_b)
