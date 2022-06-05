#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        # sliding window 
        n = len(f)

        res, l = float('-inf'), 0
        basket = collections.defaultdict(int)
        for r in range(n):
            f_tpy = f[r]
            basket[f_tpy] += 1
            
            if len(basket) <= 2:
                res = max(res, r - l + 1)
            # while condition not met
            while len(basket) > 2:
                basket[f[l]] -= 1
                if basket[f[l]] == 0:
                    del basket[f[l]]
                l += 1

        return res  
