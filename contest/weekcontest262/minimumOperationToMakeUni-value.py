#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
'''
Points to note:

We dont really care about the matrix itself. We just want the values, so we can just safely ignore the matrix and treat it like an array.
We can do as many operations as we want with x as increment/decrement (hypothetically).
Point 2 helps prove an important concept.
If we can do infinte operations on any number with x, we should get all the possible numbers in the matrix. Think on it :)
If we dont get all the possible numbers, that means the solution doesnt exist

Hence, this helps us derive this,
let A, B be any numbers in the matrix.
(A-B) % x == 0
'''

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        res = 0
        l = []
        for v in grid:
            l.extend(v)
        l.sort()
        
        median = l[len(l) // 2]

        for v in l:
            if abs(v - median) % x != 0:
                return -1
            res += abs(v - median) // x
        
        return res 
