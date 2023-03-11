#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s_t, t_s = {}, {}
        for i in range(len(s)):
            if s[i] in s_t and t[i] in t_s:
                if s_t[s[i]] != t[i] or t_s[t[i]] != s[i]:
                    return False 
            elif s[i] not in s_t and t[i] not in t_s:
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
            else:
                return False 

        return True
