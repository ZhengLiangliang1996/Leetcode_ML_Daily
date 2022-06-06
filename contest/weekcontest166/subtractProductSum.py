#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        p, s = 1, 0
        for i in range(len(str(n))):
            p *= int(n[i])
            s += int(n[i])
        return p - s
