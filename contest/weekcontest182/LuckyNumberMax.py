#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = 0
        if not arr: return res 
        cnt = collections.Counter(arr)
        for k in cnt.keys():
            if cnt[k] == k:
                res = max(res, k)
                
        return -1 if res == 0 else res
