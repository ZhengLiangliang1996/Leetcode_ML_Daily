#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        res = 0
        laser = []
        for i in range(len(bank)):
            if bank[i].count('1') > 0:
                laser.append(bank[i].count('1'))
        
        for i in range(1, len(laser)):
            res += laser[i]*laser[i-1]
        
        return res 
