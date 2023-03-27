#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s, len_p = len(s), len(p)
        if len_s < len_p: return res 
        count_p = collections.defaultdict(int)
        count_s = collections.defaultdict(int)
        for i in range(len_p):
            count_p[p[i]] += 1

        for i in range(len(s)):
            if i >= len(p):
                count_s[s[i-len_p]] -= 1
                if s[i-len_p] not in count_p:
                    count_p[s[i-len_p]] = 0
            count_s[s[i]] += 1
            if count_s == count_p:
                res.append(i - len_p + 1)
        
        return res 
