#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0

        count = [0]*26
        res, max_freq = 1, 1 
        left = 0
        # right - left + 1 is the final length we need
        # max_freq is the actual symbols thats present 
        # k is the tolerant number of char could be changed 
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])

            # check if change is needed 
            if (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
