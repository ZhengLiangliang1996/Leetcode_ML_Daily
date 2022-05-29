#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt = collections.Counter(s)
        cnt_t = collections.Counter(target)
        res = float('inf')
        for i in range(len(target)):
            if target[i] not in cnt:
                return 0
            else:
                f = cnt_t[target[i]]
                res = min(cnt[target[i]] // f, res)
                
        return res 
