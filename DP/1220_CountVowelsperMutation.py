#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, e, i, o, u, M = 1, 1, 1, 1, 1, 10**9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u)%M, (a + i)%M, (e + o)%M, i%M, (i + o)%M
        
        return (a + e + i + o + u)%M 
