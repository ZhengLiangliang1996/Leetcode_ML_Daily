#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        def prefixAligned(s, num):
            return s[:num] == '1'*num
        init = '0'*len(flips)
        res = 0
        
        for i,f in enumerate(flips):
            init = init[:f-1] + '1' + init[f:]
            if prefixAligned(init, i+1):
                res += 1
        
        return res 
