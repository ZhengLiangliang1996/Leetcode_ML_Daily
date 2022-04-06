#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@MacBook-Air>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        if current == correct: return 0
        
        c_hr, c_m = current.split(":")
        o_hr, o_m = correct.split(":")
        hr = int(o_hr) - int(c_hr)
        m = int(o_m) - int(c_m) + hr * 60
        res = m // 60
        m %= 60
        res += m // 15
        m %= 15
        res += m // 5
        m %= 5
        res += m
        
        return res 
        
