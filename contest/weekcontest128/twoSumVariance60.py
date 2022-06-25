#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def numPairsDivisibleBy60(self, t: List[int]) -> int:
        seen = defaultdict(int)
        res = 0
        
        for time in t:
            mod = time % 60
            remain = 60 - mod if mod else 0
            res += seen[remain]
            seen[mod] += 1
        
        return res
