#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if len(s) % k != 0:
            s = s + (fill * (k - len(s) % k))
        res = []
        for i in range(0,len(s)-k+1,k):
            res.append(s[i:i+k])
        
        return res 
