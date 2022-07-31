#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        # tricky greedy 
        # sort -> [10,6,12,7,3,5] 
        # 3 5 6 7 10 12 
        # g1: 3 
        # g2: 5, 6
        # g3: 7, 10, 12 
        # 1 + 2 + 3 + ... k <= n -> k will be the answer 
        n, k = len(grades), 0
        
        while n - k > 0:
            k += 1
            n -= k
        
        return k
