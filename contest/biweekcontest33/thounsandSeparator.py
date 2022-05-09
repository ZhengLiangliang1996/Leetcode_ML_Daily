#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        n, l = str(n), len(str(n))
        if l < 4: return str(n)
        res = ""
        for i in range(l):
            if (l-i) % 3 == 0:
                res += "."
            res += n[i]
        return res if res[0] != "." else res[1:]
