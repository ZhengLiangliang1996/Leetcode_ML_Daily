#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m,n = len(mat), len(mat[0])
        if r * c != m * n: return mat  # Invalid size -> return original matrix
        res = [[0]*c for _ in range(r)]
        for i in range(m*n):
            res[i//c][i%c] = mat[i // n][i % n]
        
        return res
