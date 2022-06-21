#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = []
        for i in range(len(mat)):
            a.append((sum(mat[i]), i))
        
        res = []
        a.sort()
        for i in range(k):
            res.append(a[i][1])
        return res 
