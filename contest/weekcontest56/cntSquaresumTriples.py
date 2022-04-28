#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        z = [x**2 for x in range(5, n+1)]
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i**2 + j**2 in z:
                    res += 2
        return res 
