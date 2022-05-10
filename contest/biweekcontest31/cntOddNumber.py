#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # high and low are even
        # high and low are odd
        # high and low one of them is odd and another one is even
        if low & 1 == 0 and high & 1 == 0:              # 2 3 4 5 6 7 8  -> (8 - 2) // 2 
            return (high - low) // 2 
        elif low & 1 == 1 and high & 1 == 1:
            return ((high - low) // 2) + 1              # 3 4 5 6 7 8 9  ->  (9 - 3 ) // 2 + 1 
        else:
            return (high - low + 1) // 2# 4 5 6 7 8 9  -> (9 - 4 + 1) // 2 
        
            
