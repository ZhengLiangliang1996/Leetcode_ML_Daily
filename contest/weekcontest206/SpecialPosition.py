#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        res = 0
        def chk(x, y):
            rs, cs = 0, 0
            for i in range(len(m)):
                cs += m[i][y]
            for i in range(len(m[0])):
                rs += m[x][i]
            return cs == 1 and rs == 1 
        
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == 1 and chk(i, j):
                    res += 1
                    
        return res 
