#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            tmp = ''
            if len(s) % k == 0:
                part = len(s) // k
            else:
                part = (len(s) // k) + 1
            for i in range(part):
                sub = s[i*k:i*k+k]
                tmp += str(sum([int(x) for x in sub]))
            s = tmp     
        return s 
