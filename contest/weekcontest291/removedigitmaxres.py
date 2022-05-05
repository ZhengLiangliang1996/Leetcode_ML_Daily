#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        m = float('-inf')
        for i in range(len(number)):
            if number[i] == digit:
                m = max(m, int(number[:i]+number[i+1:]))
        
        return str(m)
        
