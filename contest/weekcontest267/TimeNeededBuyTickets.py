#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
class Solution(object):
    def timeRequiredToBuy(self, ts, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """

        res = 0 
        for t in ts:
            if t < ts[k]:
                res += t
            else:
                res += ts[k]
        
        # minus those after ts[k], only 1s for each 
        res -= len([x for x in ts[k+1:] if x >= ts[k]])
        
        return res 
