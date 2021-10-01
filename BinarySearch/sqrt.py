#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 liangliang <liangliang@Liangliangs-Air.localdomain>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l = 0
        r = int(x // 2)
        
        while l <= r:
            mid = l + ((r - l) >> 1)
            
            if mid*mid == x:
                return mid 
            elif mid*mid < x: 
                l = mid + 1
            else:
                r = mid - 1
        return l-1
