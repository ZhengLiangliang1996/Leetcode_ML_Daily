#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = collections.Counter(chars)
        res = 0
        for w in words:
            w_cnt = collections.Counter(w)
            res += len(w)
            for k in w_cnt.keys():
                if k not in cnt or w_cnt[k] > cnt[k]:
                    res -= len(w)
                    break
            
        return res 
