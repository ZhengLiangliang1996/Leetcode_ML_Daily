#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:  
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == len(s): return 1
            ans = 0
            if s[i] != '0':  # Single digit
                ans += dp(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and ord(s[i + 1]) <= ord('6')):  # Two digits
                ans += dp(i + 2)
            return ans

        return dp(0) 
