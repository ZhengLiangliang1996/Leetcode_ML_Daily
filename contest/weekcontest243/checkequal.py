#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def isSumEqual(self, f: str, s: str, t: str) -> bool:
        
        def transform(s):
            res = ''
            for i in s:
                res += str(ord(i) - 97)
            
            return int(res)
        
        return transform(f)+transform(s) == transform(t)
