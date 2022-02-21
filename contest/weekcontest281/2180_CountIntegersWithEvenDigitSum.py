#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def sumEven(n):
            sn = str(n)
            res = 0
            for i in sn:
                res += int(i)
            return 1 if res % 2 == 0 else 0
        
        res = 0 
        for i in range(1, num+1):
            res += sumEven(i)
        
        return res 
