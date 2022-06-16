#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n == 1: return [0]  
        if n & 1 == 0:
            for x in range(1,n//2 + 1):
                res.extend([x, -x])
        else:
            for x in range(1,n//2 + 1):
                res.extend([x, -x])
            res.append(0)
        return res
