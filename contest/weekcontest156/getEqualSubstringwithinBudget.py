#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        res, i, cost = 0, 0, 0
        for j in range(len(s)):
            cost += abs(ord(s[j]) - ord(t[j]))
            if cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            
            res = max(res, j-i+1)
        
        return res 
        
