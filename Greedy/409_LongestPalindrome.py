#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        # calculate the even paris
        for v in count.values():
            res += v // 2 * 2
        # if there is odd left, only take 1 out 
        if any([v % 2 == 1 for v in count.values()]):
            res += 1

        return res 
