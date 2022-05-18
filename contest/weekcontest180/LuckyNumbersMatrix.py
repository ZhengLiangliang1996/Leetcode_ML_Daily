#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import numpy as np
        row_min, col_max = set(), set()
        for i in range(len(matrix)):
            row_min.add(min(matrix[i]))
        m = np.array(matrix)
        for i in range(len(matrix[0])):
            col_max.add(m[:, i].max())
        
        return list(row_min.intersection(col_max))
