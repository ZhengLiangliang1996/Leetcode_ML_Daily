#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def maxValue(self, n: str, x: int) -> str:

        i = 0
        if n[0] == "-":
            i += 1
            while i < len(n) and int(n[i]) <= x:
                i += 1
        else:
            while i < len(n) and int(n[i]) >= x:
                i += 1
        return n[:i] + str(x) + n[i:]
