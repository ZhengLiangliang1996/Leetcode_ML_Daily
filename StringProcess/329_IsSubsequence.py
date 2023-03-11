#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        
        for i in range(len(t)):
            if s[0] == t[i]:
                s = s[1:]  
                if not s:
                    return True 
        return False 
