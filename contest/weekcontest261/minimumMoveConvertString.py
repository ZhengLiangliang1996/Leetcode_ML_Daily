#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        while s: 
            if 'X' in s:
                idx = s.index('X')
                s = s[idx+3:]
                res += 1
            else:
                break
        return res 
