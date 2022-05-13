#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = '123456789'
        
        low_num = len(str(low))
        high_num = len(str(high)) 
        res = []
        for i in range(len(s)):
            for j in range(low_num, high_num+1):
                if int(s[i:i+j]) >= low and int(s[i:i+j]) <= high:
                    if int(s[i:i+j]) not in res:
                        res.append(int(s[i:i+j]))
        res.sort()
        return res 
            
