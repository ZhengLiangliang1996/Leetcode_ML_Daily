#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maximumEvenSplit(self, f):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        ans, i = [], 2
        if f % 2 == 0:
            while i <= f:
                ans.append(i)
                f -= i
                i += 2
            ans[-1] += f
            
        return ans
        
