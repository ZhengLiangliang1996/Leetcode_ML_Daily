#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        res = []
        m, sum_m = len(rolls), sum(rolls)
        total = (m + n) * mean 
        rest = total - sum_m 
        
        if rest > n * 6 or rest < n * 1: return res 
        if rest % n == 0 and 1<= rest//n <= 6: return n*[rest//n]
        # greedy, take the maximum 6 every time unless the n 
        # is too small, 4 - 2 + 1 = 3 
        #               1 - 1 + 1 = 1 
        while rest:
            rollVal = min(rest - n + 1, 6) 
            rest -= rollVal  
            res.append(rollVal) 
            n -= 1 
        return res 
    
        
