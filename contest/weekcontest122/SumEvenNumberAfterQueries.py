#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def sumEvenAfterQueries(self, n: List[int], q: List[List[int]]) -> List[int]:
        res = []
        s =  0
        for j in range(len(n)):
            if n[j] & 1 == 0:
                s += n[j]
        for i in range(len(q)):
            tmp = n[q[i][1]]
            n[q[i][1]] += q[i][0]
            if tmp & 1 == 1 and n[q[i][1]] & 1 == 0:
                s += n[q[i][1]]
            elif tmp & 1 == 0 and n[q[i][1]] & 1 == 0:
                s = s - tmp + n[q[i][1]]
            elif tmp & 1 == 0 and n[q[i][1]] & 1 == 1:
                s -= tmp 
                
            res.append(s)
        
        return res
