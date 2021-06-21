#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def generate(self, numRows):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        
        result = []
        if numRows == 0:
            return result
        
        ps = [1]
        result.append(ps)
        
        for i in range(numRows-1):
            # zip : [1,4],[4,6] -> [1,4] [4,6] 
            ps = [sum(x) for x in zip([0] + ps, ps + [0])]
            result.append(ps)
        
        return result
