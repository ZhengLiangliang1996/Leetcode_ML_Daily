#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        
        for i in range(len(s)):
            cnt = collections.defaultdict(int)
            cnt[s[i]] += 1
            for j in range(i+1, len(s)):
                cnt[s[j]] += 1
                res += (max(cnt.values()) - min(cnt.values()))
        
        return res 
