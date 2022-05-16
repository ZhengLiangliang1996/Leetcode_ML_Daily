#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # binary to 3 as base 
        # base conversion 
        while n > 3:
            if n % 3 == 2:
                return False 
            n /= 3
        
        return n != 2 
            
        
        
