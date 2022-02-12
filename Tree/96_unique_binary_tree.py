#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.


class Solution(object):
    def __init__(self):
        self.dp = dict()
        
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.dp: return self.dp[n]
        if n <= 1: return 1 
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        self.dp[n] = res 
        return res 
            
