#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {'0': 0, '01': 0, '010': 0, '1':0, '10':0, '101':0}
        for i in s:
            if i == '0':
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            if i == '1':
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
        
        return dp['101'] + dp['010']
                
