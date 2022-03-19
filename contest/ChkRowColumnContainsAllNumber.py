#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.


class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix[0])
        def chk_num(l):
            for i in range(1, n+1):
                if i not in l:
                    return False
            return True 
        
        def column(matrix, i):
            return [row[i] for row in matrix]
        
        # check rows 
        for i in range(n):
            if chk_num(matrix[i]) == False:
                return False 
            if chk_num(column(matrix, i)) == False:
                return False
        return True 
