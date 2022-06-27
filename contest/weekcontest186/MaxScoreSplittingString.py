#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            l_cnt = collections.Counter(s[:i])
            r_cnt = collections.Counter(s[i:])
            if '0' not in l_cnt:
                l = 0
            else:
                l = l_cnt['0']
            if '1' not in r_cnt:
                r = 0
            else:
                r = r_cnt['1']
            res = max(res, l+r)
        return res 
